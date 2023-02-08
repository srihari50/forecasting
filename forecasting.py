
import streamlit as st 
import pandas as pd
import numpy as np
from prophet import Prophet
from prophet.diagnostics import performance_metrics
from prophet.diagnostics import cross_validation
from prophet.plot import plot_cross_validation_metric

st.title('Cement Sales Forecasting')

data = st.file_uploader(' ',type='Xlsx', accept_multiple_files = True)
for data in data:
     if data is not None:
          appdata = pd.read_excel(data)
          newdata = pd.read_excel(data) 
          newdata['ds'] = pd.to_datetime(newdata['ds'])
     st.write(data) 
     










