import streamlit as st
from streamlit_utils import css_code, write_text, banner


banner("data_analyse")

st.markdown(css_code, unsafe_allow_html=True)

st.title("Exploration et data visualisation")

st.header("Rapport d’informations globales sur les variables")

text = """
Nous avons généré un rapport détaillé sur chacune des variables pour l’exploration des données. Ce rapport permet de nous renseigner 
sur les variables administratives, les valeurs nulles (nan) avec un fort pourcentage, candidates à la suppression, et la variable cible « grav » avec les modalités.
"""
st.write(text)

image_path = "img/rapport_variables.png" 
st.image(image_path, width=1200)


st.header("Data visualisation")

text = """
Dans cette partie, nous donnerons quelques exemples de data visualisation utilisées pour l'exploration et la compréhension des données. 
"""
st.write(text)


st.subheader("Variable cible 'grav'")

text = """
Le graphique ci-dessous représente les proportions de la classe de la variable cible de la gravité 'grav' et nous montrent des modalités déséquilibrées (imbalanced), 
avec une part très faible pour la modalité « 4-Tués » par rapport aux autres classes.   
"""
st.write(text)

image_path = "img/grav.png" 
st.image(image_path, width=400)


st.subheader("Variable heure")

text = """
On peut constater à partir de la figure ci-dessous que les accidents sont majoritairement situés vers 9h du matin et vers 17h pour toutes les classes de gravités.
"""

image_path = "img/image031.png" 
st.image(image_path, width=800)


st.subheader("Valeurs nulles")

text = """
Les heatmaps des valeurs manquantes des 4 dataframes : vehicules, usages, lieux et caracteristiques nous permettent de visaliser les variables candidates à la suppression.
Au vu de l’analyse graphique, la variable « occ_utc » contenant un grand nombre de valeurs nulles pourra être supprimée.
"""
st.write(text)

image_path = "img/image027.jpg" 
st.image(image_path, width=700)

st.subheader("Visualisation des corrélations")

text = """
La génération d’une clustermap ci—dessous, avec la méthode de spearman, nous permet d’observer des corrélations entre certaines variables à étudier plus en détail lors de l’étape de pré-processing et de features engineering 
comme Place et catu, Agg et catr, atm et surf
"""
st.write(text)

image_path = "img/image040.jpg" 
st.image(image_path, width=700)

st.header("Evolution temporelle du nombre total d’accidents")
text = """
Nous avons représenté ci-dessous l’évolution du nombre total d’accidents regroupé par jour pour les années de début 2019 à fin 2023, pour toutes les gravités confondues.
La couleur rouge désigne les périodes de confinement du COVID-19 qui représentent un biais pour notre étude.
On peut constater des minimas supérieurs aux autres périodes pour les périodes ci-dessous, impliquant par une diminution du trafic routier et par voie de conséquences, du nombre d’accidents : 
\n - du 2020-03-17 au 2020-05-11
\n - du 2020-10-30 au 2020-12-14
\n - du 2021-04-03 au 2021-05-02
\n
Nous avons utilisé la librairie pandasql avec une requête SQL pour effectuer l’agrégation des données journalières. 
"""
st.write(text)

image_path = "img/image089.png" 
st.image(image_path, width=800)


st.header("Interactive map view")
text = """
Nous avons implémenté une « map view » interactive à partir du module folium (6).
Celle-ci affiche la géolocalisation des accidents avec leur gravité. 
Les cercles de couleurs vertes, bleues, rouges et noires, correspondent respectivement aux gravités des accidents indemnes, blessés légers, blessés hospitalisés et tués par accident routier.
"""
st.write(text)

image_path = "img/image019.png" 
st.image(image_path, width=800)

st.info("L’analyse exploratoire des données nous a permis de constater un déséquilibre globale des classes de chacune des variables en fonction de la gravité et la sous-représentation de certaines classes", icon="ℹ️")
