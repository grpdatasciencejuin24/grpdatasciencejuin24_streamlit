import streamlit as st
from streamlit_utils import css_code, write_text, banner


banner("data_analyse")

st.markdown(css_code, unsafe_allow_html=True)

st.title("Analyse et exploration des données")

st.header("Description des données")
text = "Les données du site Kaggle étant issues du site de data.gouv.fr, et ne couvrant pas les années de 2017 à 2023, nous avons fait le choix d'utiliser comme source, les données publiques de data.gouv.fr"
st.write(text)
text = "Les données sur la qualification des blessés hospitalisés depuis l’année 2018 ne peuvent être comparées aux années précédentes suite à des modifications de process de saisie des forces de l’ordre », " \
       "nous avons fait le choix de n’utiliser pour notre projet que les fichiers associés aux années de 2019 à 2023"
st.write(text) 
text = "Le modèle de données est représenté par le schéma relationnel ci-dessous, obtenu par reverse engineering, avec l'ajout du dataframe consolidé des accidents au centre de la figure :"
st.write(text)
image_path = "img/data-model.png" 
st.image(image_path, width=800) 
text = "Nous avons ajouté un dataframe de dictionnaire de données pour indiquer pour chaque variable du dataframe consolidé des accidents, le fichier BAAC associé,"\
       "son type : continue ou catégorielle et sa description."
write_text(text)