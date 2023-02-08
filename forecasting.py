import streamlit as st
import pandas as pd
import numpy as np
from prophet import Prophet
from prophet.diagnostics import performance_metrics
from prophet.diagnostics import cross_validation
from prophet.plot import plot_cross_validation_metric
import base64  

st.title('Time Series Forecasting Using Streamlit')

uploaded_file = st.file_uploader(" ", type=['xlsx'])
if uploaded_file is not None:
    appdata = pd.read_excel(uploaded_file)  #read the data fro
    appdata['ds'] = pd.to_datetime(appdata['ds']) 
    st.write(uploaded_file) #display the data  
    max_date = appdata['ds'].max()

st.write("SELECT FORECAST PERIOD")

periods_input = st.number_input('12',min_value = 1, max_value = 12)

if uploaded_file is not None:
     obj = Prophet()
     obj.fit(appdata)

st.write("VISUALIZE FORECASTED DATA")  
st.write("")
if uploaded_file is not None:
    future = obj.make_future_dataframe(periods=periods_input)
    fcst = obj.predict(future)
    forecast = fcst[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]


st.write(forecast) 
















