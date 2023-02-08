import streamlit as st
import pandas as pd
import numpy as np
from prophet import Prophet
from prophet.diagnostics import performance_metrics
from prophet.diagnostics import cross_validation
from prophet.plot import plot_cross_validation_metric
import base64  

st.title('Time Series Forecasting Using Streamlit')

past_data = st.file_uploader(" ", type=['xlsx'])
if past_data is not None:
    appdata = pd.read_excel(past_data)  #read the data fro
    appdata = appdata.rename(columns={'Sales_Quantity_Milliontonnes': 'y', 'Date':'ds'})
    appdata['ds'] = pd.to_datetime(appdata['ds']) 
    
st.write(past_data) #display the data

if past_data is not None:
    model = Prophet()
    model_new.add_regressor('GDP_Construction_Rs_Crs')
    model_new.add_regressor('GDP_Realestate_Rs_Crs')
    model_new.add_regressor('Oveall_GDP_Growth%')
    model_new.add_regressor('Water_Source')
    model_new.add_regressor('Limestone')
    model_new.add_regressor('Coal_Milliontonne')
    model_new.add_regressor('Home_Interest_Rate')
    model_new.add_regressor('Trasportation_Cost')
    model_new.add_regressor('Order_Quantity_Milliontonnes')
    model_new.add_regressor('Unit_Price')
    model.fit(appdata)
    future = model.make_future_dataframe(periods=12, freq = 'M')
    
















