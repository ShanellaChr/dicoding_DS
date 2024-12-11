# Project Analysis Dashboard

Proyek ini memberikan analisis data dari Bike Sharing Dataset, menggunakan Jupyter Notebook (.ipynb) dan UI web menggunakan Streamlit.

## Project Overview

Proyek ini mencakup:  
- **Analisis Data**: Dengan menggunakan file `Proyek_Analisis_Data.ipynb`, saya menganalisis dataset menggunakan library Pandas, NumPy, serta berbagai library visualisasi untuk mendapatkan insight.  
- **Antarmuka Web**: File `dashboard.py` memungkinkan user berinteraksi dengan data melalui UI web berbasis Streamlit.  

## Installation

# 1. Setup Project Folder
mkdir "Project Analisa Data Dicoding" && cd "Project Analisa Data Dicoding"

# 2. Create and Activate Virtual Environment (venv)
python -m venv venv && .\venv\Scripts\activate  

# 3. Install Dependencies
pip install streamlit numpy pandas matplotlib seaborn  

# 4. Generate requirements.txt
pip freeze > requirements.txt  

# 5. Run Streamlit Application
streamlit run dashboard.py 
