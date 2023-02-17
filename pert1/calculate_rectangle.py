import streamlit as st

st.title = "Calculate Area of Rectangle"
length = st.number_input("Input Length", 0)
width = st.number_input("Input Width", 0)

if calculate := st.button("Calculate"):
    area = length * width
    # st.write("Area of Rectangle is", area)
    st.success(f"Area of Rectangle is {area}")