import streamlit as st
from streamlit_utils import css_code, write_text, banner


banner("accident")

st.markdown(css_code, unsafe_allow_html=True)


def tab_conclusion():

    st.title("Conclusion et perspectives")

    st.header("Conclusion")
    text = "Les deux approches de Machine Learning pour la gravité des accidents et de Deep Learning LSTM pour la prévision du nombre d’accidents, ont donné des résultats globalement satisfaisants :"\
            "\n- Modèle de classification de la gravité Machine Learning : Nous avons obtenu un recall (classe 1) d’environ 88%, un f1-score proche de 76% et une capacité convaincante"\
                "à identifier les cas de blessés graves et de décès (classe 1). Du point de vue opérationnel,"\
            "cela permet d’optimiser le nombre de vrais positifs et de réduire de manière significative le risque de faux négatifs, ce qui est crucial pour les interventions d'urgence."\
            " Toutefois, cette approche engendre aussi un nombre plus élevé de faux positifs, ce qui implique des ressources supplémentaires dans certains cas, bien que le risque humain justifie souvent de "\
            "sur-prévoir ces interventions."\
            "\n- Modèle Deep Learning LSTM : Une erreur MAPE oscillant entre 11 et 12% pour la prévision du nombre d’accidents, ce qui demeure tout à fait acceptable pour des projections à court et moyen terme."\
            " Ce niveau d'erreur permettrait de mieux affiner la planification budgétaire et la répartition des effectifs sur le terrain, avec l'objectif de réduire l’insécurité routière."
    st.markdown(text)
    text = "Les limites et points de vigilance métiers sont listés ci-dessous :"\
        "\n- Qualité et exhaustivité des données : Les jeux de données ne contiennent pas toujours des informations essentielles (vitesse des véhicules, utilisation du téléphone, alcoolémie, etc.)."\
        "Par ailleurs, une sous-déclaration ou des publications avec une fréquence annuelle dans la mise à disposition des données peuvent nuire à la fiabilité des modèles."\
        "\n- Évolution des comportements et de la réglementation : Les changements dans les politiques de sécurité routière, les évolutions technologiques (véhicules autonomes, systèmes d’aide à la conduite)"\
            " ou les modifications de la réglementation (limitations de vitesse) peuvent rendre les modèles obsolètes s'ils ne sont pas régulièrement réentraînés avec des données actualisées."\
                " Il conviendrait de voir s’il est possible d’obtenir ces données de façon plus fluide avec la publication d’un webservice, sans attendre la publication du rapport annuel. "\
        "\n- Infrastructure matérielle adaptée et équipe dédiée : Au vu des limitations constatées sur nos ordinateurs (temps de calcul élevé, plantages répétés provoqués par la surchauffe du CPU), " \
        "le déploiement de modèles dans un cadre institutionnel nécessite une infrastructure adaptée (GPU)  avec une équipe dédiée (analyste, data engineer, data scientiste) " \
        "capable de superviser l'apprentissage et d’interpréter les prédictions générées en étroite collaboration avec les métiers."\
        "\n- Mesurer l’impact sur le terrain : au-delà de la performance métrique, bien qu'un fort recall dans la prédiction des blessés graves constitue un atout sanitaire, "\
        "un trop grand nombre d’interventions pour des cas moins graves peut engendrer un effet de fausses alertes, entraînant une surcharge d’appels et une mobilisation excessive de moyens."\
            " Il est donc primordial d’assurer une concertation étroite avec les acteurs de terrain (personnel hospitalier, services de secours, forces de l’ordre) pour ajuster l’utilisation du modèle en " \
            "fonction des réalités opérationnelles."
    st.markdown(text)

    st.header("Perspectives")
    text = "Nous proposons comme perspectives, pour valoriser davantage les résultats, de :"\
                "\n- Prototyper une application métier : Une application mobile ou un système embarqué pourrait transmettre automatiquement des informations essentielles (coordonnées GPS, nombre d’occupants, heure de l’accident, etc.) aux secours. Les prédictions issues du modèle ML aideraient à prioriser les interventions en fonction de la gravité de l'accident."\
                "\n- Sensibiliser et former les acteurs : Il est important de diffuser les résultats du modèle de manière pédagogique pour que les intervenants comprennent à la fois les avantages et les limitations du système (fausses alertes liées aux faux positifs, …)."\
                "\n- Poursuivre le travail en explorant d’autres modèles (GRU, WaveNet, DeepAR) pour la prévision des séries temporelles et enrichir les données d'entrée (type de véhicule, conditions météo, état de la route, etc.) afin d'améliorer la performance des prédictions."
    st.markdown(text)




def tab_ANNEXE():

    st.title("ANNEXE")

    st.header("Modélisation multi-classes")

    text = """
    Nous définissons la multi-classe de la variable cible comme suit :
    \n - Classe 0 : Elle représente les victimes indemnes (valeur 0 de la variable cible ‘grav’ de notre dataset nettoyé)
    \n - Classe 1 : Elle représente les blessés légers (valeur 1 de la variable cible ‘grav’ de notre dataset nettoyé)
    \n - Classe 2 : Elle regroupe les victimes d’accidents graves (valeurs 2 et 3 de la variable cible ‘grav’ de notre dataset nettoyé)
    \n
    Nous obtenons les résultats ci-dessous avec les paramètres par défaut comme baseline en multi-classe :
    """

    st.markdown(text)

    image_path = "img/image104.png" 
    st.image(image_path, width=600)

    text = """
    Par rapport aux résultats obtenus en classe binaire rappelés ci-dessous, 
    nous observons que la classification multi-classe diminue les performances pour le recall en raison du déséquilibre des classes très marqué. 
    Conformément à notre cas d’usage métier de prédiction de la gravité, nous avons fait le choix de ne conserver que la classe binaire pour concentrer nos efforts et obtenir les meilleurs résultats avec la plus grande valeur métier.
    """

    write_text(text)

    image_path = "img/image105.png" 
    st.image(image_path, width=600)


    st.header("Matrice de confusion")

    text = """
    La matrice de confusion du modèle LGMClassifier sans resampling est donnée ci-dessous :
    """
    write_text(text)


    image_path = "img/Matrice_confusion.png" 
    st.image(image_path, width=500)



tab1, tab2 = st.tabs(
        ["Conclusion et perspectives", "ANNEXE"]
    )

with tab1:
        tab_conclusion()

with tab2:
        tab_ANNEXE()



