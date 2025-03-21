import requests, os
import pandas as pd
import streamlit as st

backend_base_api_url = os.getenv("BACKEND_HOST", "http://localhost:8000")

def get_models():
    return requests.get(
        url=f"{backend_base_api_url}/models"
    ).json()


def get_data(model_id):
    return requests.get(
        url=f"{backend_base_api_url}/models/%s/data"%(model_id)
    ).json()

models = get_models()
model_names = [m['name'] for m in models]

st.title("Model Results")

model_name = st.selectbox("Model Name", options=model_names)
model = list(filter(lambda x: x['name'] == model_name, models))[0]

if model['status'] != 'SUCCESS':
    st.write('PROCESSING')
else:
    data = get_data(model_id=model['id'])
    df = pd.DataFrame.from_records(data)
    st.line_chart(df)
