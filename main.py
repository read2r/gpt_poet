from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
import streamlit as st
from dotenv import load_dotenv

load_dotenv()
chat_model = ChatOpenAI()

st.title("GPT Poet")
poem_topic = st.text_input("Your poem's topic")

if st.button("Write Poem"):
    if len(poem_topic) == 0:
        st.write("No Topic")
    else:
        with st.spinner("Now writing poem..."):
            result = chat_model.predict(f"Writing poem about {poem_topic}")
            st.write(result)