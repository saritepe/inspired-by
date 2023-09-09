import requests
import streamlit as st

@st.cache_resource
def get_quotes():
    url = "https://zenquotes.io/api/quotes/"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    inspires = response.json()

    print(len(inspires))

    return inspires

quotes = get_quotes()

if "default" not in st.session_state:
    st.session_state["default"] = quotes.pop()["q"]

my_area = st.write(st.session_state["default"])

if st.button("Update default example"):
    st.session_state["default"] = quotes.pop()["q"]
    print(len(quotes))
    st.experimental_rerun()
