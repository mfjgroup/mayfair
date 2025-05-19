import pandas as pd
import streamlit as st
import plotly.express as px
<<<<<<< HEAD
import plotly.graph_objects as go
import numpy as np
# Set up Streamlit page configuration
st.set_page_config(page_title='Payment', page_icon="✈", layout="wide", initial_sidebar_state="expanded")
=======
from streamlit_extras.dataframe_explorer import dataframe_explorer  # Optional, for exploring data
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import os 
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
# Set up Streamlit page configuration
st.set_page_config(page_title='Revenue Management System', page_icon="✈", layout="wide", initial_sidebar_state="expanded")
>>>>>>> 6790240 (changed)
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
     <center><h1 class="title-test"> 🛩 Payment Summary </h1></center>
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
df = pd.read_excel('020525_RMS_Raw_Data2.xlsx', sheet_name='Booking_Data')  # Specify the sheet index or name

st.sidebar.markdown('<span style="color:Black">Please Filter Here: </span>', unsafe_allow_html=True)
##########################
<<<<<<< HEAD
# Filter the data based on the selected route
all_option_r = 'All'
ROUTE1 = [all_option_r] + list(df["ROUTE"].unique())
ROUTE2 = st.sidebar.multiselect("ROUTE:", options=ROUTE1)
 
# If 'All' is selected, show all data; otherwise, filter based on selected sectors
if all_option_r in ROUTE2 or len(ROUTE2) == 0:  # If 'All' is selected or nothing is selected
    filtered_data = df
else:
    filtered_data = df[df["ROUTE"].isin(ROUTE2)]
###############################
# Sector filter
all_option_s = 'All'
sec1 = [all_option_s] + list(filtered_data["SECTOR"].unique())
 
# Use multiselect instead of selectbox to allow multiple selections
sec2 = st.sidebar.multiselect("SECTOR:", options=sec1)

# If 'All' is selected, show all data; otherwise, filter based on selected sectors
if all_option_s in sec2 or len(sec2) == 0:  # If 'All' is selected or nothing is selected
    filtered_data = filtered_data
else:
    filtered_data = filtered_data[filtered_data["SECTOR"].isin(sec2)]
###############################
all_option_f = 'All'
flt11 = [all_option_f] + list(filtered_data["FLT_NO"].unique())
 
#
flt22 = st.sidebar.multiselect("FLT_NO:", options=flt11)

# If 'All' is selected, show all data; otherwise, filter based on selected sectors
if all_option_f in flt22 or len(flt22) == 0:  # If 'All' is selected or nothing is selected
    filtered_data = filtered_data
else:
    filtered_data = filtered_data[filtered_data["FLT_NO"].isin(flt22)]
######################################
all_option_d = 'All'
day1 = [all_option_d] + list(filtered_data["DAY"].unique())
day2 = st.sidebar.multiselect("DAY:", options=day1)
if all_option_d in day2 or len(day2) == 0:  # If 'All' is selected or nothing is selected
    filtered_data = filtered_data
else:
    filtered_data = filtered_data[filtered_data["DAY"].isin(day2)]
##################
#DIRECTION
all_option_di='All'
dir1=[all_option_di]+list(filtered_data["DIRECTION"].unique())

dir2 = st.sidebar.multiselect("DIRECTION:", options=dir1)

# If 'All' is selected, show all data; otherwise, filter based on selected sectors
if all_option_di in dir2 or len(dir2) == 0:  # If 'All' is selected or nothing is selected
    filtered_data = filtered_data
else:
    filtered_data = filtered_data[filtered_data["DIRECTION"].isin(dir2)]
#######################
all_option_b='All'
BOOKING_STATUS=[all_option_b]+list(filtered_data["BOOKING_STATUS"].unique())
BOOKING_STATUS2 = st.sidebar.multiselect("BOOKING_STATUS:", options=BOOKING_STATUS)

if all_option_b in BOOKING_STATUS2 or len(BOOKING_STATUS2) == 0:  # If 'All' is selected or nothing is selected
    filtered_data = filtered_data
else:
    filtered_data = filtered_data[filtered_data["BOOKING_STATUS"].isin(BOOKING_STATUS2)]
######################################################CONTRACT_STATUS
all_option_c='All'
Status=[all_option_c]+list(filtered_data["CONTRACT_STATUS"].unique())
Status2= st.sidebar.multiselect("CONTRACT_STATUS:", options=Status)

if all_option_c in Status2 or len(Status2) == 0:  # If 'All' is selected or nothing is selected
    filtered_data = filtered_data
else:
    filtered_data = filtered_data[filtered_data["CONTRACT_STATUS"].isin(Status2)]
####################################
###contributor
all_option_co='All'
cont=[all_option_co]+list(filtered_data["CONTRIBUTOR"].unique())
cont2= st.sidebar.multiselect("CONTRIBUTOR:", options=cont)

if all_option_co in cont2 or len(cont2) == 0:  # If 'All' is selected or nothing is selected
    filtered_data = filtered_data
else:
    filtered_data = filtered_data[filtered_data["CONTRIBUTOR"].isin(cont2)]
=======
all_option = 'All'
routes = [all_option] + list(df["ROUTE"].unique())  # 'All' added to the options
Rout = st.sidebar.selectbox("Route", options=routes)
# Filter the data based on the selected route
if Rout == all_option:
    filtered_data = df  # No filtering if 'All' is selected
else:
    filtered_data = df[df["ROUTE"] == Rout] #Filter based on selected route
############
# Sector filter
all_option_s='All'
SECTOR=[all_option_s]+list(filtered_data["SECTOR"].unique())
SECTOR2= st.sidebar.selectbox("Sector:", options=SECTOR)
if SECTOR2 == all_option_s:
    filtered_data = filtered_data  
else:
    filtered_data = filtered_data[filtered_data["SECTOR"] == SECTOR2] 
############
all_option_f='All'
FLT_NO=[all_option_f]+list(filtered_data["FLT_NO"].unique())
FLT_NO2= st.sidebar.selectbox("Flight No:", options=FLT_NO)
if FLT_NO2 == all_option_f:
    filtered_data = filtered_data  
else:
    filtered_data = filtered_data[filtered_data["FLT_NO"] == FLT_NO2] 
###################
all_option_d='All'
DAY=[all_option_d]+list(filtered_data["DAY"].unique())
DAY2= st.sidebar.selectbox("DAY No:", options=DAY)
if DAY2 == all_option_d:
    filtered_data = filtered_data  
else:
    filtered_data = filtered_data[filtered_data["DAY"] == DAY2] 
##################
#DIRECTION
all_option_di='All'
Direction=[all_option_di]+list(filtered_data["DIRECTION"].unique())
Direction2= st.sidebar.selectbox("Direction:", options=Direction)
if Direction2 == all_option_di:
    filtered_data = filtered_data  
else:
    filtered_data = filtered_data[filtered_data["DIRECTION"] == Direction2] 
#######################
all_option_b='All'
BOOKING_STATUS=[all_option_b]+list(filtered_data["BOOKING_STATUS"].unique())
BOOKING_STATUS2= st.sidebar.selectbox("BOOKING_STATUS:", options=BOOKING_STATUS)
if BOOKING_STATUS2 == all_option_b:
    filtered_data = filtered_data  
else:
    filtered_data = filtered_data[filtered_data["BOOKING_STATUS"] == BOOKING_STATUS2] 
##################
all_option_c='All'
Status=[all_option_c]+list(filtered_data["CONTRACT_STATUS"].unique())
Status2= st.sidebar.selectbox("CONTRACT_STATUS:", options=Status)
if Status2 == all_option_c:
    filtered_data = filtered_data  
else:
    filtered_data = filtered_data[filtered_data["CONTRACT_STATUS"] == Status2] 
###contributor
all_option_co='All'
cont=[all_option_co]+list(filtered_data["CONTRIBUTOR"].unique())
cont2= st.sidebar.selectbox("CONTRIBUTOR:", options=cont)
if Status2 == all_option_co:
    filtered_data = filtered_data  
else:
    filtered_data = filtered_data[filtered_data["CONTRIBUTOR"] == cont2] 
>>>>>>> 6790240 (changed)
#########pivote table 
Req_Seat=filtered_data.groupby(['CONTRIBUTOR','CONTRACT_STATUS'], as_index=False)['REQUESTED_SEATS'].sum()
seats_booked=filtered_data.groupby(['CONTRIBUTOR','CONTRACT_STATUS'], as_index=False)['SEATS_BOOKED'].sum()
net_rev =filtered_data.groupby(['CONTRIBUTOR','CONTRACT_STATUS'], as_index=False)['NET_REVENUE'].sum()
f_merge=pd.merge(Req_Seat,seats_booked,on=['CONTRIBUTOR','CONTRACT_STATUS'],how='inner')
s_merge=pd.merge(f_merge,net_rev,on=['CONTRIBUTOR','CONTRACT_STATUS'],how='inner')
    
st.dataframe(s_merge)
#####3
st.markdown("""
    <style>
        .metric-card {
            background-color: #008080;  
            padding: 5% 5% 5% 10%;
            border-radius: 10px;
            display: inline-block;
            width: 90%;
        }
        .metric-label {
            font-size: 16px;
            font-weight: bold;
             color:#FFFFFF
        }
        .metric-value {
            font-size: 24px;
            color:#FFFFFF
        }
        .metric_delta {
         background-color: #008080   
        }
     </style>
     """, unsafe_allow_html=True)
req_s=filtered_data['REQUESTED_SEATS'].sum()
total_sts=filtered_data['SEATS_BOOKED'].sum()
total_rev=filtered_data['NET_REVENUE'].sum()
col1,col2,col3,col4=st.columns(4)
with col1: 
      st.markdown(f"""
                <div class="metric-card">
                  <div class="metric-label">Requested Seats</div>
                  <div class="metric-value">{req_s:,.0f}</div>
                  <div class="metric_delta">💺</div>
                </div>
                  """,unsafe_allow_html=True)
with col2:
        st.markdown(f"""
                <div class="metric-card">
                  <div class="metric-label">Total Seats Booked</div>
                  <div class="metric-value">{total_sts:,.0f}</div>
                  <div class="metric_delta">💺</div>
                </div>
                  """,unsafe_allow_html=True)
with col3:
       st.markdown(f"""
                <div class="metric-card">
                  <div class="metric-label">Total Revenue</div>
                  <div class="metric-value">{total_rev:,.0f}€</div>
                  <div class="metric_delta">💶</div>
                </div>
                  """,unsafe_allow_html=True)

###
st.markdown("")
st.subheader("Total Revenue Per Contributor")
result1 = filtered_data.groupby(by=filtered_data["CONTRIBUTOR"])[["NET_REVENUE"]].sum().reset_index()
result1_sorted=result1.sort_values(by="NET_REVENUE",ascending=False)
fig3 = go.Figure()
fig3.add_trace(go.Bar(x=result1_sorted["CONTRIBUTOR"],
                       y=result1_sorted["NET_REVENUE"], 
                       textposition='auto',
                       textfont=dict(
                       size=14,      # Font size
                       style="italic",   
                       family="Times New Roman",    
                       color="black"    # Font color
    ),
                       name="Total Revenue"))
    
fig3.update_layout(
        title="",
        #xaxis=dict(title="Contributor"),
        xaxis=dict(
        title="Contributor",
        tickangle=-45,  # Rotate text to the left
        tickmode='array',  # Ensure text is not overlapping
        showgrid=True,
        tickfont=dict(
            size=14,  # Font size for the x-axis labels
            #family="Times New Roman",
            color="black"
        )),
        yaxis=dict(title="NET_REVENUE", showgrid=False,  tickfont=dict(
            size=14,
            color="black"
        )),
        template="gridon",
        legend=dict(x=1, y=1),
        font=dict(
        size=14,      # Font size
          # Font color
    )
    )
    
st.plotly_chart(fig3, use_container_width=True)
st.markdown("""
    <style>
        /* Adjust the width and height of the selectbox */
        .stSelectbox {
            width: 200px !important;    /* Set the width of the select box */
            #height: 50px !important;    /* Set the height of the select box */
            background-color: #800080;
            padding: 5px;
            border-radius: 10px
        }
        .stSelectbox>label {
            color: #FFFAFA;  /* Change label color */
        }
    </style>
        </style>
""", unsafe_allow_html=True)