import streamlit as st

col1, col2,col3 = st.columns(3)
col1.metric("Temperature",'70 ℉',"1.2 ℉")
col2.metric('Wind', '9mph','-8%')
col3.metric('Humidity','86%','4%')
