import streamlit as st
from streamlit_utils import css_code,write_text, banner, map_view
from model_lgbm import predict_grav

banner()

st.markdown(css_code, unsafe_allow_html=True)

st.title("Modélisation de la gravité")
st.header("Prédiction")
    
# Valeurs par défaut
lat = 48.89621	
long = 2.47012
age = 17
hour = 15
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

st.write(
        """ 
            Sélectionner les valeurs des paramètres.\n 
            Cliquer ensuite sur le bouton Prédiction afin d'utiliser le modèle LightGBM pré-entrainé pour obtenir la valeur prédite.
        """
    )

st.markdown(
        "<h4 style='text-align: center; color: black;'>Paramètres du modèle</h4>",
        unsafe_allow_html=True,
    )

    # Features les plus(+) importantes
    # lat long age hour secu1 agg obsm col sexe catr obs int choc catv place

    # lat, long, age, hour
    
age_moyen_conducteurs = st.slider("âge", 0, 100, 30)       
    
col_lat, col_long = st.columns([1, 1])

with col_lat:
    lat = st.number_input("latitude", value = lat, step=1e-6, format="%.5f")
with col_long:
    long = st.number_input("longitude", value = long, step=1e-6, format="%.5f")

col_hour, col_minute = st.columns([1, 1])

with col_hour:
    heure = st.number_input("Heure",
                               step=1,
                               min_value=0,
                               max_value=23,
                               value=hour)

with col_minute:
    minute = st.number_input("Minutes",
                               step=10,
                               min_value=0,
                               max_value=60,
                               value=0)


hour = heure + minute/60*100

#secu1 agg obsm col
col_secu1, col_agg, col_obsm, col_col = st.columns([1, 1, 1, 1])

with col_secu1:
    securite = st.selectbox(
            "équipement de sécurité",
            [
                "Ceinture","Casque","Dispositif enfant","Gilet réfléchissant","Airbag","Gant","Aucun","Autre"
            ]
        )

match securite:
    case "Ceinture":
        secu1 = 0
    case "Casque":
        secu1 = 1
    case "Dispositif enfant":
        secu1 = 2
    case "Gilet réfléchissant":
        secu1 = 3
    case "Airbag":
        secu1 = 4
    case "Gant":
        secu1 = 5
    case "Aucun":
        secu1 = 6
    case "Autre":
        secu1 = 7

with col_agg:
    agglomeration = st.selectbox(
            "localisation",
            [
                "agglomération",
                "hors agglomération"
            ]
        )

match agglomeration:
    case "agglomération":
        agg = 0
    case "hors agglomération":
        agg = 1

with col_obsm:
    obstacle_mobile = st.selectbox(
        "Obstacle mobile heurté",
            [
                "pas d'obstacle mobile", "piéton", "véhicule", "autre"
            ]
        )

match obstacle_mobile:
    case "pas d'obstacle mobile":
        obsm = 0
    case "piéton":
        obsm = 1
    case "véhicule":
        obsm = 2
    case "autre":
        obsm = 3


with col_col:
    type_collision = st.selectbox(
        "Type de collision",
            [
                "Collision entre un ou plusieurs véhicules", "Collision sans véhicules"
            ]
        )

match type_collision:
    case "Collision entre un ou plusieurs véhicules":
        col = 0
    case "Collision sans véhicules":
        col = 1


# Features les moins importantes selon l'interprétabilité
# lum atm plan situ isweekend saison holidays
    
# lum atm
with st.expander("Autres paramètres", expanded=False):
    col_lum, col_atm, col_plan, col_situ, col_week_end, col_saison, col_vacances = st.columns([1, 1, 1, 1, 1, 1, 1])

with col_lum:
            
    luminosite = st.selectbox(
        "luminosité", 
            [
            "en plein jour", "autre (nuit, crépuscule, ...)"
            ]            
            )
 
with col_atm:
    atmosphere = st.selectbox(
                "Cond. atmosphériques",
                [
                    "normal",
                    "autre (pluie, neige, ...)"
                ],
            )


with col_plan:
    courbure = st.selectbox(
                "Tracé en plan",
                [
                    "Partie rectiligne",
                    "En courbe à gauche",
                    "En courbe à droite",
                    "En S"
                ],
            )

with col_situ:
    situation = st.selectbox(
                "Situation de l’accident",
                [
                    "Aucun",
                    "Sur chaussée",
                    "Sur bande d’arrêt d’urgence",
                    "Sur accotement",
                    "Sur trottoir",
                    "Sur piste cyclable",
                    "Sur autre voie spéciale",
                    "Autres"
                ],
            )
          
with col_week_end:
            week_end = st.selectbox(
                "Période de la semaine",
                [
                    "du lundi au vendredi",
                    "du samedi au dimanche"
                ],
            )

with col_saison:
    saison = st.selectbox(
                "Saison",
                [
                    "printemps",
                    "été",
                    "autonne",
                    "hiver"
                ],
            )

with col_vacances:
            vacances = st.selectbox(
                "Vacances estivales",
                [
                    "hors vacances d'été",
                    "pendant les vacances d'été"
                ],
            )

#st.write(lat, long, age, hour, secu1, agg, obsm, col)


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

