import streamlit as st
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import folium
from streamlit_folium import st_folium
from folium.plugins import MarkerCluster
from folium.plugins import FastMarkerCluster
import pandas as pd
import numpy as np
import pickle


st.set_page_config(page_title="Exploring Church Fathers Birth Places")

st.markdown("# Explore their lives through maps and mapping")
st.sidebar.header("Appendix: Explore Their lives")


st.write(
    """Up to this point we've focused exclusively on the text, data, patterns, measurements, and other more mathematical measurements.  While the goals of the project was to conenct timeless wisdom to an ancient corpus, to learn and be shaped by the experience, it's important to to remember that these were real men who lived lives of courage. Many were martyred specifically for their faith.  

**The Didache**: Author Unknown, likely written in Syria

**Clement of Rome**: one of the earliest bishops of Rome, was martyred by being tied to an anchor and thrown into the sea. His martyrdom is traditionally believed to have occurred near the Crimea, on the Black Sea.

**Adrian Antoninus**: Also known as Hadrian of Nicomedia, Adrian Antoninus was a high-ranking Roman soldier who converted to Christianity and was martyred by being tortured and beheaded in Nicomedia (modern-day İzmit, Turkey).

**Tertullian**: Tertullian, a prolific early Christian author and apologist, died in Carthage around 240 AD.

**Tatian**: Tatian, an early Christian writer and apologist. Besides the address to the Greeks considered here, wrote the Diatesseron, a harmony of the four gospels, with copies still in existence from 152 AD. 

**Justin Martyr**: Justin Martyr, an early Christian apologist, was beheaded for his faith in Rome around 165 AD. He is known for his extensive writings defending Christianity against pagan and Jewish objections.

**Polycarp**: A bishop of Smyrna and a disciple of John the Apostle, was martyred by being burned at the stake and then stabbed when the fire failed to consume him. His martyrdom occurred in Smyrna (modern-day İzmir, Turkey).

**Athenagoras the Athenian**: Athenagoras of Athens, an early Christian apologist.

**Irenaeus**: Bishop of Lugdunum (modern-day Lyon, France), was a prominent early Christian theologian. Tradition holds that he was martyred during the persecution under Emperor Septimius Severus,

**Clement of Alexandria**: An early Christian theologian and teacher. He died around 215 AD, likely in Alexandria, Egypt.

**Ignatius**: A bishop of Antioch, was martyred by being thrown to wild beasts in the Colosseum in Rome around 108 AD. His letters written on the way to his execution are significant early Christian texts.
    """
)
#download data
with open('../pngs/names_locations.DataFrame', 'rb') as file:
    names_locations = pickle.load(file)

#Build and center a map
m = folium.Map(location=[37.983810, 24.927539], zoom_start=5) 

#Display folium
for loc in names_locations:
    folium.Marker(location=loc['geos'], popup=f"Book: {loc['authors']}").add_to(m)
    
st_data = st_folium(m, width=725, height=500)