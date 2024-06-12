import streamlit as st
import pickle
from PIL import Image
import numpy as np
import matplotlib
matplotlib.use('Agg')  # or 'Qt5Agg'
import matplotlib.pyplot as plt
import matplotlib.cm
from matplotlib.colors import Normalize
import seaborn as sns
from scipy.cluster.hierarchy import linkage, dendrogram
from scipy.spatial.distance import pdist, squareform
from pathlib import Path

st.set_page_config(page_title="Exploring Text Preparation with Jaccard Similarity", page_icon="📈")

st.markdown("# Exploring Text Preparation")
st.sidebar.header("The Tokenization")

path = Path(__file__).parent.parent

#download sets
with open(path /'./pngs/mergings1.set', 'rb') as file:
    mergings1 = pickle.load(file)
with open(path /'./pngs/mergings2.set', 'rb') as file:
    mergings2 = pickle.load(file)
with open(path /'./pngs/mergings3.set', 'rb') as file:
    mergings3 = pickle.load(file)
with open(path /'./pngs/mergings4.set', 'rb') as file:
    mergings4 = pickle.load(file)

with open(path /'./pngs/complete_corpus_sentence_tokenized_names.set', 'rb') as file:
    complete_corpus_sentence_tokenized_names = pickle.load(file)

st.write(
    """Within natural language processing, there's always a need to process text in some way. Included here is a comparison of 4 common text processing decisions, using a Jaccard Similarity and displayed as a dendrogram.
    
A **Jaccard Similarity** is a statistic used for gauging the similarity and diversity of sample sets. It measures the similarity between finite sample sets and is defined as the size of the intersection divided by the size of the union of the sample sets. 
    
A **dendrogram** is a tree-like diagram that illustrates the arrangement of clusters formed by hierarchical clustering. It's commonly used to visualize the relationships between objects or samples in a dataset based on their similarity or dissimilarity.
    """
    
    
)
st.write(
    """The first method involves tokenizing the text at the sentence level. This means each sentence is considered as a single token, and we compute the Jaccard Similarity between sentences."""
)
# Create the 1st plot. needs the fig
fig1 = plt.figure(figsize = (12,9))
dendrogram(mergings1,
           labels=list(complete_corpus_sentence_tokenized_names),
           leaf_rotation=90,
           leaf_font_size=9)
plt.title('Tokenization at the sentence Level')
plt.tight_layout()

# Display the plot. needs the st
st.pyplot(fig1)


st.write(
    """Here, we tokenized at the word level using the popular nltk library. This makes the individual word as the token."""
)

# Create the 2nd plot. needs the fig
fig2 = plt.figure(figsize = (12,9))
dendrogram(mergings2,
           labels=list(complete_corpus_sentence_tokenized_names),
           leaf_rotation=90,
           leaf_font_size=9)
plt.title('Tokenization at the word Level using nltk')
plt.tight_layout()

# Display the plot. needs the st
st.pyplot(fig2)



st.write(
    """Next, we tokenized at the word level using gensims simple_preprocess. This tokenization wraps several methodologies into a single application."""
)

# Create the 3rd plot. needs the fig
fig3 = plt.figure(figsize = (12,9))
dendrogram(mergings3,
           labels=list(complete_corpus_sentence_tokenized_names),
           leaf_rotation=90,
           leaf_font_size=9)
plt.title('Tokenization at the word Level using gensim')
plt.tight_layout()

# Display the plot. needs the st.
st.pyplot(fig3)



st.write(
    """Then we tokenized at the word level using gensim as well as removing stop words. Common stop words include "the," "is," "in," "at," "of," "a," and "to." """
)

# Create the 3rd plot. needs the fig
fig4 = plt.figure(figsize = (12,9))
dendrogram(mergings4,
           labels=list(complete_corpus_sentence_tokenized_names),
           leaf_rotation=90,
           leaf_font_size=9)
plt.title('Tokenization using gensim, w/ stop words removed')
plt.tight_layout()

# Display the plot. needs the st
st.pyplot(fig4)