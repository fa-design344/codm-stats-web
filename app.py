import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(page_title="CODM Dashboard", page_icon="🎮", layout="wide")

st.title("🎮 CODM Match Performance Dashboard")

# Convert standard Google Sheet URL to direct CSV export URL
def get_csv_url(sheet_url):
    sheet_id = sheet_url.split("/d/")[1].split("/")[0]
    return f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv"

# Read URLs from secrets
snd_url = st.secrets["connections"]["gsheets"]["snd_url"]
hp_url = st.secrets["connections"]["gsheets"]["hp_url"]
ctrl_url = st.secrets["connections"]["gsheets"]["ctrl_url"]

# Tabs for each game mode
tab1, tab2, tab3 = st.tabs(["Search & Destroy", "Hardpoint", "Control"])

with tab1:
    st.header("Search & Destroy Stats")
    try:
        df_snd = pd.read_csv(get_csv_url(snd_url))
        st.dataframe(df_snd, use_container_width=True)
    except Exception as e:
        st.error(f"Error loading Search & Destroy data: {e}")

with tab2:
    st.header("Hardpoint Stats")
    try:
        df_hp = pd.read_csv(get_csv_url(hp_url))
        st.dataframe(df_hp, use_container_width=True)
    except Exception as e:
        st.error(f"Error loading Hardpoint data: {e}")

with tab3:
    st.header("Control Stats")
    try:
        df_ctrl = pd.read_csv(get_csv_url(ctrl_url))
        st.dataframe(df_ctrl, use_container_width=True)
    except Exception as e:
        st.error(f"Error loading Control data: {e}")
