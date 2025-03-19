import streamlit as st
from streamlit_utils import css_code, write_text, banner


banner()

st.markdown(css_code, unsafe_allow_html=True)

st.title("Pre-processing et features engineering")

st.header("Les étapes")

text = "Cette phase consiste à déterminer et traiter les données brutes non adaptées (erreurs de saisie par les forces de l’ordre, …) afin de pouvoir les utiliser lors des prochaines phases."\
           "Elle est indispensable pour éviter de corrompre et biaiser les résultats lors des phases d'entraînement des modèles."\
           "Le schéma ci-dessous représente les 4 étapes du pré-processing et les actions principales associées"
write_text(text)
write_text("")
image_path = "img/image041.png" 
st.image(image_path, width=1000)