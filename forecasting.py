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
    model.add_regressor('GDP_Construction_Rs_Crs')
    model.add_regressor('GDP_Realestate_Rs_Crs')
    model.add_regressor('Oveall_GDP_Growth%')
    model.add_regressor('Water_Source')
    model.add_regressor('Limestone')
    model.add_regressor('Coal_Milliontonne')
    model.add_regressor('Home_Interest_Rate')
    model.add_regressor('Trasportation_Cost')
    model.add_regressor('Order_Quantity_Milliontonnes')
    model.add_regressor('Unit_Price')
    model.fit(appdata)
    future = model.make_future_dataframe(periods=12, freq = 'M')

new_data = st.file_uploader(" ", type=['xlsx'], accept_multiple_files = True)
if new_data is not None:
    data = pd.read_excel(new_data)  #read the data fro
    data = data.rename(columns={'Date':'ds'})
    data['ds'] = pd.to_datetime(data['ds']) 
st.write(data)












