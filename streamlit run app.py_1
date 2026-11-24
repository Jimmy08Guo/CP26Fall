import streamlit as st
st.write("Above the columns")
row1 = st.columns(3)
row1[0].write("Left")
row1[1].write("Center")
row1[2].write("Right")

row2 = st.columns(2)
if row2[0].button("Exit"):
    st.write('Exiting...')
if row2[1].button("Enter"):
    st.write("Entering")
st.write("Below the columns")
