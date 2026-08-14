import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection

# Page configuration
st.set_page_config(page_title="CODM Dashboard", page_icon="🎮", layout="wide")

st.title("🎮 CODM Match Performance Dashboard")

# Connect to Google Sheets
conn = st.connection("gsheets", type=GSheetsConnection)

# Tabs for each game mode
tab1, tab2, tab3 = st.tabs(["Search & Destroy", "Hardpoint", "Control"])

with tab1:
    st.header("Search & Destroy Stats")
    try:
        df_snd = conn.read(worksheet="Sheet1", spreadsheet=st.secrets["connections"]["gsheets"]["snd_url"])
        st.dataframe(df_snd, use_container_width=True)
    except Exception as e:
        st.error(f"Error loading Search & Destroy data: {e}")

with tab2:
    st.header("Hardpoint Stats")
    try:
        df_hp = conn.read(worksheet="Sheet1", spreadsheet=st.secrets["connections"]["gsheets"]["hp_url"])
        st.dataframe(df_hp, use_container_width=True)
    except Exception as e:
        st.error(f"Error loading Hardpoint data: {e}")

with tab3:
    st.header("Control Stats")
    try:
        df_ctrl = conn.read(worksheet="Sheet1", spreadsheet=st.secrets["connections"]["gsheets"]["ctrl_url"])
        st.dataframe(df_ctrl, use_container_width=True)
    except Exception as e:
        st.error(f"Error loading Control data: {e}")
      
