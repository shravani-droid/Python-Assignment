
import streamlit as st

st.title("Even or Odd Number")

num = st.number_input("Enter an Integer", step=1, value=0)

if st.button("Check"):
    if num % 2 == 0:
        st.success("The number is Even")
    else:
        st.success("The number is Odd")
