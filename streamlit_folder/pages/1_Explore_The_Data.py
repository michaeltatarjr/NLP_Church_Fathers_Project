import streamlit as st
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm
from matplotlib.colors import Normalize
import seaborn as sns
from pathlib import Path

st.set_page_config(page_title="Getting to know the corpus")

st.markdown("# Basic Exploratory Analysis")
st.sidebar.header("The Books")
st.write(
    """The corpus is made up of 43 early christian writings of various lengths. Spanning approximately 200 years, they represent a wide variety of authors, styles, and intents. These include letters of encouragement to those enduring persecution, robust defenses of the faith to the Roman Senate, eyewitness accounts of martydoms of key figures in the early church, theological works and early instructions for meeting as a young faith community. 
    
By the numbers:
    
Number of Documents: 43
    
Mean Number of Words per Document: 25591.0
    
Vocabulary Size: 44277 """
)

path = Path(__file__).parent.parent

image1 = Image.open(path /'/pngs/charactercount.png')
image2 = Image.open(path /'./pngs/timeline.png')

#with col1:
st.image(image1, caption='Character Count')
st.image(image2, caption='Approximate Timeline')

# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
