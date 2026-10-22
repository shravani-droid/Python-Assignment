
import streamlit as st

st.title("Celsius to Fahrenheit Converter")

celsius = st.number_input("Enter Temperature in Celsius")

if st.button("Convert"):
    fahrenheit = (celsius * 9 / 5) + 32
    st.success("Temperature in Fahrenheit = "
               + str(round(fahrenheit, 2)) + " °F")
