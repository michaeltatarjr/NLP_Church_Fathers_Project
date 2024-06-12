import streamlit as st
import pickle
import pandas as pd
import numpy as np
import altair as alt
from urllib.error import URLError

st.set_page_config(page_title="Comparing Cosine Similarities", page_icon="📊")

st.markdown("# Doc2Vec and Cosine Similarity")
st.sidebar.header("Cosine Similarities")
st.write(
    """Using different techniques for document embeddings and analysis can be helpful in looking for overall patterns in the text. It can also be used to look at differences between individual books, as well as groups of books. We do that here, using gensims Doc2Vec, and sckit-learns Cosine Similarity. 
    
Use the drop down menu to pick a book, or a group of books to compare to the entire corpus."""
)

@st.cache_data
def get_UN_data():
    with open('../pngs/sim_matrix2.DataFrame', 'rb') as file:
        LOCAL_URL = pickle.load(file)
        df = LOCAL_URL
        return df.set_index("names")

try:
    df = get_UN_data()
    books = st.multiselect(
        "Choose a book!", list(df.index), ["Old Testament", "New Testament"]
    )
    if not books:
        st.error("Please select at least one book!")
    else:
        data = df.loc[books]
        st.write("### Similarity Comparison", data.sort_index())


except URLError as e:
    st.error(
        """
        **You broke it!**
        """
        % e.reason
    )