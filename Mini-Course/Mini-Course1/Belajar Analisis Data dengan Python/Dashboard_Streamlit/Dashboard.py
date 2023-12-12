import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
hourly_data = pd.read_csv('../Dataset/hour.csv')
daily_data = pd.read_csv('../Dataset/day.csv')

# Pertanyaan 1: Tren harian
st.title('Tren Harian Penyewaan Sepeda')
daily_rentals_trend = daily_data.groupby('dteday')['cnt'].sum()
st.line_chart(daily_rentals_trend)

# Pertanyaan 2: Tren musiman
st.title('Tren Musiman Penyewaan Sepeda (2011-2012)')
seasonal_rentals = hourly_data.groupby(['yr', 'season'])['cnt'].mean().unstack()
st.bar_chart(seasonal_rentals)

# Pertanyaan 3: Pengaruh kondisi cuaca
st.title('Pengaruh Kondisi Cuaca terhadap Jumlah Penyewaan Sepeda')
plt.figure(figsize=(10, 6))
sns.boxplot(x='weathersit', y='cnt', data=hourly_data, palette='coolwarm')
plt.title('Pengaruh Kondisi Cuaca terhadap Jumlah Penyewaan Sepeda')
plt.xlabel('Kondisi Cuaca')
plt.ylabel('Jumlah Penyewaan')
weather_conditions = ['Clear', 'Mist', 'Light Snow/Rain', 'Heavy Rain/Snow']
plt.xticks([0, 1, 2, 3], weather_conditions)

# Menampilkan plot menggunakan st.pyplot
st.pyplot(plt)