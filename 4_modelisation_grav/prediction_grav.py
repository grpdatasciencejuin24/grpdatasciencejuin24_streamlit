import streamlit as st
from streamlit_utils import css_code,write_text, banner, map_view, set_bg_hack
from model_lgbm import predict_grav

banner("machine_learning")

def prediction_app(lat, long, age, hour, place, sexe, secu1, catv, obs, obsm, choc, lum, agg, int, atm, col, catr, plan, situ, isweekend, saison, holidays):

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


    st.info("Les paramètres (des plus pertinents semon l'analyse des features importances)", icon="ℹ️")
        # Features les plus(+) importantes
        # lat long age hour secu1 agg obsm col sexe catr obs int choc catv place

    # lat, long, age, obs        
    col_lat, col_long, col_age, col_obs, col_obsm, col_choc, col_catr = st.columns([1, 1, 1, 1, 1, 1, 1])

    with col_lat:
        lat = st.number_input("latitude", value = lat, step=1e-6, format="%.5f")
    with col_long:
        long = st.number_input("longitude", value = long, step=1e-6, format="%.5f")

    with col_age:
        age =  st.number_input("âge",
                                step=1,
                                min_value=0,
                                max_value=100,
                                value=age)


    
    # obs
    with col_obs:
        sel_obs = st.selectbox(
                "obstacle fixe",
                [
                    "sans obstacle heurté",
                    "avec un obstacle heurté"
                ]
            )

    match sel_obs:
        case "sans obstacle heurté":
            obs = 0
        case "avec un obstacle heurté":
            obs = 1

    with col_catr:
        sel_catr = st.selectbox(
                "Catégorie de route",
                [
                    "autoroute",
                    "route nationale",
                    "route départementale",
                    "voie communale",
                    "hors réseau public",
                    "parc de stationnement ouvert à la circulation publique",
                    "routes de métropole urbaine",
                    "autre"
                ]
            )

    match sel_catr:
        case "autoroute":
            catr = 1
        case "route nationale":
            catr = 2
        case "route départementale":
            catr = 3
        case "voie communale":
            catr = 4
        case "hors réseau public":
            catr = 5
        case "parc de stationnement ouvert à la circulation publique":
            catr = 6
        case "routes de métropole urbaine":
            catr = 7
        case "autre":
            catr = 8


   # obsm
    with col_obsm:
        sel_obsm = st.selectbox(
                "obstacle mobile",
                [
                    "sans obstacle heurté",
                    "piéton",
                    "véhicule",
                    "autre"
                ]
            )

    match sel_obsm:
        case "sans obstacle heurté":
            obsm = 0
        case "piéton":
            obsm = 1 
        case "véhicule":
            obsm = 2
        case "autre":
            obsm = 3  

    # choc
    with col_choc:
        sel_choc = st.selectbox(
                "Point de choc initial",
                [
                    "aucun",
                    "avant",
                    "avant droit",
                    "avant gauche",
                    "arrière",
                    "arrière droit",
                    "arrière gauche",
                    "côté droit",
                    "côté gauche",
                    "choc multiples (tonneaux)"
                ]
            )

    match sel_obsm:
        case "sans obstacle heurté":
            obsm = 0
        case "piéton":
            obsm = 1 
        case "véhicule":
            obsm = 2
        case "autre":
            obsm = 3  



    col_hour, col_minute, col_place, col_sexe, col_int = st.columns([1, 1, 1, 1, 1])

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

    # place sexe
    with col_sexe:
        sel_sexe = st.selectbox(
                "sexe",
                [
                    "femme",
                    "homme"
                    
                ]
            )

    match sel_sexe:
        case "homme":
            sexe = 0
        case "femme":
            sexe = 1


    with col_int:
        sel_int = st.selectbox(
                "intersection",
                [
                    "sans intersection",
                    "avec intersection"                                        
                ]
            )

    match sel_int:
        case "sans intersection":
            int = 0
        case "avec intersection":
            int = 1

    with col_place:
        sel_place = st.selectbox(
                "place",
                [
                    "conducteur",
                    "passager avant",
                    "passager arrière",
                    "piéton"
                ]
            )

    match sel_place:
        case "conducteur":
            place = 0
        case "piéton":
            place = 1
        case "passager avant":
            place = 2
        case "passager arrière":
            place = 3
        
    #secu1 agg obsm col catv
    col_secu1, col_agg, col_obsm, col_col, col_catv = st.columns([1, 1, 1, 1, 1])

    with col_secu1:
        sel_secu1 = st.selectbox(
                "équipement de sécurité",
                [
                    "Casque","Ceinture", "Dispositif enfant","Gilet réfléchissant","Airbag","Gant","Aucun","Autre"
                ]
            )

    match sel_secu1:
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


    with col_catv:
        sel_catv = st.selectbox(
                "catégorie de véhicule",
                [
                    "2 roues motorisées (moto, scotter, ...)", "voiture","camion","bus","vélo, trotinette", "autres"
                ]
            )

    match sel_catv:
        case "voiture": 
              catv = 0
        case "2 roues motorisées (moto, scotter, ...)": 
              catv = 1
        case "camion":
              # camion
              catv = 2
        case "bus":
              # Bus
              catv = 3
        case "vélo, trotinette":
              # vélo, trotinette 
              catv = 4
        case "autres":
              # autres
              catv = 5

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
                    "véhicule","pas d'obstacle mobile", "piéton", "autre"
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
                    "Collision sans véhicules", "Collision entre un ou plusieurs véhicules"
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
    with st.expander("Autres paramètres (moins pertinents selon l'analyse des features importances)", icon="ℹ️", expanded=False):
        col_lum, col_atm, col_plan, col_situ, col_week_end, col_saison, col_holidays = st.columns([1, 1, 1, 1, 1, 1, 1])

    with col_lum:
        sel_lum = st.selectbox(
            "luminosité", 
                [
                "en plein jour", 
                "autre (nuit, crépuscule, ...)"
                ],            
                )
    
    match sel_lum:
        case "en plein jour":
            lum = 0
        case "autre (nuit, crépuscule, ...)":
            lum = 1

    with col_atm:
        sel_atm = st.selectbox(
                    "Cond. atmosphériques",
                    [
                        "pluie, neige, ..."
                        "normal",
                        
                    ],
                )

    match sel_atm:
        case "normal":
            atm = 0
        case "pluie, neige, ...":
            atm = 1

    with col_plan:
        sel_plan = st.selectbox(
                    "Tracé en plan",
                    [
                        "en courbe à gauche",
                        "en courbe à droite",
                        "partie rectiligne",
                        "en S"
                    ],
                )

    match sel_plan:
        case "partie rectiligne":
            plan = 0
        case "en courbe à gauche":
            plan = 1
        case "en courbe à droite":
            plan = 2
        case "en S":
            plan = 3


    with col_situ:
        sel_situ = st.selectbox(
                    "situation de l'accident",
                    [
                        "sur chaussée",
                        "sur bande d'arrêt d'urgence",
                        "sur accotement",
                        "sur trottoir",
                        "sur piste cyclable",
                        "sur autre voie spéciale",
                        "aucun",
                        "autre"
                    ],
                )

    match sel_situ:
        case "aucun":
            situ = 0
        case "sur chaussée":
            situ = 1
        case "sur bande d'arrêt d'urgence":
            situ = 2
        case "sur accotement":
            situ = 3
        case "sur trottoir":
            situ = 4
        case "sur piste cyclable":
            situ = 5
        case "sur autre voie spéciale":
            situ = 6
        case "autre":
            situ = 7


    with col_week_end:
                sel_week_end = st.selectbox(
                    "Période de la semaine",
                    [
                        "du lundi au vendredi",
                        "du samedi au dimanche"
                    ],
                )


    match sel_week_end:
        case "du lundi au vendredi":
            isweekend = 0
        case "du samedi au dimanche":
            isweekend = 1

    with col_saison:
        sel_saison = st.selectbox(
                    "Saison",
                    [
                         "hiver",
                         "autonne",
                         "été",
                         "printemps",
                    ],
                )

    match sel_saison:
        case "printemps":
            saison = 0
        case "été":
            saison = 1
        case "autonne":
            saison = 2
        case "hiver":
            saison = 3

    with col_holidays:
        sel_holidays = st.selectbox(
                    "Vacances estivales",
                    [
                        "hors vacances d'été",
                        "pendant les vacances d'été"
                    ],
                )

    match sel_holidays:
        case "hors vacances d'été":
            holidays = 0
        case "pendant les vacances d'été":
            holidays = 1


    # for debugging only !!!
    # VKO 25/03/2025
    #st.write(lat, long, age, hour, place, sexe, secu1, catv, obs, obsm, choc, lum, agg, int, atm, col, catr, plan, situ, isweekend, saison, holidays)

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

st.markdown(css_code, unsafe_allow_html=True)

st.title("Modélisation de la gravité")
st.header("Prédiction")
    
# Valeurs par défaut
lat = 43.067428	
long = 1.639618
age = 20
hour = 12
secu1 = 1
agg = 0
obsm = 2
col = 1
sexe = 1
catr = 1
obs = 0
int = 0
choc = 5
catv = 1
place = 0
lum = 0
atm = 1
plan = 1
situ = 1
isweekend = 0 
saison = 3
holidays = 0

# for debugging only !!!
#st.write(lat, long, age, hour, place, sexe, secu1, catv, obs, obsm, choc, lum, agg, int, atm, col, catr, plan, situ, isweekend, saison, holidays)

pred = predict_grav(lat, long, age, hour, place, sexe, secu1, catv, obs, obsm, choc, lum, agg, int, atm, col, catr, plan, situ, isweekend, saison, holidays)

# for debugging only !!
# st.write(pred)

prediction_app(lat, long, age, hour, place, sexe, secu1, catv, obs, obsm, choc, lum, agg, int, atm, col, catr, plan, situ, isweekend, saison, holidays)
