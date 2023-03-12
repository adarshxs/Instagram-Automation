import openai
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

file1 = open("moods.txt","r")

st.set_page_config(page_title="Instagram . Automation", page_icon="🤖")

st.title("Instagram Caption Generator")
st.sidebar.header("Instructions")
st.sidebar.info(
    '''This is a web application that allows you to generate
        captions for your instagram posts! You can describe **the context of your post** and choose the **tone** 
        for the caption. The caption will be generated using the AI! 
       '''
    )
st.sidebar.info("Pro tip: Make your description specific for best results.")
st.sidebar.info("Pro tip: Use the slider to adjust the creativity of the caption.")
st.markdown(
    "This mini-app generates Instagram captions using OpenAI's GPT-3 based [Davinci model](https://beta.openai.com/docs/models/overview). You can find the code on [GitHub](https://github.com/adarshxs/Instagram-Automation) and the author on [Linkedin](https://www.linkedin.com/in/adarsh-a-s/)."
)

model_engine = "gpt-3.5-turbo"
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
                                  prompt = "Write a"+ param + "instagram caption about" + user_query + ". Also use appropriate tags and emojis.",
                                  max_tokens = 1024,
                                  n = 1,
                                  temperature = temp,
                                  
                                )
    response = completion.choices[0].text
    response=response.replace('"','')
    return response

main()


st.markdown("""---""")
col1, col2 = st.columns(2)
with col1:
    st.markdown(
        "**Do follow me on Instagram! [@adarsh.py](https://www.instagram.com/adarsh.py)**")  
    st.markdown("code: [Github](https://github.com/adarshxs/Instagram-Automation)")
