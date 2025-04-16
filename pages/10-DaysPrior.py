import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
# Set up Streamlit page configuration
st.set_page_config(page_title='Days Prior', page_icon="✈", layout="wide", initial_sidebar_state="expanded")
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
     <center><h1 class="title-test"> 🛩 Days_Prior Bkg by Routes Summary </h1></center>
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
df['DAYS_PRIOR_SEG'] = df['DAYS_PRIOR'].apply(lambda x:'0-31' if 0 <= x < 31
                                              else '31-62' if 31 <= x < 62
                                              else '62-93' if 62 <= x < 93 
                                              else '93-124' if 93 <= x < 124
                                              else '124-155' if 124 <= x < 155
                                              else '155-186' if 155 <= x < 186
                                              else '186-217' if 186 <= x < 217
                                              else '217-248' if 217 <= x < 248
                                              else '248-279' if 248 <= x < 279
                                              else '279-310' if 279 <= x < 310
                                              else '310-341' if 310 <= x < 341
                                              else '341-372' if 341 <= x < 372
                                              else '372-403' if 372 <= x < 403
                                              else 'Out of range')
st.sidebar.markdown('<span style="color:Black">Please Filter Here: </span>', unsafe_allow_html=True)
#st.sidebar.markdown('<span style="color:Black">Route: </span>', unsafe_allow_html=True)

all_option = 'All'
routes = [all_option] + list(df["ROUTE"].unique())  # 'All' added to the options

# Dropdown using selectbox for route selection, including 'All'
Rout = st.sidebar.selectbox("Route", options=routes)

# Filter the data based on the selected route
if Rout == all_option:
    filtered_data = df  # No filtering if 'All' is selected
else:
    filtered_data = df[df["ROUTE"] == Rout]  # Filter based on selected route
############
# Sector filter
all_option_s='All'
sectors=[all_option_s]+list(filtered_data["SECTOR"].unique())
Sector = st.sidebar.selectbox("Sector:", options=sectors)
if Sector == all_option:
    filtered_data = filtered_data  # No filtering if 'All' is selected
else:
    filtered_data = filtered_data[filtered_data["SECTOR"] == Sector]  # Filter based on selected route
#################
all_option_s='All'
#filtered_data = filtered_data[filtered_data["FLT_NO"].isin(Flight_No)]  
Flight_No=[all_option_s]+list(filtered_data["FLT_NO"].unique())
Flight_No2= st.sidebar.selectbox("Flight No:", options=Flight_No)
if Flight_No2 == all_option:
    filtered_data = filtered_data  # No filtering if 'All' is selected
else:
    filtered_data = filtered_data[filtered_data["FLT_NO"] == Flight_No2]  
#################
all_option_s='All'
#filtered_data = filtered_data[filtered_data["FLT_NO"].isin(Flight_No)]  
DAY=[all_option_s]+list(filtered_data["DAY"].unique())
DAY2= st.sidebar.selectbox("Day:", options=DAY)
if DAY2 == all_option:
    filtered_data = filtered_data  
else:
    filtered_data = filtered_data[filtered_data["DAY"] == DAY2]  
##############
#DIRECTION
all_option_s='All'
Direction=[all_option_s]+list(filtered_data["DIRECTION"].unique())
Direction2= st.sidebar.selectbox("Direction:", options=Direction)
if Direction2 == all_option:
    filtered_data = filtered_data  
else:
    filtered_data = filtered_data[filtered_data["DIRECTION"] == Direction2] 
##################
##BOOKING_STATUS
all_option_s='All'
Booking=[all_option_s]+list(filtered_data["BOOKING_STATUS"].unique())
Booking2= st.sidebar.selectbox("BOOKING_STATUS:", options=Booking)
if Booking2 == all_option:
    filtered_data = filtered_data  
else:
    filtered_data = filtered_data[filtered_data["BOOKING_STATUS"] == Booking2] 
######################
all_option_s='All'
Contract=[all_option_s]+list(filtered_data["CONTRACT_STATUS"].unique())
Contract2= st.sidebar.selectbox("CONTRACT_STATUS:", options=Contract)
if Contract2 == all_option:
    filtered_data = filtered_data  
else:
    filtered_data = filtered_data[filtered_data["CONTRACT_STATUS"] == Contract2] 
##########
###contributor
all_option_s='All'
Contributor=[all_option_s]+list(filtered_data["CONTRIBUTOR"].unique())
Contributor2= st.sidebar.selectbox("CONTRIBUTOR:", options=Contributor)
if Contributor2 == all_option:
    filtered_data = filtered_data  
else:
    filtered_data = filtered_data[filtered_data["CONTRIBUTOR"] == Contributor2] 
#####################
seats_booked=filtered_data.groupby('DAYS_PRIOR_SEG',as_index=False)['SEATS_BOOKED'].sum()
total_revenue=filtered_data.groupby('DAYS_PRIOR_SEG',as_index=False)['NET_REVENUE'].sum()
merg_1=pd.merge(seats_booked,total_revenue,on='DAYS_PRIOR_SEG',how='inner')
merg_1['AVG_FARE_PER_SEAT']=merg_1['NET_REVENUE']/ merg_1['SEATS_BOOKED']
merg_1=merg_1.drop(columns=["NET_REVENUE"])
st.dataframe(merg_1)
###############FIGURES#############
# Add the first bar trace for Seats Booked
st.subheader("Seats Booked By Avg Fares")
#result1['totals']=(result1['Seats_Booked']+result1['Avl_Seats_by_Cap'])
result1 = merg_1.groupby(by=merg_1["DAYS_PRIOR_SEG"])[["SEATS_BOOKED","AVG_FARE_PER_SEAT"]].sum().reset_index()
fig3 = go.Figure()
fig3.add_trace(go.Bar(x=result1["DAYS_PRIOR_SEG"], y=result1["SEATS_BOOKED"], name="Seats Boooked"))
fig3.add_trace(go.Scatter(x=result1["DAYS_PRIOR_SEG"], y=result1["AVG_FARE_PER_SEAT"], mode="lines", name="Avg Fare Per Seat", yaxis="y2"))
fig3.update_layout(
        title="",
        xaxis=dict(
        title="Days Prior",
        tickangle=-45,  # Rotate text to the left
        tickmode='array',  # Ensure text is not overlapping
        showgrid=True,
        tickfont=dict(
            size=14,  # Font size for the x-axis labels
            #family="Times New Roman",
            color="black"
        )),
        yaxis=dict(title="NET_REVENUE", showgrid=False,tickfont=dict(
            size=14,
            color="black")),
        yaxis2=dict(title="SEATS_BOOKED", overlaying="y", side="right",tickfont=dict(
            size=14,
            color="black")),
        template="gridon",
        legend=dict(x=1, y=1)
    )
    
st.plotly_chart(fig3, use_container_width=True)
#________________________#
seats_booked2=df.groupby(['DAYS_PRIOR_SEG','ROUTE'],as_index=False)['SEATS_BOOKED'].sum()
total_revenue2=df.groupby(['DAYS_PRIOR_SEG','ROUTE'],as_index=False)['NET_REVENUE'].sum()
merg_2=pd.merge(seats_booked2,total_revenue2,on=['DAYS_PRIOR_SEG','ROUTE'],how='inner')
merg_2['AVG_FARE_PER_SEAT']=merg_2['NET_REVENUE']/ merg_2['SEATS_BOOKED']
merg_2=merg_2.drop(columns=["NET_REVENUE"])
st.dataframe(merg_2)
###GRAPHS
result2 = merg_2.groupby(by=merg_2["ROUTE"])[["SEATS_BOOKED","AVG_FARE_PER_SEAT"]].sum().reset_index()
fig3 = go.Figure()
fig3.add_trace(go.Bar(x=result2["ROUTE"], y=result2["SEATS_BOOKED"], name="Seats Boooked"))
fig3.add_trace(go.Scatter(x=result2["ROUTE"], y=result2["AVG_FARE_PER_SEAT"], mode="lines", name="Avg Fare Per Seat", yaxis="y2"))
fig3.update_layout(
        title="",
        xaxis=dict(
        title="Days Prior",
        tickangle=-45,  # Rotate text to the left
        tickmode='array',  # Ensure text is not overlapping
        showgrid=True,
        tickfont=dict(
            size=14,  # Font size for the x-axis labels
            #family="Times New Roman",
            color="black"
        )),
        yaxis=dict(title="NET_REVENUE", showgrid=False,tickfont=dict(
            size=14,
            color="black")),
        yaxis2=dict(title="SEATS_BOOKED", overlaying="y", side="right",tickfont=dict(
            size=14,
            color="black")),
        template="gridon",
        legend=dict(x=1, y=1)
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
