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
  <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-screener.js" async>
  {
  "width": "100%",
  "height": "800",
  "defaultColumn": "overview",
  "defaultScreen": "general",
  "market": "forex",
  "showToolbar": true,
  "colorTheme": "dark",
  "locale": "en"
}
  </script>
</div>
<!-- TradingView Widget END -->
""", height=800)



