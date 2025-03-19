import streamlit as st
from model_lstm import predict
from streamlit_utils import css_code,write_text, banner, map_view



banner()

st.markdown(css_code, unsafe_allow_html=True)

st.title("Modélisation du nombre d'accidents")
st.header("Prédiction")

n_days = st.select_slider("Choisissez le nombre de jours pour la prédiction du nombre journalier d'accidents",
                                    options = [120, 150, 180, 360])

result = st.button("Predict")
if result:
    #st.write("Nombre de jours de prédiction:",n_days)
    predict(n_days)