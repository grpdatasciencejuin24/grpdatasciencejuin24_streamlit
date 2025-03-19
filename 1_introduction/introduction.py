import streamlit as st
from streamlit_utils import css_code,write_text, banner

# pip install st_social_media_links

banner()

st.markdown(css_code, unsafe_allow_html=True)

st.title("Introduction")

st.header("Contexte")
text = "Un accident de la route est une collision non intentionnelle, qui a lieu sur le réseau routier entre un engin roulant (automobile, camion, moto, vélo, …) " \
    "et tout autre véhicule, personne ou animal, se déplaçant ou non, engendrant au moins des dégâts matériels, voire des traumatismes ou le décès d'une ou plusieurs personnes impliquées."
write_text(text)

image_path = "img/image005.png" 
st.image(image_path, width=800)


st.header("Les enjeux")
text = "Nous avons défini les deux cas d’usage métier ci-dessous, après avoir échangé avec des personnes travaillant dans ces domaines :"\
          "\n- Pour le Ministère de la santé, l’enjeux est de connaître au plus tôt si les victimes d’ accidents sont blessées graves pour optimiser la prise en charge (transport de la victime, 1er soins, …), la qualité et le délai du traitement pour mettre tout en œuvre pour les sauver. "\
          "\n- Pour le Ministère de l’intérieur, l’enjeux serait de prédire le nombre total des accidents pour justifier et mettre en place les moyens nécessaires (optimiser l’affectation et la mobilisation des forces de l’ordre sur l’ensemble du territoire, développer des campagnes de sensibilisation et de dissuasion *, …) pour répondre aux directives de la CEE."\
          "Les enjeux et objectifs associés sont détaillés dans la partie modélisation"
st.markdown(text)
st.header("Méthodologie et planning du projet")

text = """
Nous utilisons la méthodologie projet basée sur Prince2. Les phases principales du projet sont alignées avec les activités classiques du processus d’un projet de datascience, 
représentées par le schéma ci-dessous :
"""
write_text(text)

image_path = "img/image014.png" 
st.image(image_path, width=800)


text = """
Le planning associé est donné ci-après :
"""
write_text(text)

image_path = "img/planning.png" 
st.image(image_path, width=1000)
