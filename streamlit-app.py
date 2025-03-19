import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import FuncFormatter
from model_lstm import predict
from model_lgbm import predict_grav
from streamlit_para import map_view
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
        st.markdown("""<h4 style='text-align: center; color: black;'>Contexte métier</h4>""", unsafe_allow_html=True,)
        
        st.write(
        "### 1. Prédiction de la gravité des accidents\n"
        "- Concevoir des modèles de classification pour distinguer les accidents graves des accidents légers.\n"
        "- Optimiser la prise en charge médicale en identifiant rapidement les blessés graves.\n"
        "- Comparer les performances des modèles pour maximiser le rappel (recall) et minimiser les faux négatifs.\n"
        )
        st.write(
        "### 2. Prévision du nombre d’accidents\n"
        "- Utiliser un modèle de Deep Learning (LSTM) pour prévoir le nombre total d’accidents en France.\n"
        "- Aider les autorités à mieux allouer les ressources et anticiper les périodes à risque.\n"
        "- Réduire l’incertitude et améliorer la planification des mesures de prévention.\n"
        )
        
    with tab2:
        st.markdown(
            "<h4 style='text-align: center; color: black;'>Méthodologie</h4>",
            unsafe_allow_html=True,
        )
        st.write(
        "### 1. Modélisation de la gravité des accidents avec le Machine Learning\n"
        "- Utilisation de Lazy Predict pour évaluer rapidement plusieurs modèles.\n"
        "- Sélection de 5 modèles : BalancedRandomForestClassifier, XGBoost, LGBMClassifier, AdaBoostClassifier, BaggingClassifier.\n"
        "- Optimisation via RandomizedSearchCV et parallélisation CPU.\n"
        )
        st.write(
        "### 2. Modélisation du nombre d’accidents avec le Deep Learning (LSTM)\n"
        "- Modèle Long Short-Term Memory (LSTM) entraîné sur les données de 2019-2023.\n"
        "- Utilisation du MAPE et sMAPE comme métriques.\n"
        "- Prise en compte des biais dus aux confinements COVID-19.\n"
        )
     
    with tab3:
        st.markdown(
            "<h4 style='text-align: center; color: black;'>Le planning du projet et les jalons</h4>",
            unsafe_allow_html=True,
        )
        st.image("img/planning.jpg")


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
        st.write(
        "### 1. Source des données\n"
        "- 2 sources de données : data.gouv.fr et Kaggle.\n"
        "- 4 catégories : Usagers, Véhicules, Lieux et Caractéristiques.\n"
        "- Données sur une période de 2008 à 2023.\n"
        )
        st.write(
        "### 2. Analyse des données source\n"
        "- Doublons de données entre les 2 sources.\n"
        "- Les modèles de données ont évolué avec le temps : informations supplémentaires ou gestion différente .\n"
        )
        st.write(
        "### 3. Données de travail\n"
        "- Uniquement les fichiers provenant de data.gouv.fr.\n"
        "- Uniquement sur la période de 2019 à 2023 car des données complémentaires ont été ajoutées à partir de 2019 et il n'était pas possible d'alimenter les données manquantes sur les années précédentes.\n"
        )
        st.write(
        "### 4. Analyse exploiratoire\n"
        "- Consolidation des données dans un DataFrame.\n"
        "- Etude et traitement des doublons, valeurs manquantes et des outliers.\n"
        "- Etude des répartitions des variables par de la datavisualisation.\n"
        "- Bonus : affichage des accidents sur une mapView par gravité.\n"
        )
        st.write(
        "### 5. Pre processing et Features engineering\n"
        "- Regroupement des modalités.\n"
        "- Standardisation des variables continues.\n"
        "- Etude des corrélations entre les variables : V-Cramer et HeatMap\n"
        )

    with tab2:
        st.markdown(
            "<h4 style='text-align: center; color: black;'>Répartition des classes</h4>",
            unsafe_allow_html=True,
        )
        st.write(
        "##### La variable cible contient plusieurs classes (Indemne, blessé léger, blessé hospitalisé et tué) mais afin de répondre à notre problématique nous avons fait le choix de passer la variable en binaire avec les 2 classes suivantes:\n"
        )
        st.write(
        "- Classe 0 : indemnes et blessés légers.\n"
        "- Classe 1 : Tous les autres cas (tué sur le coup et ceux qui décédent dans les 30 jours suivant l'accident).\n"
        )
        st.write(
        "- Nos analyses sur plusieurs modèles ont également montrées que les résultats étaient plus mauvais en multi-classe qu'en classe binaire. Cela a permis de nous réconforter dans notre choix.\n"
        "- La répartition de la variable cible montre une forte disparité : on se retrouve donc face à un problème de classe déséquilibrée. Un travail de resampling sera donc mis en place dans l'étude des modèles.\n"
        )
        st.image("img/classe_target.jpg")

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
    "Vincent KOMIWES, Sidney HANIFA, Farah VARSALLY, Simon-Pierre SILGA\n\n"
    "Mentor : Eliott DOUIEB"
)

