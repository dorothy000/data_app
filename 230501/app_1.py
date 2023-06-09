import streamlit as st

st.title('This is a title')
st.header('This is a header')
st.subheader('Thif is a subheader')

st.text("Hello World. Streamlit text")
name = 'Jooyeon Kim'
st.text('Hi, {}'.format(name))

st.markdown('## This is markdown')

st.success('성공적으로 저장하였습니다.')
st.warning('업로드할 수 없는 파일 형식입니다.')
st.info('알려드립니다.')
st.error('This is an error')
st.exception('This is an exception')

#super funtion
st.write('Normal Text')
st.write('## This is a markdown text')
st.write(1+2)
st.write(dir(st))

#help info
st.help(range)