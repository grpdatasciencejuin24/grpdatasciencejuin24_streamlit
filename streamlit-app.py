# Date : 17/03/2025
# Version : 1.0
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


st.set_page_config(layout="wide")

introduction = st.Page("1_introduction/introduction.py", title="Contexte, enjeux et méthodologie", icon=":material/dashboard:")

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


conclusion = st.Page("6_conclusion/conclusion.py", title="Conclusion et perspectives", icon=":material/search:")


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
    """<a href="https://www.linkedin.com/in/sidneyhanifa/">Sidney HANIFA <img src="data:image/png;base64,{}" width="25"></a>""".format(
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


st.sidebar.markdown(
    """</br></br><a href="https://github.com/grpdatasciencejuin24/DS_Accidents_June2024">Projet Github <img src="data:image/png;base64,{}" width="25"></a>""".format(
        base64.b64encode(open("img/GitHub.png", "rb").read()).decode()
    ),
    unsafe_allow_html=True,
)
