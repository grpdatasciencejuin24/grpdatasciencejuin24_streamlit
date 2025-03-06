import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import FuncFormatter
from model_lstm import predict
from model_lgbm import predict_grav, map_view

import folium
from streamlit_folium import st_folium

# cd "C:\Python\Datascientest\Projet\8-Streamlit"
# streamlit run .\streamlit-app.py

st.set_page_config(layout="wide")

st.markdown(
    """
    <style>
        [data-testid=stSidebar] [data-testid=stImage]{
            text-align: center;
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 40%;
        }
    </style>
    """, unsafe_allow_html=True
)

with st.sidebar:
    "# Modélisation et prédiction des accidents routiers"
    st.image("img/logo3.jpeg")
    

def banner():
    st.image("img/Image1.png")

def page_introduction():

    banner()
    
    st.markdown(
        "<h2 style='text-align: center; color: black;'>Introduction</h2>",
        unsafe_allow_html=True,
    )

    tab1, tab2, tab3 = st.tabs(
        ["Contexte métier", "Méthodologie", "Le planning du projet et les jalons"]
    )

    with tab1:
        st.markdown(
            "<h4 style='text-align: center; color: black;'>Contexte métier</h4>",
            unsafe_allow_html=True,
        )

    with tab2:
        st.markdown(
            "<h4 style='text-align: center; color: black;'>Méthodologie</h4>",
            unsafe_allow_html=True,
        )

    with tab3:
        st.markdown(
            "<h4 style='text-align: center; color: black;'>Le planning du projet et les jalons</h4>",
            unsafe_allow_html=True,
        )


def tab_mapview():

    # Features les plus importantes
    lat = 48.89621	
    long = 2.47012
    age = 17
    hour = 15.0
    secu1 = 0
    agg = 0
    obsm = 2
    col = 1
    sexe = 1
    catr = 1
    obs = 0
    int = 0
    choc = 5
    catv = 0
    place = 2

    lum = 0
    atm = 1
    plan = 1
    situ = 1
    isweekend = 0 
    saison = 2
    holidays = 0

    pred = predict_grav(lat, long, age, hour, 
                 place, sexe, secu1, catv, obs, obsm, choc, lum, agg, int, atm, col, catr, plan, situ, isweekend, saison, holidays)

    on = st.toggle('Show map')

    if on:

        if pred == 0:
            pred_message = "le modèle prédit la classe 0"
            vcolor = f'#229954'
        else:
            pred_message = "le modèle prédit la classe 1"
            vcolor = f'#17202a'

        map_view(lat, long, vcolor, pred_message)


def page_EAD():

    banner()
    st.markdown(
        "<h2 style='text-align: center; color: black;'>Analyse exploiratoire des données</h2>",
        unsafe_allow_html=True,
    )

    tab1, tab2, tab3 = st.tabs(
        ["Modèle de données", "Répartition des classes", "Géolocalisation"]
    )

    with tab1:
        st.markdown(
            "<h4 style='text-align: center; color: black;'>Modèle de données</h4>",
            unsafe_allow_html=True,
        )

    with tab2:
        st.markdown(
            "<h4 style='text-align: center; color: black;'>Répartition des classes</h4>",
            unsafe_allow_html=True,
        )

    with tab3:
        st.markdown(
            "<h4 style='text-align: center; color: black;'>Géolocalisation</h4>",
            unsafe_allow_html=True,
        )

        tab_mapview()



def page_conclusion():

    banner()
    st.markdown(
        "<h2 style='text-align: center; color: black;'>Conclusion</h2>",
        unsafe_allow_html=True,
    )

    tab1, tab2 = st.tabs(
        ["Synthèse des résultats obtenus", "Perspectives"]
    )

    with tab1:
        st.markdown(
            "<h4 style='text-align: center; color: black;'>Synthèse des résultats obtenus</h4>",
            unsafe_allow_html=True,
        )

    with tab2:
        st.markdown(
            "<h4 style='text-align: center; color: black;'>Perspectives</h4>",
            unsafe_allow_html=True,
        )

def tab_demo_ML():
    
    lat = 48.89621	
    long = 2.47012
    age = 17
    hour = 15.0
    secu1 = 0
    agg = 0
    obsm = 2
    col = 1
    sexe = 1
    catr = 1
    obs = 0
    int = 0
    choc = 5
    catv = 0
    place = 2

    lum = 0
    atm = 1
    plan = 1
    situ = 1
    isweekend = 0 
    saison = 2
    holidays = 0


    st.markdown(
        "<h2 style='text-align: center; color: black;'>Démonstration </h2>",
        unsafe_allow_html=True,
    )

    st.write(
        """ 
            Sélectionner les valeurs des paramètres de votre accident de la route.\n 
            Cliquer ensuite sur le bouton Prédiction afin d'utiliser le modèle LightGBM pour obtenir la valeur prédite.
        """
    )

    st.markdown(
        "<h4 style='text-align: center; color: black;'>Paramètres du modèle</h4>",
        unsafe_allow_html=True,
    )

    # Features les plus importantes
    # lat long age hour secu1 agg obsm col sexe catr obs int choc catv place

    col58, col59, col60 = st.columns([1, 1, 1])

    with col58:
        
        lat = st.number_input("latitude", value = lat, step=1e-6, format="%.5f")
        long = st.number_input("longitude", value = long, step=1e-6, format="%.5f")

        #st.write(lat)
        #st.write(long)

        age_moyen_conducteurs = st.slider("âge", 0, 100, 30)

        hour = st.number_input("Heure",
                               step=1e-1,
                               format="%.2f",
                               min_value=0.00,
                               max_value=23.59,
                               value=hour)


    with col59:
        securite = st.selectbox(
            "équipement de sécurité",
            [
                "Ceinture","Casque","Dispositif enfant","Gilet réfléchissant","Airbag","Gant","Aucun","Autre"
            ]
        )
    with col60:
        agglomeration = st.selectbox(
            "localisation",
            [
                "agglomération",
                "hors agglomération"
            ]
        )
        
    # Features les moins importantes selon l'interprétabilité
    # lum atm plan situ isweekend saison holidays
    with st.expander("other parameters", expanded=False):
        col61, col62 = st.columns([1, 1])

        with col61:
            
            luminosite = st.selectbox(
                "luminosité", 
                [
                    "en plein jour", "autre (nuit, crépuscule, ...)"
                ]
            )
 
        with col62:
            atmosphere = st.selectbox(
                "Conditions atmosphériques",
                [
                    "normal",
                    "autre (pluie, neige, ...)"
                ],
            )

    
    on = st.toggle('Afficher la géolocalisation avec la valeur prédite')
    if on:   
        pred = predict_grav(lat, long, age, hour, place, sexe, secu1, catv, obs, obsm, choc, lum, agg, int, atm, col, catr, plan, situ, isweekend, saison, holidays)

        if pred == 0:
                pred_message = "le modèle prédit la classe 0"
                vcolor = f'#229954'
        else:
                pred_message = "le modèle prédit la classe 1"
                vcolor = f'#e74c3c'     
        map_view(lat, long, vcolor, pred_message) 

    result = st.button("Predict")
    if result:
        pred = predict_grav(lat, long, age, hour, place, sexe, secu1, catv, obs, obsm, choc, lum, agg, int, atm, col, catr, plan, situ, isweekend, saison, holidays)
        
        if pred == 0:
                pred_message = "le modèle prédit la classe 0"
                vcolor = f'#229954'
        else:
                pred_message = "le modèle prédit la classe 1"
                vcolor = f'#e74c3c'

        st.write(pred_message)

       

def page_model_ML():
    banner()
    st.markdown(
        "<h2 style='text-align: center; color: black;'>Modélisation de la gravité avec le Machine Learning</h2>",
        unsafe_allow_html=True,
    )

    tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(
        ["Cas d'usage métier et objectifs",
         "Approche utilisée",
         "Baseline",
         "Tuning des Hyperparamètres",
         "Entraînement et évaluation finale",
         "Interprétabilité",
         "Démonstration"]
      )

    with tab1:
        st.markdown(
            "<h4 style='text-align: center; color: black;'></h4>",
            unsafe_allow_html=True,
        )

    with tab2:
        st.markdown(
            "<h4 style='text-align: center; color: black;'></h4>",
            unsafe_allow_html=True,
        )
    
    with tab3:
        st.markdown(
            "<h4 style='text-align: center; color: black;'></h4>",
            unsafe_allow_html=True,
        )

    with tab4:
        st.markdown(
            "<h4 style='text-align: center; color: black;'></h4>",
            unsafe_allow_html=True,
        )

    with tab5:
        st.markdown(
            "<h4 style='text-align: center; color: black;'></h4>",
            unsafe_allow_html=True,
        )

    with tab6:
        st.markdown(
            "<h4 style='text-align: center; color: black;'></h4>",
            unsafe_allow_html=True,
        )

    with tab7:
        tab_demo_ML()
        



def tab_demo_LSTM():

    st.markdown(
        "<h2 style='text-align: center; color: black;'> </h2>",
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns([0.5, 0.5])
    with col1:
        n_days = st.select_slider("Choisissez le nombre de jours pour la prédiction du nombre journalier d'accidents",
                                    options = [120, 150, 180, 360])
    with col2:
        class_grav = st.selectbox(
            "Classe de la gravité",
            [
                "Toutes les classes confondues (par défaut)",
                "Indemme et bléssés légers",
                "Blessés grave et décédes dans les 30 jours"
            ]
            )


    result = st.button("Predict")
    if result:
        #st.write("Nombre de jours de prédiction:",n_days)
        predict(n_days)

def page_model_DeepLearningLSTM():
    banner()
    st.markdown(
        "<h2 style='text-align: center; color: black;'>Modélisation du nombre d'accidents avec le Deep Learning LSTM</h2>",
        unsafe_allow_html=True,
    )

    tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(
        ["Cas d'usage métier et objectifs",
         "Approche utilisée",
         "Baseline",
         "Tuning des Hyperparamètres",
         "Entraînement et évaluation finale",
         "Interprétabilité",
         "Démonstration"]
      )

    with tab1:
        st.markdown(
            "<h4 style='text-align: center; color: black;'></h4>",
            unsafe_allow_html=True,
        )

    with tab2:
        st.markdown(
            "<h4 style='text-align: center; color: black;'></h4>",
            unsafe_allow_html=True,
        )
    
    with tab3:
        st.markdown(
            "<h4 style='text-align: center; color: black;'></h4>",
            unsafe_allow_html=True,
        )

    with tab4:
        st.markdown(
            "<h4 style='text-align: center; color: black;'></h4>",
            unsafe_allow_html=True,
        )

    with tab5:
        st.markdown(
            "<h4 style='text-align: center; color: black;'></h4>",
            unsafe_allow_html=True,
        )

    with tab6:
        st.markdown(
            "<h4 style='text-align: center; color: black;'></h4>",
            unsafe_allow_html=True,
        )

    with tab7:
        tab_demo_LSTM()


#################################################################################################
# les pages
#################################################################################################
page = st.sidebar.radio(
    "",
    [
        "Introduction",
        "Analyse exploiratoire des données",
        "Modélisation de la gravité",
        "Modélisation du nombre d'accidents",
        "Conclusion",
    ],
)


match page:    
    case "Introduction":
        page_introduction()
    case "Analyse exploiratoire des données":
        page_EAD()
    case "Modélisation de la gravité":
        page_model_ML()
    case "Modélisation du nombre d'accidents":
        page_model_DeepLearningLSTM()
    case "Conclusion":
        page_conclusion()
    case _:
        print("ERROR-page value is not defined:",page)


st.divider()
st.sidebar.info(
    """ Vincent KOMIWES,
       Sidney HANIFA,           
       Farah VARSALLY,
       Simon-Pierre SILGA
       Mentor : Eliott DOUIEB
    """
)

