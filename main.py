import openai
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

file1 = open("moods.txt","r")

st.title("Instagram Caption Generator")
st.sidebar.header("Instructions")
st.sidebar.info(
    '''This is a web application that allows you to generate
        captions for your instagram posts! You can **the context of your post** and choose the **tone** 
        for the caption. The caption will be generated using the AI! 
       '''
    )

model_engine = "text-davinci-003"
openai.api_key = os.getenv("api_key")

def main():

    # Get user input
    user_query = st.text_input("Briefly describe your image/reel","Me holding hands with my girlfriend")
    temp = st.slider("Creativity", 0.0, 1.0, 0.5)
    param=st.selectbox("Tone", (file1.readlines()))
    st.subheader('Generated Caption :sunglasses:')

    if user_query != ":q" or user_query != "":
        # Pass the query to the ChatGPT function
        response = ChatGPT(user_query, temp, param)
        return st.code(response, language='None')
        
    
def ChatGPT(user_query, temp, param):
    # Use the OpenAI API to generate a response
    completion = openai.Completion.create(
                                  engine = model_engine,
                                  prompt = "Write a"+ param + "instagram caption about" + user_query + ". Also use appropriate tags.",
                                  max_tokens = 1024,
                                  n = 1,
                                  temperature = temp,
                                )
    response = completion.choices[0].text
    return response

main()
