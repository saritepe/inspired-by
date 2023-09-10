import requests
import streamlit as st

@st.cache_data
def get_quote_of_day():
    url = "https://zenquotes.io/api/today/"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    inspires = response.json()

    return inspires[0]


def daily_quote():

    quote_dict = get_quote_of_day()
    print(quote_dict)

    author = quote_dict["a"]
    quote = quote_dict["q"]

    st.subheader(quote)
    st.caption(author)