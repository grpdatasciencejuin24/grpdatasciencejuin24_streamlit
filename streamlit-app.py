# Date : 17/03/2025
# Version : 1.0
# Created by : Vincent
# Validated by : Sydney
# Directory structure
# streamlit repository/
#├── 1_introduction   
#│   ├── introduction.py
#├── 2_analyse
#│   └── description.py
#│   └── exploration.py
#├── 3_pre-processing
#│   └── etapes.py
#│   └── synthese.py
#├── 4_modelisation_gravite
#│   └── cas_usage_grav.py
#│   └── approche_resultats_grav.py
#│   └── prediction_grav.py
#├── 5_modelisation_nbacc
#│   └── cas_usage_nbacc.py
#│   └── approche_resultats_nbacc.py
#│   └── prediction_nbacc.py
#├── 6_conclusion
#│   └── conclusion.py
#└── streamlit_app.py

# pre-requsites :
# pip install seaborn matplotlib scipy folium streamlit_folium joblib lightgbm scikit-learn sqlalchemy tensorflow
# pip install streamlit
#  1. within Terminal
#    cd "C:\Python\Datascientest\Projet\8-Streamlit"
#  2. run app
#    streamlit run .\streamlit-app.py


import streamlit as st
import base64
from streamlit_utils import set_bg_hack


st.set_page_config(layout="wide")

#set_bg_hack("img/background.png")

# icon
# https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/
# https://fonts.google.com/icons?icon.set=Material+Symbols&icon.style=Rounded
# 	

introduction = st.Page("1_introduction/introduction.py", title="Contexte, enjeux et méthodologie", icon=":material/home:")

description = st.Page("2_analyse/description.py", title="Description des données", icon=":material/dashboard:")
exploration = st.Page("2_analyse/exploration.py", title="Exploration et data visualisation", icon=":material/dashboard:")

etapes = st.Page("3_pre-processing/etapes.py", title="Les étapes", icon=":material/dashboard:")
synthese = st.Page("3_pre-processing/synthese.py", title="Synthèse des résultats", icon=":material/dashboard:")

cas_usage_grav = st.Page("4_modelisation_grav/cas_usage_grav.py", title="Cas d'usage métier et objectifs", icon=":material/dashboard:")
approche_resultats_grav = st.Page("4_modelisation_grav/approche_resultats_grav.py", title="Approche et résultats", icon=":material/dashboard:")
prediction_grav = st.Page("4_modelisation_grav/prediction_grav.py", title="Prédiction", icon=":material/dashboard:")

cas_usage_nbacc = st.Page("5_modelisation_nbacc/cas_usage_nbacc.py", title="Cas d'usage métier et objectifs", icon=":material/dashboard:")
approche_resultats_nbacc = st.Page("5_modelisation_nbacc/approche_resultats_nbacc.py", title="Approche et résultats", icon=":material/dashboard:")
prediction_nbacc = st.Page("5_modelisation_nbacc/prediction_nbacc.py", title="Prédiction", icon=":material/dashboard:")


conclusion = st.Page("6_conclusion/conclusion.py", title="Conclusion et perspectives", icon=":material/dashboard:")


pg = st.navigation(
        {
            "Introduction": [introduction],
            "Analyse et exploration": [description,exploration],
            "Pre-processing et features engineering": [etapes,synthese],
            "Modélisation de la gravité": [cas_usage_grav,approche_resultats_grav,prediction_grav],
            "Modélisation du nombre d'accidents": [cas_usage_nbacc,approche_resultats_nbacc,prediction_nbacc],
            "Conclusion et perspectives": [conclusion]
        }
    )



pg.run()

st.sidebar.markdown(
    """<a href="https://fr.linkedin.com/in/vincent-komiwes-959b0832">Vincent KOMIWES <img src="data:image/png;base64,{}" width="25"></a>""".format(
        base64.b64encode(open("img/linkedin.png", "rb").read()).decode()
    ),
    unsafe_allow_html=True,
)

st.sidebar.markdown(
    """<a href="https://www.linkedin.com/in/simon-pierre-silga-3076121a?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app">Sidney HANIFA <img src="data:image/png;base64,{}" width="25"></a>""".format(
        base64.b64encode(open("img/linkedin.png", "rb").read()).decode()
    ),
    unsafe_allow_html=True,
)

st.sidebar.markdown(
    """<a href="https://www.linkedin.com/in/your-profile-username/">Simon-Pierre SILGA <img src="data:image/png;base64,{}" width="25"></a>""".format(
        base64.b64encode(open("img/linkedin.png", "rb").read()).decode()
    ),
    unsafe_allow_html=True,
)

st.sidebar.markdown(
    """<a href="https://www.linkedin.com/in/your-profile-username/">Farah VARSALLY <img src="data:image/png;base64,{}" width="25"></a>""".format(
        base64.b64encode(open("img/linkedin.png", "rb").read()).decode()
    ),
    unsafe_allow_html=True,
)

#st.sidebar.markdown(
#    """<a href="https://github.com/DataScientest-Studio/JUIN24_CDS_Accidents/"><img src="data:image/png;base64,{}" width="25"></a>""".format(
#        base64.b64encode(open("img/github.png", "rb").read()).decode()
#    ),
#    unsafe_allow_html=True,
#)