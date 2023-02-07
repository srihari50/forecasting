import matplotlib.pyplot as plt
import streamlit as st
from datetime import date
import pandas as pd
from PIL import Image
import pickle

st.header("Prediction")

def model_np():
	m = pickle.load(open('forecast_model.pkl', 'rb'))

	st.subheader("Using Prophet")
	df = data.copy()
	df.reset_index(inplace=True)
	df_train = df[['Date','Sales_Quantity_Milliontonnes']]
	df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

	future = m.make_future_dataframe(df_train)
	forecast = m.predict(future)
	forecast = forecast.rename(columns={"ds": "Date", "yhat1": "Sales_Quantity_Milliontonnes"})
	st.write("Forecasting of Etheruem Close Price from 2023-31-1 to 2023-31-12")
	st.write(forecast[['Date', 'Sales_Quantity_Milliontonnes']].head())
	st.write(f"Forecasting of Close Price of {period} days")
	st.line_chart(forecast['Close'])

model_np()
