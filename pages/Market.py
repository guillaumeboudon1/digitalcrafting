import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")  # Full-width layout
st.title("Market Overview")

col1, col2 = st.columns(2)

# ──────────────────────────────────────────────────────────────────────────────
# TOP STORIES
# ──────────────────────────────────────────────────────────────────────────────
with col1:
    # Use st.header (less vertical margin than st.title)
    st.header("Top stories")
    components.html(
        """
        <!-- TradingView Widget BEGIN -->
        <div class="tradingview-widget-container">
          <div class="tradingview-widget-container__widget"></div>
          <script
            type="text/javascript"
            src="https://s3.tradingview.com/external-embedding/embed-widget-timeline.js"
            async
          >
          {
            "feedMode": "all_symbols",
            "isTransparent": true,
            "displayMode": "regular",
            "width": "100%",
            "height": "600",
            "colorTheme": "dark",
            "locale": "en"
          }
          </script>
        </div>
        <!-- TradingView Widget END -->
        """,
        height=600,
    )

# ──────────────────────────────────────────────────────────────────────────────
# ECONOMIC CALENDAR
# ──────────────────────────────────────────────────────────────────────────────
with col2:
    # Again, use st.header instead of st.title
    st.header("Economic calendar")
    components.html(
        """
        <!-- TradingView Widget BEGIN -->
        <div class="tradingview-widget-container">
          <div class="tradingview-widget-container__widget"></div>
          <script
            type="text/javascript"
            src="https://s3.tradingview.com/external-embedding/embed-widget-events.js"
            async
          >
          {
            "colorTheme": "dark",
            "isTransparent": true,
            "width": "100%",
            "height": "600",
            "locale": "en",
            "importanceFilter": "-1,0,1",
            "countryFilter": "ar,au,br,ca,cn,fr,de,in,id,it,jp,kr,mx,ru,sa,za,tr,gb,us,eu"
          }
          </script>
        </div>
        <!-- TradingView Widget END -->
        """,
        height=600,
    )

st.markdown("---")

# ──────────────────────────────────────────────────────────────────────────────
# FULL-WIDTH MARKET OVERVIEW (unchanged)
# ──────────────────────────────────────────────────────────────────────────────
components.html(
    """
    <!-- TradingView Widget BEGIN -->
    <div class="tradingview-widget-container">
      <div class="tradingview-widget-container__widget"></div>
      <script
        type="text/javascript"
        src="https://s3.tradingview.com/external-embedding/embed-widget-market-overview.js"
        async
      >
      {
        "colorTheme": "dark",
        "dateRange": "12M",
        "showChart": true,
        "locale": "en",
        "largeChartUrl": "",
        "isTransparent": true,
        "showSymbolLogo": true,
        "showFloatingTooltip": false,
        "height": "800",
        "plotLineColorGrowing": "rgba(41, 98, 255, 1)",
        "plotLineColorFalling": "rgba(41, 98, 255, 1)",
        "gridLineColor": "rgba(42, 46, 57, 0)",
        "scaleFontColor": "rgba(219, 219, 219, 1)",
        "belowLineFillColorGrowing": "rgba(41, 98, 255, 0.12)",
        "belowLineFillColorFalling": "rgba(41, 98, 255, 0.12)",
        "belowLineFillColorGrowingBottom": "rgba(41, 98, 255, 0)",
        "belowLineFillColorFallingBottom": "rgba(41, 98, 255, 0)",
        "symbolActiveColor": "rgba(41, 98, 255, 0.12)",
        "tabs": [
          {
            "title": "Indices",
            "symbols": [
              {"s": "FOREXCOM:SPXUSD", "d": "S&P 500 Index"},
              {"s": "FOREXCOM:NSXUSD", "d": "US 100 Cash CFD"},
              {"s": "FOREXCOM:DJI",   "d": "Dow Jones Industrial Average Index"},
              {"s": "INDEX:NKY",      "d": "Japan 225"},
              {"s": "INDEX:DEU40",    "d": "DAX Index"},
              {"s": "FOREXCOM:UKXGBP","d": "FTSE 100 Index"}
            ],
            "originalTitle": "Indices"
          },
          {
            "title": "Forex",
            "symbols": [
              {"s": "FX:EURUSD",  "d": "EUR to USD"},
              {"s": "FX:GBPUSD",  "d": "GBP to USD"},
              {"s": "FX:USDJPY",  "d": "USD to JPY"},
              {"s": "FX:USDCHF",  "d": "USD to CHF"},
              {"s": "FX:AUDUSD",  "d": "AUD to USD"},
              {"s": "FX:USDCAD",  "d": "USD to CAD"}
            ],
            "originalTitle": "Forex"
          },
          {
            "title": "Futures",
            "symbols": [
              {"s": "BMFBOVESPA:ISP1!", "d": "S&P 500 Index Futures"},
              {"s": "BMFBOVESPA:EUR1!", "d": "Euro Futures"},
              {"s": "PYTH:WTI3!",       "d": "WTI CRUDE OIL"},
              {"s": "BMFBOVESPA:ETH1!", "d": "Hydrous ethanol"},
              {"s": "BMFBOVESPA:CCM1!", "d": "Corn"}
            ],
            "originalTitle": "Futures"
          },
          {
            "title": "Bonds",
            "symbols": [
              {"s": "EUREX:FGBL1!", "d": "Euro Bund"},
              {"s": "EUREX:FBTP1!", "d": "Euro BTP"},
              {"s": "EUREX:FGBM1!", "d": "Euro BOBL"}
            ],
            "originalTitle": "Bonds"
          }
        ]
      }
      </script>
    </div>
    <!-- TradingView Widget END -->
    """,
    height=800,
)

# ──────────────────────────────────────────────────────────────────────────────
# HOTLISTS (unchanged)
# ──────────────────────────────────────────────────────────────────────────────
components.html(
    """
    <!-- TradingView Widget BEGIN -->
    <div class="tradingview-widget-container">
      <div class="tradingview-widget-container__widget"></div>
      <script
        type="text/javascript"
        src="https://s3.tradingview.com/external-embedding/embed-widget-hotlists.js"
        async
      >
      {
        "colorTheme": "dark",
        "dateRange": "12M",
        "exchange": "US",
        "showChart": true,
        "locale": "en",
        "largeChartUrl": "",
        "isTransparent": true,
        "showSymbolLogo": false,
        "showFloatingTooltip": false,
        "height": "800",
        "plotLineColorGrowing": "rgba(41, 98, 255, 1)",
        "plotLineColorFalling": "rgba(41, 98, 255, 1)",
        "gridLineColor": "rgba(42, 46, 57, 0)",
        "scaleFontColor": "rgba(219, 219, 219, 1)",
        "belowLineFillColorGrowing": "rgba(41, 98, 255, 0.12)",
        "belowLineFillColorFalling": "rgba(41, 98, 255, 0.12)",
        "belowLineFillColorGrowingBottom": "rgba(41, 98, 255, 0)",
        "belowLineFillColorFallingBottom": "rgba(41, 98, 255, 0)",
        "symbolActiveColor": "rgba(41, 98, 255, 0.12)"
      }
      </script>
    </div>
    <!-- TradingView Widget END -->
    """,
    height=800,
)

# ──────────────────────────────────────────────────────────────────────────────
# ETF HEATMAP
# ──────────────────────────────────────────────────────────────────────────────
st.title("Stock heatmap")
components.html(
    """
    <!-- TradingView Widget BEGIN -->
    <div class="tradingview-widget-container">
      <div class="tradingview-widget-container__widget"></div>
      <script
        type="text/javascript"
        src="https://s3.tradingview.com/external-embedding/embed-widget-stock-heatmap.js"
        async
      >
      {
        "exchanges": [],
        "dataSource": "SPX500",
        "grouping": "sector",
        "blockSize": "market_cap_basic",
        "blockColor": "change",
        "locale": "en",
        "symbolUrl": "",
        "colorTheme": "dark",
        "hasTopBar": false,
        "isDataSetEnabled": false,
        "isZoomEnabled": true,
        "hasSymbolTooltip": true,
        "isMonoSize": false,
        "width": "100%",
        "height": "800"
      }
      </script>
    </div>
    <!-- TradingView Widget END -->
    """,
    height=800,
)

# ──────────────────────────────────────────────────────────────────────────────
# ETF HEATMAP (duplicate heading—move or rename if needed)
# ──────────────────────────────────────────────────────────────────────────────
st.title("ETF heatmap")
components.html(
    """
    <!-- TradingView Widget BEGIN -->
    <div class="tradingview-widget-container">
      <div class="tradingview-widget-container__widget"></div>
      <script
        type="text/javascript"
        src="https://s3.tradingview.com/external-embedding/embed-widget-etf-heatmap.js"
        async
      >
      {
        "dataSource": "AllUSEtf",
        "blockSize": "aum",
        "blockColor": "change",
        "grouping": "asset_class",
        "locale": "en",
        "symbolUrl": "",
        "colorTheme": "dark",
        "hasTopBar": false,
        "isDataSetEnabled": false,
        "isZoomEnabled": true,
        "hasSymbolTooltip": true,
        "isMonoSize": false,
        "width": "100%",
        "height": "800"
      }
      </script>
    </div>
    <!-- TradingView Widget END -->
    """,
    height=800,
)
