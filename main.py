import streamlit as st
import pandas as pd
import numpy as np
import openai
import pyperclip

openai.api_key = "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"
model_engine = "text-davinci-003"

st.title('Fake JSON Generator')
