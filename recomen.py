import streamlit as st
import pandas as pd
name=st.text_input('enter your name')
fathername=st.text_input('enter your father name')
adr=st.text_area("enter your text")
classdata=st.selectbox('enter your class:',(1,2,3,4))

