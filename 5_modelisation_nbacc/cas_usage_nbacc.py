import streamlit as st
from streamlit_utils import css_code,write_text, banner, map_view

banner("accident")

st.markdown(css_code, unsafe_allow_html=True)

st.title("Modélisation du nombre d'accidents")
st.header("Cas d'usage métier et objectifs")

text = """
La prévision du nombre total des accidents permettrait de demander, de justifier et de mettre en place les moyens nécessaires (optimiser l’affectation et la mobilisation des forces de l’ordre sur l’ensemble du territoire, développer des campagnes de sensibilisation et de dissuasion *, …) pour répondre aux directives de la CEE.
L’image ci-dessous représente un exemple de mobilisation des forces de l’ordre en terme humain (gendarmes sur le terrain) et matériel (véhicules de gendarmerie).
Dans un contexte de réduction des dépenses, la prédiction du volume annuel d’accidents rentrerait dans le cadre de la préparation du budget et de son optimisation argumentée.
\n
*lutte contre la consommation d’alcool et de stupéfiants, utilisation du téléphone portable au volant, limitation de vitesse, contrôle de vitesse, contrôle du taux d’alcoolémie, …
\n 
Nos objectifs sont de concevoir un modèle de type « times-series » en utilisant le Deep-Learning LSTM, évaluer sa performance et de prédire l’évolution du nombre d’accidents en fonction du temps
"""

write_text(text)

image_path = "img/cas_usage_2.jpg" 
st.image(image_path, width=400)

st.info("Pour rappel, la CEE a pour objectif de diminuer de moitié le nombre de morts et de blessés graves sur les routes pour 2030, et à le réduire à zéro ou presque à l'horizon 2050, et la France doit s’aligner sur ces objectifs.", icon="ℹ️")