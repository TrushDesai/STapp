import streamlit as st
from openai import OpenAI
import os

api_key = os.getenv("OPENAI_API_KEY")  # Used in production
client = OpenAI(api_key=api_key)

st.title('🎯 AI Google Review Response Assistant for restaurants 🍽️')
st.markdown('I was made to help you craft 5 variations of SEO friendly google review response')

def analyze_text(text):
    if not api_key:
        st.error("OpenAI API key is not set. Please set it in your environment variables.")
        return
    
    client = OpenAI(api_key=api_key)
    model = "gpt-3.5-turbo"

      # Instructions for the AI (adjust if needed)
    messages = [
        {"role": "system", "content": "You are an assistant who helps craft SEO friendly google review responses and end with line to invite them again also start with thanking them for adding a review and finish with follow us on instagram and link."},
        {"role": "user", "content": f"Please help me generate 5 different review responses for :\n{text}"}
    ]

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0  # Lower temperature for less random responses
    )
    return response.choices[0].message.content



# Cell 4: Streamlit UI 
user_input = st.text_area("Enter a Google review:", "It was an amazing experience, very yummy food we will return again ")

if st.button('Generate responses'):
    with st.spinner('Generating Text...'):
        post_text = analyze_text(user_input)
        st.write(post_text)

   
