import streamlit as st

st.set_page_config(
    page_title="Start Here",
    page_icon="👋",
)

st.write("# Investigating textural similarities of Early Christian Church Fathers 0-250 AD")

st.sidebar.success("Click above to select a technique!")

st.markdown(
    """

##### Executive Summary
This project aims to explore the correlation and connections between the writings of the Early Christian Church Fathers of ancient Near Eastern antiquity and source texts. Using Natural Language Processing (NLP), various text visualizations, text analysis, NLTK libraries, and other techniques, we will investigate how the writings of the Church Fathers up to 250 AD are similar to each other and to the Old and New Testament, respectively. 

###### Motivation
The goal of this project is to align timeless wisdom with real-world, innovative methodology. The intersection of ancient texts and the world of the Mediterranean and Near East they inhabited 2000 years ago with modern data science techniques presents a unique and untested opportunity. The fascination with ancient, dusty writings from different eras and cultures drives this investigation, which leverages data science and NLP to analyze a rich historical corpus.

###### Data Questions
Our analysis will focus on:
 1. Basic EDA and corpus understanding
 2. A brief comparison of tokenization methods
 3. Looking for patterns with heatmapping
 4. Comparing documents using document vectors and cosine similiarities
 5. Dimensionality reduction using nonlinear techniques

 
###### Data Science Techniques:
 1. Python syntax and Data Science libraries such as: 
     * Pandas, Numpy, Seaborn, MatplotLib, pickle, glob 
 2. Tokenization techniques using:
     * nltk
     * gensim
     * spacy
     * stop_word and various lemmatizations
     * Jaccard Similarities
 3. Computing document similarity using:
     * Doc2Vec
     * Cosine similarity
     * Heatmaps to compare results
 4. 2D and 3D Dimensionality Reduction using:
     * tSNE

 
"""
)