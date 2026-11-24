import streamlit as st
st.write("this is from getinfo.py")
if "name" not in st.session_state or len(st.session_state.name) == 0:
    st.session_state.name = st.text_input("Enter your name")

