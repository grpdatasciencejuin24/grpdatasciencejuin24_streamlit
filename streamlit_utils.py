import streamlit as st
import os 
import base64
import folium
from streamlit_folium import st_folium


import streamlit as st

css_code = """ 
"""

def write_text(text):
    st.write(text)

def banner2(val):

    match val:
        case "neural_network":
            set_bg_hack("img/neural_network.png")
        case "accident":
            set_bg_hack("img/accident.png")
        case "data_analyse":
            set_bg_hack("img/data_analyse.png")
        case "machine_learning":
            set_bg_hack("img/machine_learning.png")
        case _:
            set_bg_hack("img/accident.png")
    return
    

def banner(val):

    match val:
        case "neural_network":
            set_bg_hack("img/accident.png")
        case "accident":
            set_bg_hack("img/accident.png")
        case "data_analyse":
            set_bg_hack("img/accident.png")
        case "machine_learning":
            set_bg_hack("img/machine_learning.png")
        case _:
            set_bg_hack("img/machine_learning.png")
    return

def set_bg_hack2(main_bg):
 
    main_bg_ext = "png"

def set_bg_hack(main_bg):
 
    main_bg_ext = "png"
        
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
    

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
