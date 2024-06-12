import streamlit as st
import pickle
from PIL import Image
import numpy as np
import matplotlib
matplotlib.use('Agg')  # or maybe 'Qt5Agg'. Whats the difference?
import matplotlib.pyplot as plt
import matplotlib.cm
from matplotlib.colors import Normalize
import seaborn as sns
from pathlib import Path


st.set_page_config(page_title="Exploring Patterns in Cosine Similarities", page_icon="📊")

st.markdown("# Document Vectors and Cosine Similarity Pt.1")
st.sidebar.header("The Heatmap")
st.write(
    """Document vectors, also known as document embeddings, are numerical representations of documents in a high-dimensional space. These vectors capture the semantic meaning of documents, allowing for various natural language processing (NLP) tasks. Cosine similarity is a metric used to measure how similar two vectors are, regardless of their magnitude.  Here and in the following page, we explore patterns of the document similarity via heatmaps...
   """
)

path = Path(__file__).parent.parent


#download sets
with open(path /'./pngs/similarity_matrix.ndarray', 'rb') as file:
    similarity_matrix = pickle.load(file)
#with open('../pngs/mergings2.set', 'rb') as file:
#    mergings2 = pickle.load(file)
with open(path /'./pngs/titles.list', 'rb') as file:
    titles = pickle.load(file)

    
#heatmap
fig = plt.figure(figsize=(18,18))  # change the figsize to control the resolution
ax = fig.add_subplot(111)
ax.tick_params(axis='both', labelsize=12)
cmap = matplotlib.colormaps['viridis']  # you may use other build-in colormap or define you own colormap
# if your data is not in range[0,1], use a normalization. Here is normalized by min and max values.
norm = Normalize(vmin=np.amin(similarity_matrix), vmax=np.amax(similarity_matrix))
image = ax.imshow(similarity_matrix, cmap=cmap, norm=norm)

# Show all ticks and label them with the respective list entries
ax.set_xticks(np.arange(len(titles)), labels=titles)
ax.set_yticks(np.arange(len(titles)), labels=titles)

#rotate right by 45 degrees
plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")

plt.colorbar(image)
st.pyplot(fig, clear_figure=True)