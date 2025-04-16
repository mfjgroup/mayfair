import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import os 
import numpy as np
# Set up Streamlit page configuration
st.set_page_config(page_title='PRL', page_icon="✈", layout="wide", initial_sidebar_state="expanded")
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
     <center><h1 class="title-test"> 🛩 Passenger Reconcillation List 📝 </h1></center>
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

st.sidebar.markdown('<span style="color:#008080;font-weight:bold">Select Departure Date:</span>', unsafe_allow_html=True)
col1,col2,col3,col4=st.columns(4)
default_start_date = pd.to_datetime('2024-03-01')
default_end_date = pd.to_datetime('2025-02-01')
with col1:
     start_date = st.sidebar.date_input(label="Start Date (YYYY/MM/DD)",value=default_start_date)
with col2:
     end_date = st.sidebar.date_input(label="End Date",value=default_end_date)

st.markdown("")
df = pd.read_excel('020525_RMS_Raw_Data2.xlsx', sheet_name='PRL')

df['Dep Date']=df['Travel Date'].dt.strftime('%d %b %Y')

dataset2 = df[(df["Travel Date"] >= pd.to_datetime(start_date)) & (df["Travel Date"] <= pd.to_datetime(end_date))]
dataset2['Dep Date']=dataset2['Travel Date'].dt.strftime('%d %b %Y')
dataset2['Sector']=dataset2['Orgn'] +"-" +dataset2['Dest']

all_option_d = 'All'
Day_1 = [all_option_d] + list(dataset2["Day"].unique())
Day_2 = st.sidebar.multiselect("Day:", options=Day_1)
# If 'All' is selected, show all data; otherwise, filter based on selected sectors
if all_option_d in Day_2 or len(Day_2) == 0:  # If 'All' is selected or nothing is selected
    filtered_data = dataset2
else:
    filtered_data = dataset2[dataset2["Day"].isin(Day_2)]

###########
all_option_sec='All'
sector1=[all_option_sec]+list(filtered_data["Sector"].unique())
sector2=st.sidebar.multiselect("Sector",options=sector1)

if all_option_sec in sector2 or len(sector2)==0:
     filtered_data=filtered_data
else:
     filtered_data=filtered_data[filtered_data["Sector"].isin(sector2)]
############
all_option_flt='All'
flt1=[all_option_flt]+list(filtered_data["Flt_No."].unique())
flt2=st.sidebar.multiselect("Flt_No.",options=flt1)

if all_option_flt in flt2 or len(flt2)==0:
     filtered_data=filtered_data
else:
     filtered_data=filtered_data[filtered_data["Flt_No."].isin(flt2)]
#####################
all_option_st='All'
sts1=[all_option_st]+list(filtered_data["Coupon Status"].unique())
sts2=st.sidebar.multiselect("Coupon Status",options=sts1)

if all_option_st in sts2 or len(sts2)==0:
     filtered_data=filtered_data
else:
     filtered_data=filtered_data[filtered_data["Coupon Status"].isin(sts2)]
#################
pax_count= filtered_data.groupby(['Dep Date','Day','Contributors','Lastname','Firstname','Title','Pax Type','Flt_No.','Orgn','Dest','Coupon Status','Remarks'],as_index=False)['PAX_COUNT'].count()

st.dataframe(pax_count)

st.markdown("""
    <style>
    span[data-baseweb="tag"] {
    background-color: Purple !important;
      }
   </style>
""",
    unsafe_allow_html=True,
)
###########
st.markdown("""
     <style>
        .metric-card {
            background-color: #FF1493;  
            padding: 5% 5% 5% 10%;
            color:#FFFFFF;
            border-radius: 10px;
            display: inline-block;
            width: 90%;
        }
        .metric-label {
            font-size: 16px;
            font-weight: bold;
        }
        .metric-value {
            font-size: 24px;
            color:#FFFFFF;
            font-weight:bold;
        }
        .metric_delta {
         background-color: #FF1493;   
        }
     </style>
     """, unsafe_allow_html=True)
col1,col2,col3,col4=st.columns(4)
total_pax=pax_count['PAX_COUNT'].sum()
with col1: 
      st.markdown(f"""
                <div class="metric-card">
                  <div class="metric-label">Total Pax</div>
                  <div class="metric-value">{total_pax:,.0f}</div>
                </div>
                  """,unsafe_allow_html=True)









