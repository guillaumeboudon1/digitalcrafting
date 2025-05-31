import streamlit as st

st.set_page_config(
    page_title="My Dashboard",
    page_icon="📈",
)

from modules.nav import Navbar


def main():
    Navbar()

    st.title(f'🛡️ Competition Checker')


if __name__ == '__main__':
    main()

st.title("My Dashboard")     
