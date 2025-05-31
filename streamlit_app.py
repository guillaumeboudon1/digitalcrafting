import streamlit as st

st.set_page_config(
    page_title="My Dashboard",
    page_icon="📈",
)

def main():
    with st.sidebar:
        st.page_link('streamlit_app.py', label='Individual Checker', icon='🔥')
        st.page_link('pages/competition.py', label='Competition Checker', icon='🛡️')

st.title("My Dashboard")    



if __name__ == '__main__':
    main()
