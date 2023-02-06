import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from prophet import Prophet
from prophet.plot import plot_plotly, plot_components_plotly
from prophet.diagnostics import cross_validation
from prophet.diagnostics import performance_metrics
from prophet.plot import plot_cross_validation_metric
import streamlit as st

st.title("cement sales prediction app")
st.markdown('Sales Graph')

uploaded_file = st.file_uploader(" ", type=['xlsx'])

st.uploaded_file.rename(columns = {'Date' : 'ds', 'Sales_Quantity_Milliontonnes' : 'y'}, inplace = True)
uploaded_file


if uploaded_file is not None:     
    cement = pd.read_excel(uploaded_file)
    

    model = Prophet()

    st.info("Forecasted Value")
    
    
    st.model.component_modes

    future = model.make_future_dataframe(periods= 12, freq = 'M')

    forecast = model.predict(future)
    f = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]

    model.plot(forecast)
    
    model.plot_components(forecast)

    plot_plotly(model, forecast)

    df_cv = cross_validation(model, initial = '365 days', period = '180 days', horizon = '365 days')
    
    df_cv.head(), df_cv.tail()
    
    df_p = performance_metrics(df_cv)
    
    plot_cross_validation_metric(df_cv, metric = 'rmse')
    
    st.write("Sales Forecast: ", forecast)



