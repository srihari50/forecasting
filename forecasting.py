import streamlit as st
import pandas as pd
import numpy as np
from prophet import Prophet
from prophet.diagnostics import performance_metrics
from prophet.diagnostics import cross_validation
from prophet.plot import plot_cross_validation_metric
import base64  

st.title('Time Series Forecasting Using Streamlit')

uploaded_files = st.file_uploader(" ", accept_multiple_files=True, type = ['xlxs'])
if uploaded_files is not None:
    for uploaded_files in uploaded_files:
         data = pd.read_excel(uploaded_file)
         future_data = pd.read_excel(uploaded_file)
    st.write(uploaded_file)
    st.write(uploaded_file)

if data is not None:
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
st.write(future)
   
forecast_data = model.predict(future)

forecast_data[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(12)










