import streamlit as st
from streamlit_utils import css_code, write_text, banner

banner()

st.markdown(css_code, unsafe_allow_html=True)

st.title("Modélisation du nombre d'accidents")

st.header("Approche utilisée")

text = """
LSTM (Long Short-Term Memory) est une méthode de Deep learning très efficace pour traiter les séries temporelles. Nous souhaitons la mettre à profit pour concevoir un modèle, l’évaluer, et sous réserve de performances acceptables, l’utiliser pour prédire le nombre d’accidents annuels.
Les modèles de mémoire à long terme LTSM (11), (12) sont un type d'architecture de réseau neuronal récurrent (RNN)*. Ils ont récemment acquis une importance significative dans le domaine du Deep Learning.

* Structure des RNN : Contrairement aux réseaux de neurones classiques (comme les perceptrons multicouches), un RNN a une structure de boucle qui permet aux informations de circuler non seulement d'un neurone à un autre, mais aussi à travers les étapes du temps. Chaque sortie d'une cellule de RNN à un moment donné devient l'entrée pour le même neurone à l'instant suivant, ce qui permet au réseau de garder une mémoire des événements passés.

LSTM repose sur trois portes principales : la porte d'entrée (input gate), la porte d'oubli (forget gate) et la porte de sortie (output gate).  
"""
write_text(text)

image_path = "img/image086.png" 
st.image(image_path, width=500)


text = """
Pour comparer les modèles, nous allons utiliser l’approche représentée par le schéma ci-dessous :
"""
write_text(text)

image_path = "img/image087.png" 
st.image(image_path, width=1000)


st.header("Résultats")

st.subheader("Baseline")

text = """
Nous obtenons une convergence de la fonction de perte (Loss) vers 0 sur l’ensemble de training comme sur l’ensemble de test avec les paramètres ci-dessous. Cf graphique ci-dessous.
L’erreur qui tend vers 0 sur l'ensemble de training montre la capacité du modèle à apprendre avec une augmentation de la précision pour l’apprentissage.
L’erreur qui tend vers 0 sur l'ensemble de test montre la capacité du modèle à généraliser sur des données nouvelles, qu'il ne connaît pas, c’est-à-dire sans overfitting, ce qui est très encourageant.
"""
st.write(text)

image_path = "img/image091.png" 
st.image(image_path, width=600)


st.subheader("Métriques utilisées")

text = """
Pour évaluer les performances du modèle pour la baseline, nous allons utiliser des métriques spécifiques aux séries temporelles en évaluant la qualité de la précision avec le Mean Absolute Percentage Error (MAPE) et le Symmetric Mean Absolute Percentage Error (sMAPE).
lus ces valeurs sont faibles (proche de 0), meilleure est la prédiction.
Nous obtenons les valeurs suivantes qui sont très satisfaisantes sur les ensembles de training et de test :
\n - MAPE sur l’ensemble de training: 14.12%
\n - sMAPE sur l’ensemble de training : 13.42%
\n - MAPE sur l’ensemble de test : 12.67%
\n - sMAPE sur l’ensemble de test : 12.22%
"""
st.write(text)

image_path = "img/image094.jpg" 
st.image(image_path, width=1000)

st.subheader("Tuning des Hyperparamètres et performances finales")

text = """
Nous avons utilisé le dictionnaire ci-dessous de paramètres pour effectuer le tuning des hyperparamètres :
"""
st.write(text)


image_path = "img/image095.png" 
st.image(image_path, width=1000)

text = """
Après tuning, la convergence de la fonction Loss est un peu moins rapide, mais tout de même très satisfaisante.  
Nous obtenons les valeurs suivantes qui sont très satisfaisantes sur les ensembles de training et de test, avec une légère amélioration :
\n - MAPE sur l’ensemble de training : 13.19%
\n - sMAPE sur l’ensemble de training : 12.47%
\n - MAPE sur l’ensemble de test : 11.90%
\n - sMAPE sur l’ensemble de test : 11.53%
\n
Les prédictions effectuées sur les ensembles de training et de test sont légèrement améliorées, avec des valeurs pour les pics plus élevés mais toujours plus faibles que les valeurs réelles.
"""
st.write(text)


image_path = "img/image096.png" 
st.image(image_path, width=600)

text = """
Le tuning permet d'obtenir des prédictions légèrement améliorées, avec des valeurs pour les pics plus élevés mais toujours plus faibles que les valeurs réelles.
"""
st.write(text)


image_path = "img/image097.jpg" 
st.image(image_path, width=1000)


text = """
L’écart relatif entre le nombre d’accidents prédit par le modèle et le nombre d’accidents réels sur l’année 2023 est très faible, de 0.6 %, ce qui est excellent. 
Cela répond pleinement à notre objectif, et le modèle est largement suffisant pour prédire le nombre d’accidents moyens annuels, où la prédiction des pics n’est pas déterminante.
"""
st.write(text)


