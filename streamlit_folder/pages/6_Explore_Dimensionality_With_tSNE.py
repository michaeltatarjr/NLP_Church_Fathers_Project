import streamlit as st
import pickle
import pandas as pd
import numpy as np
from sklearn.manifold import TSNE
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize, regexp_tokenize
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


st.set_page_config(page_title="Exploring Dimensionality with t-SNE")

st.markdown("# Exploring Similarities using Nonlinear Dimensionality Reduction")
st.sidebar.header("tSNE")


st.write(
    """Dimensionality reduction is a technique used to reduce the number of variables under consideration. This process simplifies high-dimensional data into fewer dimensions while preserving as much of the significant structure and information as possible. t-SNE (t-Distributed Stochastic Neighbor Embedding) is a machine learning algorithm for dimensionality reduction. As applied here, t-SNE helps in reducing the complexity of textual data, allowing us to visualize and understand the relationships and clusters of similar documents in 2D and 3D space.  
    
In both cases, model is tokenized at the word level, and by term frequency–inverse document frequency.
    """
)
#download sets
with open('../pngs/embeddings_2d.ndarray', 'rb') as file:
    embeddings_2d = pickle.load(file)
with open('../pngs/embeddings_3d.ndarray', 'rb') as file:
    embeddings_3d = pickle.load(file)

with open('../pngs/labels2.set', 'rb') as file:
    labels = pickle.load(file)

    
    
#2D scatter plot
fig1 = px.scatter(
    x=embeddings_2d[:, 0], 
    y=embeddings_2d[:, 1],
    hover_name=labels,
    title='t-SNE 2D Visualization of Text Embeddings'
)

# Update traces for fig1
#fig1.update_layout()
fig1.update_traces(marker=dict(size=3), textposition='top center')

# Update layout for fig1
fig1.update_layout(
    plot_bgcolor='white',
    paper_bgcolor='white', 
    hovermode="x unified"
)

# Display the 2D plot
st.plotly_chart(fig1)




# Create the 3D scatter plot
fig2 = px.scatter_3d(
    x=embeddings_3d[:, 0], 
    y=embeddings_3d[:, 1], 
    z=embeddings_3d[:, 2],
    #text=labels,
    hover_name=labels,
    title='t-SNE 3D Visualization of Text Embeddings'
)

# Update traces for fig2
fig2.update_layout(hovermode="x")
fig2.update_traces(marker=dict(size=3), textposition='top center')

# Display the 3D plot in Streamlit
st.plotly_chart(fig2)