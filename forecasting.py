
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
     for files in files:
          data = pd.read_excel(files)
          data = data.rename(columns={'Sales_Quantity_Milliontonnes': 'y', 'Date':'ds'})
          data['ds'] = pd.to_datetime(data['ds'])
          newdata = pd.read_excel(files)
st.write(files) 
st.write(newdata)











