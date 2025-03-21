import requests, os
import pandas as pd
import streamlit as st

backend_base_api_url = os.getenv("BACKEND_HOST", "http://localhost:8000")


def create_model(name):
    r = requests.post(
        url=f"{backend_base_api_url}/models/",
        json={
            "name": name
        }
    )

    return r.json()


def get_models():
    return requests.get(
        url=f"{backend_base_api_url}/models"
    ).json()



st.title('Build and Train AI Models')

with st.form("model_form", clear_on_submit=True, enter_to_submit=False):
    name = st.text_input("Model Name")

    submitted = st.form_submit_button(
        label="Train Model"
    )

    if submitted:
        create_model(name=name)


models = get_models()

if models:
    df = pd.DataFrame.from_records(models)
    st.table(data=df.set_index('id'))

