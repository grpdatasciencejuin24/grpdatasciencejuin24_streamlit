import streamlit as st
from streamlit_utils import css_code, write_text, banner


banner()

st.markdown(css_code, unsafe_allow_html=True)

st.title("Pre-processing et features engineering")

st.header("Synthèse des résultats")

image_path = "img/pre-processing-2.png" 
st.image(image_path, width=1000)

st.write("Les actions réalisées ont permis d'effectuer :")
text = "- L'intégration automatique des 20 fichiers BACC (années 2019 à 2023) dans un dataframe consolidé avec 619971 lignes concaténées"\
           "\n- 58 variables, incluant l'ajout de la région et de la zone géographique"\
           "\n- La suppression des variables avec un nombre important de valeurs nulles (supérieur à 50%) soit un nombre de variables réduites à 23, des lignes en doublons (164), des valeurs manquantes,"\
           "des valeurs aberrantes (âge>100 ans, coordonnées GPS situées hors des limites du département, ...)"\
           "\n- L'ajout des limites des départements"\
           "\n- La transformation avec encodage des variables avec regroupement de modalités (zone géographique, …) et binarisation pour fournir à l'entrainement des modèles des valeurs numériques simplifiées"\
           "\n- La réduction potentielle du nombre de variables de 58 à 15 avec comme features communes les variables : lat, long, hour, age, secu, sexe, place, catv, agg (agglémoration)"\
           "\n- La détermination du nombre optimal du taux de données à 40% (à noter qu'un taux de 10 pourcents donne déjà de bons résultats et est utilisable pour la mise au point des Notebooks) pour optimiser le temps de calcul"
             
st.markdown(text)


text = "Nous obtenons au final un dataset constitué de 518885 lignes avec 16% du jeu de données initial supprimés sans changement significatif sur la répartition de la variable cible."
write_text(text)
