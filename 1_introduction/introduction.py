import streamlit as st
from streamlit_utils import css_code,write_text, banner, set_bg_hack
import time

banner("accident")

st.markdown(css_code, unsafe_allow_html=True)

st.title("Introduction")

#st.info('This is a purely informational message', icon="ℹ️")
#st.warning('This is a warning', icon="⚠️")

def tab_contexte_enjeux():

    container1 = st.container(border=True)
    container1.header("Contexte et enjeux")
    text = """Un accident de la route est une collision non intentionnelle, qui a lieu sur le réseau routier entre un engin roulant (automobile, camion, moto, vélo, …) 
        et tout autre véhicule, personne ou animal, se déplaçant ou non, engendrant au moins des dégâts matériels, voire des traumatismes ou le décès d'une ou plusieurs personnes impliquées.
        Les enjeux sont donnés ci-après, suivants les Ministères :
\n
1.	Pour le Ministère de la santé, 
 
L’enjeux est de connaître au plus tôt si les victimes d’ accidents sont blessées graves pour optimiser la prise en charge (transport de la victime, 1er soins, …), la qualité et le délai du traitement pour mettre tout en œuvre pour les sauver. 
\n
2.	Pour le Ministère de l’intérieur,
 
L’enjeux est de prédire le nombre total des accidents pour justifier et mettre en place les moyens nécessaires (optimiser l’affectation et la mobilisation des forces de l’ordre sur l’ensemble du territoire, développer des campagnes de sensibilisation et de dissuasion *, …) pour répondre aux directives de la CEE.
Les cas d’usages métiers sont détaillés dans les parties de modélisation.


\n
*lutte contre la consommation d’alcool et de stupéfiants, utilisation du téléphone portable au volant, limitation de vitesse, contrôle de vitesse, contrôle du taux d’alcoolémie, …
"""

    container1.write(text)


def tab_methodologie_planning():

    st.header("Méthodologie et planning projet")

    container1 = st.container(border=True)
    text = """
    Nous avons découpé notre projet de datascience en 4 phases principales.  
    Pour chacunes des phases, nous utilisons une méthodologie agile incrémentale et itérative avec une démarche d'amélioration continue.
    """

    container1.write(text)

    #video_file = open("img/Animation1.mp4", "rb")
    #video_bytes = video_file.read()

    #container1.video(video_bytes,loop=True, autoplay=True)

    image_path = "img/Phases.png" 
    container1.image(image_path, width=1400) 

    return


tab1, tab2 = st.tabs(
        ["Contexte et enjeux", "Méthodologie et planning projet"]
    )

with tab1:
        tab_contexte_enjeux()

with tab2:
        tab_methodologie_planning()
