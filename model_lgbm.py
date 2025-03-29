import streamlit as st

import lightgbm as lgbm
from lightgbm import LGBMClassifier
import pandas as pd 

import joblib

@st.cache_resource
def predict_grav(lat, long, age, hour, 
                 place, sexe, secu1, catv, obs, obsm, choc, lum, agg, int, atm, col, catr, plan, situ, isweekend, saison, holidays):
    pipeline = joblib.load('model/pipeline_lightgbm_1.joblib')

    numerical_cols = ['lat', 'long', 'age', 'hour']
    categorical_cols = ['place', 'sexe', 'secu1', 'catv', 'obs', 'obsm', 'choc', 'lum', 'agg', 'int', 'atm', 'col', 'catr', 'plan', 'situ', 'isweekend', 'saison', 'holidays']

    cols = numerical_cols + categorical_cols

    X_test = pd.DataFrame(columns=cols)

    for col in numerical_cols:
        X_test[col] = X_test[col].astype({col:'float'})

    for col in categorical_cols:
        X_test[col] = X_test[col].astype({col:'int64'})

    X_test.info()

    X_test.loc[0,"lat"] = lat
    X_test.loc[0,"long"] = long
    X_test.loc[0,"age"] = age
    X_test.loc[0,"hour"] = hour

    X_test.loc[0,"place"] = place
    X_test.loc[0,"sexe"] = sexe
    X_test.loc[0,"secu1"] = secu1
    X_test.loc[0,"catv"] = catv
    X_test.loc[0,"obs"] = obs
    X_test.loc[0,"obsm"] = obsm
    X_test.loc[0,"choc"] = choc
    X_test.loc[0,"lum"] = lum
    X_test.loc[0,"agg"] = agg
    X_test.loc[0,"int"] = int
    X_test.loc[0,"atm"] = atm
    X_test.loc[0,"col"] = col
    X_test.loc[0,"catr"] = catr
    X_test.loc[0,"plan"] = plan
    X_test.loc[0,"situ"] = situ
    X_test.loc[0,"isweekend"] = isweekend
    X_test.loc[0,"saison"] = saison
    X_test.loc[0,"holidays"] = holidays


    y_pred = pipeline.predict(X_test)
    pred = y_pred[0]
  
    lat = X_test.loc[0,"lat"]
    long = X_test.loc[0,"long"]

    return pred


