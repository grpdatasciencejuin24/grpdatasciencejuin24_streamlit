import streamlit as st
import os 
import folium
from streamlit_folium import st_folium


import streamlit as st

css_code = """ 
"""

def write_text(text):
    st.write(text)

def banner():
    #with st.container(mode="fixed", position="bottom", border=True):
    st.image("img/Image1.png")
    
    
def map_view(lat,long,vcolor, popup_message):

    map_center = [lat, long]

    m = folium.Map(location=map_center, zoom_start=15)

    folium.CircleMarker(
                    location=[lat, long],
                    radius=15,
                    color=vcolor,  # Couleur en fonction de la probabilité
                    fill=True,
                    fill_color=vcolor,
                    fill_opacity=0.6,
                    popup=popup_message
                    ).add_to(m)

    st_data = st_folium(m, width=725)
