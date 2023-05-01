import streamlit as st
st.header('display json')
st.json([{"data":"name"}])
# JavaScript Object Notation은 Javascript 객체 문법으로 구조화된 데이터를 표현하기 위한 문자 기반의 표준 포맷
# json에서는 큰따옴표 사용 권장

st.header('display code')
st.code('''
def sayHello():
    print('Hello streamlit')
''',language='python')