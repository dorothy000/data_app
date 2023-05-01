import streamlit as st

name = 'Jooyeon Kim'

if st.button('Submit', key=1):
    st.write('Name: {}'.format(name))

if st.button('Submit', key=2):
    st.write('Full Name: {}'.format(name))

st.header('Radio Button')
status = st.radio('What is your state','Active','Inactive'))

if status == 'Active':
    st.success('You are active')
if status == 'Active':
    st.success('You are active')