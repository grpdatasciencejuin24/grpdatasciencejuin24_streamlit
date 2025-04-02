import streamlit as st
from streamlit_utils import css_code, write_text, banner

banner("neural_network")

st.markdown(css_code, unsafe_allow_html=True)

st.title("Modélisation du nombre d'accidents")


def tab_approche():

    st.header("Approche")

    text = """
    LSTM (Long Short-Term Memory) est une méthode de Deep learning très efficace pour traiter les séries temporelles. Nous souhaitons la mettre à profit pour concevoir un modèle, l’évaluer, et sous réserve de performances acceptables, l’utiliser pour prédire le nombre d’accidents annuels.
    Les modèles de mémoire à long terme LTSM sont un type d'architecture de réseau neuronal récurrent (RNN). Ils ont récemment acquis une importance significative dans le domaine du Deep Learning.
    \n
    Contrairement aux réseaux de neurones classiques (comme les perceptrons multicouches), un RNN a une structure de boucle qui permet aux informations de circuler non seulement d'un neurone à un autre, mais aussi à travers les étapes du temps. Chaque sortie d'une cellule de RNN à un moment donné devient l'entrée pour le même neurone à l'instant suivant, ce qui permet au réseau de garder une mémoire des événements passés.

     
    """
    write_text(text)


    text = """
    LSTM repose sur trois portes principales : la porte d'entrée (input gate), la porte d'oubli (forget gate) et la porte de sortie (output gate). 
    Le schéma ci-dessous représente le mécanisme complexe mis en ouvre dans ce modèle:  on utilisera le LSTM comme une boîte noire.
    """

    st.info(text, icon="ℹ️")

    image_path = "img/image086.png" 
    st.image(image_path, width=500)


    text = """
    Pour évaluer les performances du modèle, nous allons utiliser des métriques spécifiques aux séries temporelles en évaluant la qualité de la précision avec le Mean Absolute Percentage Error (MAPE) et le Symmetric Mean Absolute Percentage Error (sMAPE).
    Plus ces valeurs sont faibles (proche de 0), meilleure est la prédiction.
    """
    st.write(text)

    text = """
    Pour comparer les différents paramètres, nous allons utiliser l’approche représentée par le schéma ci-dessous :
    """
    write_text(text)

    image_path = "img/image087.png" 
    st.image(image_path, width=1200)

    return

def tab_resultats():

    st.header("Résultats")

    st.subheader("Baseline")

    text = """
    Nous observons une convergence de la fonction de perte (Loss) vers 0, aussi bien sur l’ensemble d’entraînement que sur l’ensemble de test, avec les paramètres ci-dessous (voir graphique).
    Une erreur tendant vers 0 sur l’ensemble d’entraînement indique que le modèle apprend efficacement et que la précision augmente durant l’apprentissage. De même, une erreur proche de 0 sur l’ensemble de test suggère que le modèle généralise bien sur des données nouvelles qu’il n’a jamais vues, sans signe d’overfitting, ce qui est très encourageant.
    """

    st.write(text)

    image_path = "img/image091.png" 
    st.image(image_path, width=600)

    text = """
    Nous obtenons les valeurs suivantes d'évaluation des métriques, très satisfaisantes sur les ensembles de training et de test :
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
    On obtient comme meilleurs paramètres principaux un nombre de couches de 2, un taux de dropout de 0.3 et une activation par la fonction tanh. 
    Avec cette optimisation, on observe une convergence de la fonction Loss vers 0, équivalente entre l’ensemble de validation et d’entrainement.
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
    Cela répond pleinement à notre objectif, et le modèle est largement suffisant pour prédire le nombre annuel d’accidents, où la prédiction des pics n’est pas déterminante.
    """

    st.info(text, icon="ℹ️")

    return

tab1, tab2 = st.tabs(
        ["Approche", "Résultats"]
    )

with tab1:
        tab_approche()

with tab2:
        tab_resultats()
