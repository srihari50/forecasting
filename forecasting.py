
import streamlit as st 
import pandas as pd
import numpy as np
from prophet import Prophet
from prophet.diagnostics import performance_metrics
from prophet.diagnostics import cross_validation
from prophet.plot import plot_cross_validation_metric

st.title('Cement Sales Forecasting')

st.file_uploader(' ',type='Xlsx', accept_multiple_files = True)

if data is not None:
     appdata = pd.read_excel(data)
     appdata['ds'] = pd.to_datetime(appdata['ds'],errors='coerce') 
     st.write(data) 
     










