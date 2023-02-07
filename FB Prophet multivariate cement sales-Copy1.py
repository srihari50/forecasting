import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from prophet import Prophet
from prophet.plot import plot_plotly

df_train=pd.read_excel(r"C:\Users\sriha\Desktop\cement project\All India_Features - train data.xlsx")
df_test=pd.read_excel(r"C:\Users\sriha\Desktop\cement project\All India_Features - test data.xlsx")
df=df_train
df

df_train

df_train.columns, df.columns

df_train = df_train.rename(columns={'Sales_Quantity_Milliontonnes': 'y', 'Date':'ds'})

model_new = Prophet()

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

model_new.fit(df_train)

future_data = model_new.make_future_dataframe(periods=12, freq = 'M')

future_data.tail(12)

df = df.append(df_test)
df = df.rename(columns={'Sales_Quantity_Milliontonnes': 'y', 'Date':'ds'})
df.tail(12)

future_data=df[['ds', 'GDP_Construction_Rs_Crs', 'GDP_Realestate_Rs_Crs', 'Oveall_GDP_Growth%', 'Water_Source', 
                'Limestone', 'Coal_Milliontonne', 'Home_Interest_Rate', 'Trasportation_Cost','Order_Quantity_Milliontonnes',
                'Unit_Price']]
future_data

future_data.head(12)

df

forecast_data = model_new.predict(future_data)

forecast_data[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(12)

model_new.plot(forecast_data)

model_new.plot_components(forecast_data)

plot_plotly(model_new, forecast_data)

forecast_data['yhat'].tail(12), df['y'].tail(12)

from sklearn.metrics import mean_squared_error, mean_absolute_error, mean_absolute_percentage_error

mse = mean_squared_error(forecast_data['yhat'].tail(12), df['y'].tail(12))
mae = mean_absolute_error(forecast_data['yhat'].tail(12), df['y'].tail(12))
mape = mean_absolute_percentage_error(forecast_data['yhat'].tail(12), df['y'].tail(12))

mse, mae, mape

import pickle
with open('forecast_model.pkl', "wb") as f:
    pickle.dump(model_new, f)

import matplotlib.pyplot as plt
import streamlit as st
from datetime import date
import pandas as pd
from PIL import Image
import pickle

st.title('Ethereum Price Forecasting')


st.sidebar.title("About")
st.sidebar.info("Forecasting Close Price of Ethereum using 'NeuralProphet' Machine Learning model.")

def get_input():
    st.sidebar.header("Input From user")
    st.sidebar.subheader("Select range of Date for visualize data for particular date range.")
    st.sidebar.write("(From 2023-1-31 to 2023-12-31)")
    start_date = st.sidebar.text_input("Start Date", "2023-1-31")
    end_date = st.sidebar.text_input("End Date", "2023-12-31")
    st.write("")
    st.sidebar.subheader("Enter Period for Forecasting of Price")
    period = st.sidebar.text_input("Period (In Months)", "12")
    return start_date, end_date, period


START = "2023-1-31"
TODAY = date.today().strftime("%Y-%M-%d")

def get_data(start, end):
    df = pd.read_excel(r'C:\Users\sriha\Desktop\cement project\All India_Features - train data.xlsx')
    start = pd.to_datetime(start)
    end = pd.to_datetime(end)
    start_row = 0
    end_row = 0

    for i in range(0, len(df)):
        if start <=	pd.to_datetime(df['Date'][i]):
            start_row = i
            break
    for j in range(0, len(df)):
        if end >= pd.to_datetime(df['Date'][len(df)-1-j]):
            end_row = len(df) - 1 - j
            break

    df = df.set_index(pd.DatetimeIndex(df['Date'].values))
    return df.iloc[start_row:end_row+1, :]

start, end, period = get_input()
data = get_data(start, end)

st.subheader("Data")
st.write("First 5 Columns")
st.write(data.head())
st.write("Last 5 Columns")
st.write(data.tail())





