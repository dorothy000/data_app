import streamlit as st
st.header('display json')
st.json([{'data':'name'}])

st.header('display code')
st.code('''
def sayHello():
    print('Hello streamlit')
''',language='python')