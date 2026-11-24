import streamlit as st
if "name" in st.session_state:
    st.write("Hello", st.session_state.name)
else:
    st.write("Go to the other tab and enter your name")

