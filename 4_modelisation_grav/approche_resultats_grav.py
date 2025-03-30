import streamlit as st
from streamlit_utils import css_code, write_text, banner

banner("machine_learning")

st.markdown(css_code, unsafe_allow_html=True)

st.title("Modélisation de la gravité")

help_msg = """
La mesure dite de **recall**, adaptée aux classes déséquilibrées, mesure la capacité du modèle à identifier les vrais positifs.\n
Elle est définie par la formule suivante : VP / ( VP + FN )
\n
Plus la valeur est proche de 1, plus le nombre de faux négatifs est faible, et le nombre de vrai positif est élevé.\n
**Vrai positif (VP) :**
\n Définition : Le modèle a correctement prédit la valeur comme appartenant à la classe positive.
\n Cas exemple 1 : Le modèle prédit qu'un patient est malade, et le patient est effectivement malade.
\n Cas exemple 2 : Le modèle prédit qu’une victime est blessée grave, décédée sur le coup ou dans les 30 jours, est c’est effectivement le cas.
 
\n
**Faux positif (FP) :**
\n Définition : Le modèle a incorrectement prédit la valeur comme appartenant à la classe positive, alors que l'exemple appartient à la classe négative (par exemple, "non malade" dans le cas d'un diagnostic médical).
\n Cas exemple 1 : Le modèle prédit qu'un patient est malade, mais le patient est en réalité sain
\n Cas exemple 2 : Le modèle prédit qu’une victime est blessée grave, décédée sur le coup ou dans les 30 jours, mais la victime est en fait indemne ou blessée léger.

\n
**Faux négatif (FN) :**
\n Définition : Le modèle a incorrectement prédit la valeur comme appartenant à la classe négative, alors que la valeur appartient à la classe positive.
\n Cas exemple 1 : Le modèle prédit qu'un patient n'est pas malade, alors que le patient est effectivement malade.
\n Cas exemple 2 : Le modèle prédit qu’une victime est en fait indemne ou blessée léger alors qu’elle est blessée grave, décédée sur le coup ou dans les 30 jours

\n
**Vrai négatif (VN) :**
\n Définition : Le modèle a correctement prédit une valeur comme appartenant à la classe négative.
\n Cas exemple 1 : Le : Le modèle prédit qu'un patient n'est pas malade, et le patient est effectivement en bonne santé.
\n Cas exemple 2 :  Le modèle prédit qu’une victime est en fait indemne ou blessée léger, ce qui est effectivement le cas.
"""

st.header("Approche et métrique utilisées", help=help_msg)

text = """
Par rapport à notre cas d’usage métier, nous souhaitons prédire le mieux possible les vrais positifs et réduire le plus possible les faux négatifs de la classe 1 qui nécessitent des soins d’urgence et adaptés en milieu hospitalier.
Dans ce cas, la métrique la plus appropriée pour évaluer les performances du modèle de classification de l’objectif métier est le recall :
\n - Elle est adaptée à notre cas de classes déséquilibrées
\n - L’objectif est d’avoir une valeur de recall la plus proche de 1 avec un nombre de faux négatifs le plus faible possible et un nombre de vrais positifs le plus élevé possible.

Dans la suite, nous allons optimiser et comparer les performances de nos modèles par rapport à la métrique du recall dans les algorithmes pour un recall le plus proche de 1 possible, sans négliger la valeur du f1-score.
Nous regarderons également l’effort de computing, qui représente un coût par rapport à l’hébergement (AWS ou autre).
"""
st.markdown(text)


text = """
Pour comparer les modèles, nous allons utiliser l’approche représentée par le schéma ci-dessous :
"""
write_text(text)

image_path = "img/image068.png" 
st.image(image_path, width=1400)

st.header("Résultats")

st.subheader("LazyClassifieur")

text = """
Lazy Predict est un excellent point de départ pour identifier rapidement le modèle le plus approprié. Dans notre cas, il a permis d’évaluer 25 modèles de classification, et de retenir le TOP des 4 meilleurs modèles les plus performants :
BalancedRandomForestClassifier, XGBoost, LGBMClassifier, AdaBoostClassifier, BaggingClassifier
"""
st.write(text)

st.subheader("Baseline")

text = """
Nous avons utilisé un pipeline pour chacun des modèles, et une boucle sur un dictionnaire de modèles pour évaluer les performances avec les paramètres par défaut pour obtenir une baseline. Cette baseline servira de référence pour comparer avant et après le tuning des hyperparamètres, et avec et sans resampling. Nous avons obtenu les résultats suivants :
Le modèle BalancedRandomForestClassiifer donne des résultats tout à fait corrects pour la métrique du recall 1. Les résultats des autres modèles sont médiocres. 
Le modèle BaggingClassifier a dû être enlevé de la prochaine étape en raison de temps de calcul très important, supérieur à 3h.
"""
st.write(text)

image_path = "img/image070.png" 
st.image(image_path, width=600)

st.subheader("Tuning des Hyperparamètres")


text = """
GridSearchCV conduisant à des temps de calcul très élevés (supérieur à 5h pour le 1er modèle), nous avons préféré RandomizedSearchCV. En perspective, il serait intéressant d’utiliser des serveurs avec de la GPU et un grand nombre de processeur pour paralléliser et réduire le temps calcul associé, trop important et de réduire
les crashs et surchauffe des ordinateurs personnels, inadaptés pour ce type de calcul.
Comme pour la baseline, nous avons codé avec des pipelines et une boucle sur un dictionnaire de modèles avec des grilles de paramètres. 
Une boucle sur les clef/valeur de ce dictionnaire, avec resampling (SMOTE, UpperSampling) ou sans resampling , nous permet de réduire considérablement le nombre de Notebooks de 12 à 1.
"""
st.write(text)

st.subheader("Entraînement et évaluation finale des modèles optimisés")


text = """
Les résultats sont très bons sur l’ensemble des données de training. Mais selon l’analyse exploratoire des données où nous avons constaté qu’il y avait peu de features pertinentes, nous nous attendons à une difficulté du modèle à généraliser avec des résultats inférieurs sur l’ensemble de données de tests.
Nous avons ajouté des mesures des écarts relatifs entre les performances des datasets de training et de test. Cela constitue un indicateur pour le surapprentissage (overfitting) et sera un des éléments de décision pour nous aider à choisir le meilleur modèle.
En définitif, nous choisissons le modèle LGBMClassifier_1 sans resampling pour les raisons suivantes : 
\n - Il représente un meilleur équilibre entre le recall de 0.84 et le f1-score de 0.80
\n - Il minimise l’écart relatif de performance, proche de 0% entre le test et le training (i.e sans overfitting) \n
Par rapport à la baseline, le gain est important d’un facteur proche de 2  (0.84/0.44) après le tuning des hyperparamètres qui a porté ses fruits. 
Le paramètre pertinent était le scale_pos_weight calculé à partir du taux de déséquilibre des classes de la variable cible.
"""
st.write(text)

image_path = "img/evaluation_finale_ML.png" 
st.image(image_path, width=1000)

text = """
L’ajout de données complémentaires (taux d’alcoolémie, usage de stupéfiant, vitesse du véhicule, …) plus pertinentes permettrait certainement d’améliorer les performances des modèles. 
On pourrait également envisager de remplacer partiellement la saisie manuelle des données, source d’erreur que nous avons constaté lors du nettoyage des données par des mécanismes de remontée automatique des données comme la latitude et la longitude.
"""

st.write(text)


st.subheader("Interprétabilité : Features importances et SHAP")

text = """
L’interprétabilité des modèles de machine learning, dont particulièrement les modèles complexes que nous utilisons, 
est importante pour expliquer les valeurs prédites par les modèles. Les features importantes du modèle définitif choisi sont représentées ci-dessous :
"""
st.write(text)

image_path = "img/image082.jpg" 
st.image(image_path, width=1000)

text = """
Pour le modèle LGMClassifier_1 sans le resampling, l’utilisation de la librairie SHAP nous donne les résultats ci-dessous.
Nous retrouvons dans le graphique ci-dessus les principales features qui agissent de façon positive sur la prédiction comme la sécurité (secu1) et l’agglomération (agg), l’heure (hour), l’âge, la latitude et la longitude (lat et long).
Suites aux échanges avec notre mentor, les différences de résultats entre les deux méthodes proviennent des algorithmes qui ne sont pas les mêmes. 
Nous constatons aussi que la prédiction est influencée de manière positive par la somme des 69 autres features, ce qui est cohérent avec l’analyse des données par rapport au test de V-Cramer où les valeurs de dépendances par rapport à la variable cible sont faibles. 
"""
st.write(text)

image_path = "img/image083.jpg" 
st.image(image_path, width=800)

