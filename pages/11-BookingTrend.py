import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import os 
import numpy as np
# Set up Streamlit page configuration
st.set_page_config(page_title='Booking Trend', page_icon="✈", layout="wide", initial_sidebar_state="expanded")
html_title = """
    <style>
        .title-test{ color:#FFFFFF; font-weight:bold; padding:5px; border-radius:6px }
        .container {
            text-align: center;
            background-color: #800080;
            color: white;
            padding: 5px;
            border-radius: 20px;
        }
    </style>
     <div class="container"
     <center><h1 class="title-test"> 🛩 Booking Trend Summary </h1></center>
     </div>
"""
st.markdown(html_title, unsafe_allow_html=True)
st.markdown("""
    <style>
        .stSidebar {
            background-color: #E6E6FA;
        }
    </style>
""", unsafe_allow_html=True)
#####################
# Custom HTML Title
st.markdown("")
st.markdown("")
###############
st.markdown("""
    <style>
        .stSelectbox {
            background-color: #f0f8ff;  /* Set background color for dropdowns */
        }
        .stSelectbox>label {
            color: #008B8B;  /* Change label color */
        }
    </style>
""", unsafe_allow_html=True)

st.markdown(
    """
    <style>
  span[data-baseweb="tag"] {
  background-color: Purple !important;
      }
   </style>
""",
    unsafe_allow_html=True,
)
#logo_url=st.image("images/logo.jpg")
##############
st.markdown("")
df = pd.read_excel('020525_RMS_Raw_Data2.xlsx', sheet_name='Booking_Data')
df['Day_Booked'] = df['DATE_BOOKED'].dt.strftime('%d %b %Y')
df["Flight_Date"]=df["FLIGHT_DATE"].dt.strftime('%d %b %Y')
#st.dataframe(df)
seats_booked=df.groupby(["Day_Booked","SECTOR","Flight_Date"],as_index=False)["SEATS_BOOKED"].sum()
total_revenue=df.groupby(["Day_Booked","SECTOR","Flight_Date"],as_index=False)["NET_REVENUE"].sum()
merge_1=pd.merge(seats_booked,total_revenue,on=['Day_Booked','SECTOR','Flight_Date'],how="inner")
merge_1["Avg Fare Per Seat"]=merge_1["NET_REVENUE"]/merge_1["SEATS_BOOKED"]
merge_1=merge_1.drop(columns=["NET_REVENUE"])
st.dataframe(merge_1)
