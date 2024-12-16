import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import FuncFormatter

# Function to load data
def load_data():
    day_df = pd.read_csv('day.csv')
    return day_df

day_df = load_data()

# Convert 'dteday' column to datetime format
day_df['dteday'] = pd.to_datetime(day_df['dteday'])
day_df['year'] = day_df['dteday'].dt.year
day_df['month'] = day_df['dteday'].dt.month
day_df['day'] = day_df['dteday'].dt.day

# Weather icons and descriptions
weather_icons = {
    1: "☀️",  # Clear, Few clouds, Partly cloudy
    2: "🌥️",  # Mist + Cloudy, Mist + Broken clouds
    3: "❄️",  # Light Snow, Light Rain + Thunderstorm
    4: "⛈️"   # Heavy Rain + Ice Pallets + Thunderstorm
}

# Season mapping with icons
season_mapping = {
    1: "🌸 Spring",
    2: "☀️ Summer",
    3: "🍂 Fall",
    4: "❄️ Winter"
}

# Page title and description
st.title("🚴‍♀️ Bike Data Analysis 🚴‍♀️")
st.markdown("""
Welcome to the **Bike Data Analysis App**!
Here, you can explore:
- **Monthly Trend Analysis**
- **Seasonal Trends**
- **Weather Impact**
- **Comparison: Weekday vs Weekend**

Use the menu on the left to select the type of analysis you want.
""")

# Sidebar configuration
st.sidebar.header("Configure Your Analysis")
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Bicycle_icon.svg/1200px-Bicycle_icon.svg.png", width=100)

st.sidebar.subheader("1. Select Analysis Type")
analysis_type = st.sidebar.radio(
    "Type of analysis:",
    ('Monthly Trend Analysis', 'Seasonal Analysis', 'Weather Analysis', 'Weekday vs Weekend')
)

st.sidebar.subheader("2. Select Date Range")
min_date = day_df['dteday'].min()
max_date = day_df['dteday'].max()

start_date, end_date = st.sidebar.date_input(
    "Date Range:",
    [min_date, max_date],
    min_value=min_date,
    max_value=max_date
)

# Filter data by selected date range
filtered_day_df = day_df[(day_df['dteday'] >= pd.to_datetime(start_date)) & (day_df['dteday'] <= pd.to_datetime(end_date))]

# Analysis based on user selection
if analysis_type == 'Monthly Trend Analysis':
    st.header("📅 Tren Penyewaan Sepeda Bulanan 📅")
    st.markdown("Analisis tren penyewaan sepeda dalam beberapa bulan terakhir.")

    # Total penyewaan per bulan
    monthly_data = filtered_day_df.groupby('month')['cnt'].sum().reset_index()

    # Line plot untuk tren
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.lineplot(x='month', y='cnt', data=monthly_data, marker='o', color='darkorange', ax=ax)
    ax.set_title('Tren Penyewaan Sepeda Bulanan', fontsize=16)
    ax.set_xlabel('Bulan', fontsize=12)
    ax.set_ylabel('Jumlah Penyewaan Sepeda', fontsize=12)
    ax.yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{int(x):,}'))
    ax.set_xticks(range(1, 13))
    ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    st.pyplot(fig)

    # Bar plot untuk total penyewaan per bulan
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x='month', y='cnt', data=monthly_data, color='teal', ax=ax)
    ax.set_title('Total Penyewaan Sepeda per Bulan', fontsize=16)
    ax.set_xlabel('Bulan', fontsize=12)
    ax.set_ylabel('Jumlah Penyewaan Sepeda', fontsize=12)
    ax.yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{int(x):,}'))
    ax.set_xticks(range(1, 13))
    ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    st.pyplot(fig)


elif analysis_type == 'Seasonal Analysis':
    st.header("🌸 Seasonal Analysis 🌸")
    st.markdown("Analyze total bike rentals by season.")

    filtered_day_df['season_name'] = filtered_day_df['season'].map(season_mapping)
    seasonal_data = filtered_day_df.groupby('season_name')['cnt'].sum().reset_index()

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x='season_name', y='cnt', data=seasonal_data, palette="pastel", ax=ax)
    ax.set_title('Total Rentals by Season', fontsize=16)
    ax.set_xlabel('Season', fontsize=12)
    ax.set_ylabel('Total Rentals', fontsize=12)
    ax.yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{int(x):,}'))
    st.pyplot(fig)

elif analysis_type == 'Weather Analysis':
    st.header("🌦️ Weather Analysis 🌦️")
    st.markdown("Explore how weather conditions affect bike rentals.")

    filtered_day_df['weather_icon'] = filtered_day_df['weathersit'].map(weather_icons)
    weather_data = filtered_day_df.groupby('weathersit')['cnt'].sum().reset_index()
    weather_data['icon'] = weather_data['weathersit'].map(weather_icons)

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x='weathersit', y='cnt', data=weather_data, palette="coolwarm", ax=ax)
    ax.set_title('Total Rentals by Weather Condition', fontsize=16)
    ax.set_xlabel('Weather Type', fontsize=12)
    ax.set_ylabel('Total Rentals', fontsize=12)
    ax.yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{int(x):,}'))
    ax.set_xticklabels([f"{icon} {desc}" for icon, desc in zip(weather_data['icon'], ['Clear', 'Mist', 'Snow', 'Rain'])])
    st.pyplot(fig)

elif analysis_type == 'Weekday vs Weekend':
    st.header("📅 Weekday vs Weekend 📅")
    st.markdown("Compare bike rentals on weekdays and weekends.")

    filtered_day_df['is_weekend'] = filtered_day_df['weekday'].apply(lambda x: 'Weekend' if x >= 5 else 'Weekday')
    weekend_data = filtered_day_df.groupby('is_weekend')['cnt'].sum().reset_index()

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x='is_weekend', y='cnt', data=weekend_data, palette="viridis", ax=ax)
    ax.set_title('Total Rentals: Weekday vs Weekend', fontsize=16)
    ax.set_xlabel('Day Type', fontsize=12)
    ax.set_ylabel('Total Rentals', fontsize=12)
    ax.yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{int(x):,}'))
    st.pyplot(fig)
