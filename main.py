import os
import streamlit as st
import pandas as pd
import numpy as np
import openai
import pyperclip

openai.api_key = os.environ.get("OPENAI_API_KEY")
model_engine = "text-davinci-003"

st.title('Fake JSON Generator')


st.header('Enter your JSON here')
text_input = st.text_area('Enter your JSON here', height=500)

prompt = "Generate sample JSON object list for the following interface. Please give me a valid json that is validated" + text_input

# Set the maximum number of tokens to generate in the response
max_tokens = 350

# Generate a response
# Dont run completion if text_input is empty
x = 0
st.header('Generated JSON')
if text_input and x != 1:
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=0.5,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # Print generated completion in a new textboxes. Add a copy to clipboard button to the textbox and define the button action and function
    if completion:
        st.text_area('Generated JSON',
                     completion.choices[0].text[2:], key='text_area', height=500)
        if st.button('Copy to clipboard'):
            pyperclip.copy(completion.choices[0].text[2:])
            st.write('Copied to clipboard!')
    x += 1
