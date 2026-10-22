
import streamlit as st

st.title("Addition of Two Numbers")

a = st.number_input("Enter First Number")
b = st.number_input("Enter Second Number")

if st.button("Add"):
    result = a + b
    st.success("Addition = " + str(result))


