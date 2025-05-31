import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")  # Full-width layout

st.title("Forex")

# FULL WIDTH - FOREX HEATMAP
st.header("Forex heatmap")
components.html("""
<!-- TradingView Widget BEGIN -->
<div class="tradingview-widget-container">
  <div class="tradingview-widget-container__widget"></div>
  <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-forex-heat-map.js" async>
  {
  "width": "100%",
  "height": "500",
  "currencies": [
    "EUR",
    "USD",
    "JPY",
    "GBP",
    "CHF",
    "AUD",
    "CAD",
    "NZD",
    "CNY"
  ],
  "isTransparent": true,
  "colorTheme": "dark",
  "locale": "en",
  "backgroundColor": "#1D222D"
}
  </script>
</div>
<!-- TradingView Widget END -->
""", height=500)




# FULL WIDTH - FOREX CROSS RATES
st.header("Forex cross rates")
components.html("""
<!-- TradingView Widget BEGIN -->
<div class="tradingview-widget-container">
  <div class="tradingview-widget-container__widget"></div>
  <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-forex-cross-rates.js" async>
  {
  "width": "100%",
  "height": "500",
  "currencies": [
    "EUR",
    "USD",
    "JPY",
    "GBP",
    "CHF",
    "AUD",
    "CAD",
    "NZD",
    "CNY"
  ],
  "isTransparent": true,
  "colorTheme": "dark",
  "locale": "en",
  "backgroundColor": "#000000"
}
  </script>
</div>
<!-- TradingView Widget END -->
""", height=500)