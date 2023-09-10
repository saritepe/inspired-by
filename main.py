import requests
import streamlit as st
from pages.daily_quote import daily_quote
from pages.quotes import show_quotes


page_names_to_funcs = {
    "Daily": daily_quote,
    "Quotes": show_quotes
}

demo_name = st.sidebar.selectbox("Choose a demo", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()