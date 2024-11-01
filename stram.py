import streamlit as st
import pandas as pd
import numpy as np
import datetime


st.title("Hello, Streamlit!")
st.write("This is my first streamlit app.")
#button
if st.button('Click me'):
    st.write("#RutoMustGo")

#radio
st.text("use of radio")
status=st.radio("Which country are you from?",("Kenya","kinangop"))
if status == "kinangop":
    st.write("You are from kinangop")
else:
    st.write("You are from kenya")
#Slider

slider_value=st.slider("Select a value: ",min_value=0,max_value=100,value=50)
st.write(f"Selected Value is {slider_value}")

checkbox_value = st.checkbox("Show content")
if checkbox_value:
    st.write("Content displayed.")

st.write("Displaying an image:")
st.image("images\img1.png", caption="come over", use_column_width=True,width=30)
if st.button(label='Click me!'):
    st.write("nmechoka")
st.markdown("### This is a markdown")
st.success("Successful")
st.info("Information")
st.warning("Warning")
st.error("Error")
    
