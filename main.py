import streamlit as st

st.title("Weather Forecast API")

place = st.text_input("Place :")

day = st.slider("Forecaste ",min_value=1,max_value=5,help="Select the number of forecast days")

option = st.selectbox("select data to views",("temperature","sky"))

st.subheader(f"{option} for the next {day} days of {place}")

