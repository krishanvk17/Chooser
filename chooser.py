import streamlit as st
import random
st.write("Hello! this is chooser, your go-to website to make difficult choices you cant make yourself!")

num=st.slider("Choose how many options you have.",1,10)
choice=random.randint(1,num)

st.write("Think or write out which option each number is.")
if st.button:
  st.write("I choose...",choice,"!")
  st.info("Refresh your screen to try again!")
