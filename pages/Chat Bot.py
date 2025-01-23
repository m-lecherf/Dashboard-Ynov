import streamlit as st
import requests
from bs4 import BeautifulSoup

prompt = st.chat_input("Say something")
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

if prompt:
    response = requests.get('https://www.blogdumoderateur.com/?s='+prompt)
    soup = BeautifulSoup(response.text, 'html.parser')
    soup = soup.findAll('article')[0]
    img = soup.find('img')
    img = img['src']
    title = soup.find('h3')
    title = title.text
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("assistant"):
        if(len(title) == 0):
            response = "Sorry, I couldn't find anything on that topic"
        else:
            response = "![image]("+img+")" + '\n' + "#"+title
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
    