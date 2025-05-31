import streamlit as st
import streamlit.components.v1 as components

# ──────────────────────────────────────────────────────────────────────────────
# 1. STREAMLIT PAGE CONFIG ← MUST BE FIRST
# ──────────────────────────────────────────────────────────────────────────────
st.set_page_config(layout="wide")

# ──────────────────────────────────────────────────────────────────────────────
# 2. LOAD BOOTSTRAP CSS FOR CONSISTENT STYLING
# ──────────────────────────────────────────────────────────────────────────────
# (This invisible components.html call injects the Bootstrap CDN.)
components.html(
    """
    <link
      rel="stylesheet"
      href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css"
      integrity="sha384-JcKb8q3iqJ61gNVpCF9KX0BxV7IjE2DaJoFvVda3mYIxVXMmDkFfVfW5y3NgVXz9"
      crossorigin="anonymous"
    >
    """,
    height=0,
    width=0,
)

# ──────────────────────────────────────────────────────────────────────────────
# 3. ADD CSS TO ENSURE BUTTONS SHOW POINTER CURSOR ALWAYS
# ──────────────────────────────────────────────────────────────────────────────
st.markdown(
    """
    <style>
    /* Make all Streamlit buttons use pointer cursor */
    div.stButton > button {
        cursor: pointer !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ──────────────────────────────────────────────────────────────────────────────
# 4. INITIALIZE THEME IN SESSION STATE (DEFAULT = DARK)
# ──────────────────────────────────────────────────────────────────────────────
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = True

def _toggle_theme():
    st.session_state.dark_mode = not st.session_state.dark_mode

# ──────────────────────────────────────────────────────────────────────────────
# 5. HEADER WITH TITLE + ICON‐ONLY THEME TOGGLE
# ──────────────────────────────────────────────────────────────────────────────
col_title, col_toggle = st.columns([9, 1])
with col_title:
    st.title("Analysis")
with col_toggle:
    # Black & white Unicode glyphs:
    #   ☾ (U+263D) = First Quarter Moon (outline)
    #   ☀ (U+2600) = Sun (outline)
    icon = "☀" if st.session_state.dark_mode else "☾"
    st.button(icon, key="theme_toggle", on_click=_toggle_theme)

theme = "dark" if st.session_state.dark_mode else "light"

# ──────────────────────────────────────────────────────────────────────────────
# 6. SYMBOL INPUT
# ──────────────────────────────────────────────────────────────────────────────
symbol = st.text_input(
    "Enter a ticker symbol (e.g. NASDAQ:AAPL, FX:EURUSD, etc.)",
    value="NASDAQ:AAPL"
)

# ──────────────────────────────────────────────────────────────────────────────
# 7. FULL WIDTH – SYMBOL INFO
# ──────────────────────────────────────────────────────────────────────────────
st.markdown("---")
components.html(
    f"""
    <!-- TradingView Symbol Info Widget BEGIN -->
    <div style="width:100%;">
      <div class="tradingview-widget-container">
        <div class="tradingview-widget-container__widget"></div>
        <script type="text/javascript"
                src="https://s3.tradingview.com/external-embedding/embed-widget-symbol-info.js"
                async>
        {{
          "symbol": "{symbol}",
          "height": 300,
          "locale": "en",
          "colorTheme": "{theme}",
          "isTransparent": true,
          "width": "100%"
        }}
        </script>
      </div>
    </div>
    <!-- TradingView Symbol Info Widget END -->
    """,
    height=250,
)

# ──────────────────────────────────────────────────────────────────────────────
# 8. FULL WIDTH – ADVANCED CHART
# ──────────────────────────────────────────────────────────────────────────────
components.html(
    f"""
    <!-- TradingView Advanced Chart Widget BEGIN -->
    <div style="width:100%;">
      <div class="tradingview-widget-container">
        <div class="tradingview-widget-container__widget"></div>
        <script type="text/javascript"
                src="https://s3.tradingview.com/external-embedding/embed-widget-advanced-chart.js"
                async>
        {{
          "width": "100%",
          "height": 610,
          "symbol": "{symbol}",
          "interval": "D",
          "timezone": "Etc/UTC",
          "theme": "{theme}",
          "style": "1",
          "locale": "en",
          "allow_symbol_change": true,
          "support_host": "https://www.tradingview.com"
        }}
        </script>
      </div>
    </div>
    <!-- TradingView Advanced Chart Widget END -->
    """,
    height=650,
)

# ──────────────────────────────────────────────────────────────────────────────
# 9. HALF WIDTH – COMPANY PROFILE & TECHNICAL ANALYSIS
# ──────────────────────────────────────────────────────────────────────────────
st.markdown("---")
col1, col2 = st.columns(2)

# COMPANY PROFILE
with col1:
    st.header("Company Profile")
    components.html(
        f"""
        <!-- TradingView Symbol Profile BEGIN -->
        <div style="width:100%;">
          <div class="tradingview-widget-container">
            <div class="tradingview-widget-container__widget"></div>
            <script type="text/javascript"
                    src="https://s3.tradingview.com/external-embedding/embed-widget-symbol-profile.js"
                    async>
            {{
              "symbol": "{symbol}",
              "width": "100%",
              "height": "500",
              "locale": "en",
              "colorTheme": "{theme}",
              "isTransparent": true
            }}
            </script>
          </div>
        </div>
        <!-- TradingView Symbol Profile END -->
        """,
        height=500,
    )

# TECHNICAL ANALYSIS
with col2:
    st.header("Technical Analysis")
    components.html(
        f"""
        <!-- TradingView Technical Analysis BEGIN -->
        <div style="width:100%;">
          <div class="tradingview-widget-container">
            <div class="tradingview-widget-container__widget"></div>
            <script type="text/javascript"
                    src="https://s3.tradingview.com/external-embedding/embed-widget-technical-analysis.js"
                    async>
            {{
              "interval": "1m",
              "width": "100%",
              "height": 450,
              "symbol": "{symbol}",
              "showIntervalTabs": true,
              "displayMode": "single",
              "locale": "en",
              "colorTheme": "{theme}",
              "isTransparent": true
            }}
            </script>
          </div>
        </div>
        <!-- TradingView Technical Analysis END -->
        """,
        height=500,
    )

# ──────────────────────────────────────────────────────────────────────────────
# 10. FULL WIDTH – FINANCIALS OVERVIEW (NO SCROLL)
# ──────────────────────────────────────────────────────────────────────────────
st.markdown("---")
st.subheader("Financials Overview")
components.html(
    f"""
    <!-- TradingView Financials Widget BEGIN -->
    <div style="width:100%;">
      <div class="tradingview-widget-container">
        <div class="tradingview-widget-container__widget"></div>
        <script type="text/javascript"
                src="https://s3.tradingview.com/external-embedding/embed-widget-financials.js"
                async>
        {{
          "isTransparent": true,
          "largeChartUrl": "",
          "displayMode": "regular",
          "width": "100%",
          "height": 1200,
          "colorTheme": "{theme}",
          "symbol": "{symbol}",
          "locale": "en"
        }}
        </script>
      </div>
    </div>
    <!-- TradingView Financials Widget END -->
    """,
    height=1200,
)
