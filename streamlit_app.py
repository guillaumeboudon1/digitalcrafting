import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import requests
from datetime import datetime

# Tradier API setup
TRADIER_TOKEN = "iViIAlWJosRyQaxsyqr6lW8ULSlg"
TRADIER_URL = "https://sandbox.tradier.com/v1/markets/options/chains"
TRADIER_ORDER_URL = "https://sandbox.tradier.com/v1/accounts/{account_id}/orders"
HEADERS = {"Authorization": f"Bearer {TRADIER_TOKEN}", "Accept": "application/json"}

ACCOUNT_ID = "VA27940677"  # Sandbox account

st.set_page_config(page_title="Options Strategy Builder", layout="wide")
st.title("🧮 Advanced Options Strategy Builder")

symbol = st.text_input("Enter Ticker Symbol", value="AAPL").upper()

if 'strategy_legs' not in st.session_state:
    st.session_state['strategy_legs'] = []

# Get underlying price
@st.cache_data(ttl=300)
def get_underlying_price(symbol):
    url = f"https://sandbox.tradier.com/v1/markets/quotes"
    params = {"symbols": symbol}
    r = requests.get(url, headers=HEADERS, params=params)
    data = r.json()
    quote = data.get("quotes", {}).get("quote", {})
    return quote.get("last", 0)

underlying_price = get_underlying_price(symbol)

# Get expirations from Tradier
@st.cache_data(ttl=300)
def get_expirations(symbol):
    url = f"https://sandbox.tradier.com/v1/markets/options/expirations"
    params = {"symbol": symbol, "includeAllRoots": "true", "strikes": "false"}
    r = requests.get(url, headers=HEADERS, params=params)
    data = r.json()
    return data.get("expirations", {}).get("date", [])

expirations = get_expirations(symbol)
if not expirations:
    st.warning("No options data available for this symbol.")
    st.stop()

formatted_expirations = [datetime.strptime(exp, "%Y-%m-%d").strftime("%b %d %Y") for exp in expirations]
selected_exp_idx = st.selectbox("Choose Expiration:", range(len(formatted_expirations)), format_func=lambda x: formatted_expirations[x])
selected_exp_date = expirations[selected_exp_idx]

# Get option chain from Tradier
@st.cache_data(ttl=300)
def get_option_chain(symbol, expiration):
    params = {"symbol": symbol, "expiration": expiration, "greeks": "true"}
    r = requests.get(TRADIER_URL, headers=HEADERS, params=params)
    data = r.json()
    options = data.get("options", {}).get("option", [])
    return pd.DataFrame(options)

option_df = get_option_chain(symbol, selected_exp_date)
if option_df.empty:
    st.warning("No chain data returned.")
    st.stop()

st.subheader("Option Chain")
strikes = sorted(option_df['strike'].unique())
headers = ["Call Bid (Sell)", "Call Ask (Buy)", "Strike", "Put Bid (Sell)", "Put Ask (Buy)"]
header_cols = st.columns(len(headers))
for i, h in enumerate(headers):
    header_cols[i].markdown(f"**{h}**")

for strike in strikes:
    row_cols = st.columns(len(headers))
    call = option_df[(option_df['strike'] == strike) & (option_df['option_type'] == 'call')].iloc[0].fillna(0)
    put = option_df[(option_df['strike'] == strike) & (option_df['option_type'] == 'put')].iloc[0].fillna(0)

    call_bid = call.get('bid') or 0
    call_ask = call.get('ask') or 0
    put_bid = put.get('bid') or 0
    put_ask = put.get('ask') or 0

    if row_cols[0].button(f"{call_bid:.2f}", key=f"sell_call_{strike}"):
        st.session_state['strategy_legs'].append({'side': 'sell_to_open', 'price': call_bid, 'option_type': 'call', 'strike': strike, 'expiration': selected_exp_date, 'quantity': 1})
    if row_cols[1].button(f"{call_ask:.2f}", key=f"buy_call_{strike}"):
        st.session_state['strategy_legs'].append({'side': 'buy_to_open', 'price': call_ask, 'option_type': 'call', 'strike': strike, 'expiration': selected_exp_date, 'quantity': 1})

    row_cols[2].markdown(f"**{strike}**")

    if row_cols[3].button(f"{put_bid:.2f}", key=f"sell_put_{strike}"):
        st.session_state['strategy_legs'].append({'side': 'sell_to_open', 'price': put_bid, 'option_type': 'put', 'strike': strike, 'expiration': selected_exp_date, 'quantity': 1})
    if row_cols[4].button(f"{put_ask:.2f}", key=f"buy_put_{strike}"):
        st.session_state['strategy_legs'].append({'side': 'buy_to_open', 'price': put_ask, 'option_type': 'put', 'strike': strike, 'expiration': selected_exp_date, 'quantity': 1})

if st.session_state['strategy_legs']:
    st.subheader("Selected Legs")
    for idx, leg in enumerate(st.session_state['strategy_legs']):
        cols = st.columns(7)
        with cols[0]:
            st.write(f"Leg {idx+1}")
        with cols[1]:
            leg['option_type'] = st.selectbox("Type", ["call", "put"], index=0 if leg['option_type']=='call' else 1, key=f"type_{idx}")
        with cols[2]:
            leg['side'] = st.selectbox("Side", ["buy_to_open", "sell_to_open"], index=0 if leg['side']=='buy_to_open' else 1, key=f"side_{idx}")
        with cols[3]:
            leg['strike'] = st.number_input("Strike", value=leg['strike'], key=f"strike_{idx}")
        with cols[4]:
            leg['price'] = st.number_input("Price", value=leg['price'], key=f"price_{idx}")
        with cols[5]:
            leg['quantity'] = st.number_input("Qty", value=leg['quantity'], min_value=1, key=f"qty_{idx}")
        with cols[6]:
            if st.button("Delete", key=f"delete_{idx}"):
                st.session_state['strategy_legs'].pop(idx)
                st.experimental_rerun()

    price_range = np.linspace(underlying_price * 0.7, underlying_price * 1.3, 500)
    total_pl = np.zeros_like(price_range)
    total_credit = 0

    for leg in st.session_state['strategy_legs']:
        strike, premium, qty = leg['strike'], leg['price'], leg['quantity']
        payoff = np.where(price_range > strike, price_range - strike - premium, -premium) if leg['option_type']=='call' else np.where(price_range < strike, strike - price_range - premium, -premium)
        if leg['side'] == 'sell_to_open': payoff *= -1
        total_pl += payoff * qty
        total_credit += (premium if leg['side'] == 'sell_to_open' else -premium) * qty

    max_profit = np.max(total_pl)
    max_loss = np.min(total_pl)

    fig = go.Figure()
    profit_mask = total_pl >= 0
    loss_mask = total_pl < 0
    fig.add_trace(go.Scatter(x=price_range[profit_mask], y=total_pl[profit_mask], fill='tozeroy', name='Profit', line=dict(color='green')))
    fig.add_trace(go.Scatter(x=price_range[loss_mask], y=total_pl[loss_mask], fill='tozeroy', name='Loss', line=dict(color='red')))
    fig.update_layout(title='Payoff Chart', xaxis_title='Underlying Price', yaxis_title='Profit / Loss', hovermode='x unified')
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Summary")
    st.write(f"Net Premium: {total_credit:.2f}")
    st.write(f"Max Profit: {max_profit:.2f}")
    st.write(f"Max Loss: {max_loss:.2f}")

    if st.button("Send Paper Trade"):
        orders = []
        for leg in st.session_state['strategy_legs']:
            orders.append({
                "class": "option",
                "symbol": symbol,
                "option_type": leg['option_type'],
                "side": leg['side'].replace('_to_open',''),
                "quantity": leg['quantity'],
                "price": leg['price'],
                "strike": leg['strike'],
                "expiration_date": leg['expiration']
            })
        st.success("Order prepared for paper trade (simulation only).")

    if st.button("Clear All"):
        st.session_state['strategy_legs'] = []
