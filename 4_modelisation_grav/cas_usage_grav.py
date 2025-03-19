import streamlit as st
from streamlit_utils import css_code,write_text, banner, map_view

banner()

st.markdown(css_code, unsafe_allow_html=True)

st.title("Modélisation de la gravité")
st.header("Description du cas d'usage et du contexte métier")
text = "L’enjeux pour le Ministère de la santé, est de connaître au plus tôt si les victimes des accidents ne sortent pas indemnes ou blessés légers, " \
    "c'est-à-dire si elles sont blessées graves. En effet cette information sur l’état de la victime d'un accident permettrait d'optimiser la prise en charge (transport de la victime, 1er soins), " \
    "la qualité et le délai du traitement par les urgences des hôpitaux. Ceux-ci sont décisifs pour les victimes gravement blessées pour mettre tout en œuvre pour les sauver."
write_text(text)
image_path = "img/samu2.jpg" 
st.image(image_path, width=800)
text = "Dans ce contexte métier, à défaut d'une prise en charge rapide et efficace pour les victimes d'accident concernés, cela peut avoir des conséquences graves, " \
    "car les victimes pourraient ne pas recevoir les premiers soins des secours (Cf photo ci-dessus pour l’arrivée du SAMU sur les lieux de l’accident pour la prise en charge des blessés) " \
    "ou un suivi médical approprié à temps, mettant sa vie en danger."
write_text(text)

st.header("Objectifs")
text = "Par rapport à ce cas d'usage métier, nous définissons :"
write_text(text)
text = "- La classe 1 des victimes d'accidents des blessés graves et des décès sur le coup et dans les 30 jours (ce qui correspond aux valeurs 2 et 3 de la variable cible 'grav' de notre dataset nettoyé)"\
           "\n- La classe 0 des victimes indemnes et blessés légers (ce qui correspond aux valeurs 0 et 1 de la variable cible 'grav' de notre dataset nettoyé)"
st.markdown(text)
write_text("")
text = "Nos objectifs sont les suivants :"
write_text(text)
text = "- Concevoir les meilleurs modèles de classification, les comparer par rapport à leurs performances"\
           "\n- Prédire au mieux la classe 1 en maximisant le nombre de vrais positifs et en minimisant le nombre de faux négatifs"
st.markdown(text)
write_text("")
text = "Ces objectifs permettront de prioriser les moyens des urgences pour réduire les aggravations et sauver des victimes gravement blessées, " \
    "conformément aux enjeux du Ministère de la santé décrits dans le cas d’usage."
write_text(text)

st.header("Le Data Challenge WAICF")
text = "Durant l’année 2020, dans le cadre du salon de l'intelligence artificielle WAICF, Trustii.io a organisé un Data Challenge." \
    " L’objectif était de construire des modèles de machine learning pour prédire la gravité des accidents de la route." \
    "Les sources de données provenaient des sites data.gov.fr et data.gov.uk des années 2016 à 2020." \
    "Pendant 48h, 83 participants issues de plusieurs universités et écoles en France et à l'étranger, ont soumis plus de 235 models, plusieurs participants ont participé en équipe." \
    " La meilleure équipe a construit un modéle qui a eu un score de 0.6760 avec la métrique balanced_accuracy selon (5)."\
    "Même si la période des années est différente avec celle de nos données, ce résultat permet de donner un ordre de grandeur du score, et un objectif atteignable associé pour notre projet."\
    "Nous comparerons également les performances de notre modèle avec celle obtenues lors de ce Challenge."
write_text(text)

