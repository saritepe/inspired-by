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

if st.button("Get Inspired"):
    quote_dict = quotes.pop()
    author = quote_dict["a"]
    quote = quote_dict["q"]
    print(len(quotes))
    st.subheader(quote)
    st.caption(author)

    if(len(quotes)) == 0 : 
        get_quotes.clear()
