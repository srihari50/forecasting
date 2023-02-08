
import streamlit as st 
import pandas as pd
import numpy as np
from prophet import Prophet
from prophet.diagnostics import performance_metrics
from prophet.diagnostics import cross_validation
from prophet.plot import plot_cross_validation_metric

st.title('Cement Sales Forecasting')

data = st.file_uploader(' ',type='Xlsx')
if data is not None:
  appdata = pd.read_excel(data)
  appdata = appdata.rename(columns={'Sales_Quantity_Milliontonnes': 'y', 'Date':'ds'})
  appdata['ds'] = pd.to_datetime(appdata['ds']) 

st.write(data)

if data is not None:
     obj = Prophet()
     obj.fit(appdata)










