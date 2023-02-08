
import streamlit as st 
import pandas as pd
import numpy as np
from prophet import Prophet
from prophet.diagnostics import performance_metrics
from prophet.diagnostics import cross_validation
from prophet.plot import plot_cross_validation_metric

st.title('Cement Sales Forecasting')

files = st.file_uploader(' ',type='Xlsx')
if files is not None:
     data = pd.read_excel(files)
     data = data.rename(columns={'Sales_Quantity_Milliontonnes': 'y', 'Date':'ds'})
     data['ds'] = pd.to_datetime(appdata['ds'])
st.write(files) 


files2 = st.file_uploader(' ',type='Xlsx', accept_multiple_files = True)
if files2 is not None:
     newdata = pd.read_excel(files2)
     newdata = newdata.rename(columns={'y', 'Date':'ds'})
     newdata['ds'] = pd.to_datetime(newdata['ds'])
st.write(newdata)










