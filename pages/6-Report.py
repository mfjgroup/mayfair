import pandas as pd
import streamlit as st
import plotly.express as px
#from streamlit_extras.dataframe_explorer import dataframe_explorer  # Optional, for exploring data
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import os
import numpy as np

# Set up Streamlit page configuration
st.set_page_config(page_title='Report', page_icon="✈", layout="wide", initial_sidebar_state="expanded")

#####################
# Custom HTML Title

html_title = """
    <style>
        .title-test{ color:#FFFFFF; font-weight:bold; padding:5px; border-radius:6px }
        .container {
            text-align: center;
            background-color: #800080;
            color: white;
            padding: 3px;
            border-radius: 20px;
        }
    </style>
     <div class="container"
     <center><h1 class="title-test"> 🛩 Monthly & Daily & Yearly Summary</h1></center>
     </div>
"""
st.markdown(html_title, unsafe_allow_html=True)
st.markdown("")
df = pd.read_excel('020525_RMS_Raw_Data2.xlsx', sheet_name='Booking_Data')  # Specify the sheet index or name

st.markdown('<span style="color:#7d3c98;font-weight:bold">Monthly Report: </span>', unsafe_allow_html=True)
df['Month'] = df['DATE_BOOKED'].dt.strftime('%b %Y')  #dt.month_name()
df['YearMonth'] = df['DATE_BOOKED'].dt.to_period('M')
    #df_sorted = df.sort_values('YearMonth')
    #apply(lambda x: f'{x:,}€')
seats_booked = df.groupby(['Month','YearMonth'],as_index=False)['SEATS_BOOKED'].sum()
total_Revenue=df.groupby(['Month','YearMonth'])['NET_REVENUE'].sum()
f_merge=pd.merge(seats_booked,total_Revenue,on=['Month','YearMonth'],how='inner')
f_merge=f_merge.sort_values(by=['YearMonth'])
f_merge = f_merge.reset_index(drop=True)
f_merge=f_merge.drop(columns=['YearMonth'])
f_merge['NET_REVENUE']=f_merge['NET_REVENUE'].apply(lambda x:f'{x:,}€')
col1,col2=st.columns(2)
with col1:
     st.dataframe(f_merge)
with col2:
      result = df.groupby(by=df["Month"])["NET_REVENUE"].sum().reset_index().sort_values(by='Month')
      fig1 = px.pie(result, names="Month", values="NET_REVENUE", title="")
      st.plotly_chart(fig1, use_container_width=True)
st.markdown("")
st.markdown('<span style="color:#7d3c98;font-weight:bold">Daily Report: </span>', unsafe_allow_html=True)
df['Day_Booked'] = df['DATE_BOOKED'].dt.strftime('%d %b %Y')
df['day_p'] = df['DATE_BOOKED'].dt.to_period('D')
seats_booked_d = df.groupby(['Day_Booked','day_p'],as_index=False)['SEATS_BOOKED'].sum()
total_Revenue_d=df.groupby(['Day_Booked','day_p'])['NET_REVENUE'].sum()
f_merge_d=pd.merge(seats_booked_d,total_Revenue_d,on=['Day_Booked','day_p'],how='inner')
f_merge_d=f_merge_d.sort_values(by=['day_p'])
f_merge_d = f_merge_d.reset_index(drop=True)
f_merge_d=f_merge_d.drop(columns=['day_p'])
f_merge_d['NET_REVENUE']=f_merge_d['NET_REVENUE'].apply(lambda x:f'{x:,}€')
col1,col2=st.columns(2)
with col1:
     st.dataframe(f_merge_d)
    #df=df.sort_values(by="DATE_BOOKED")
st.markdown("")
st.markdown("")
st.markdown('<span style="color:#7d3c98;font-weight:bold">Yearly Report: </span>', unsafe_allow_html=True)
df['Year'] = df['DATE_BOOKED'].dt.strftime('%Y')
df['year_p'] = df['DATE_BOOKED'].dt.to_period('Y')
seats_booked_y = df.groupby(['Year','year_p'],as_index=False)['SEATS_BOOKED'].sum()
total_Revenue_y=df.groupby(['Year','year_p'])['NET_REVENUE'].sum()
f_merge_y=pd.merge(seats_booked_y,total_Revenue_y,on=['Year','year_p'],how='inner')
f_merge_y=f_merge_y.sort_values(by=['year_p'])
f_merge_y = f_merge_y.reset_index(drop=True)
f_merge_y=f_merge_y.drop(columns=['year_p'])
f_merge_y['NET_REVENUE']=f_merge_y['NET_REVENUE'].apply(lambda x:f'{x:,}€')
col1,col2=st.columns(2)
with col1:
     headers = {
    'selector': 'th.col_heading',
    'props': [('background-color', '#F0F8FF'), ('color', 'F0F8FF')]
    }

     index_style = {
    'selector': 'th.index_name',
    'props': [('background-color', '#F0F8FF'), ('color', 'F0F8FF')]
    }
     tmp_year_style = (
     f_merge_y.style
        .set_table_styles([])  # Set header and index styles
        .set_properties(**{'background-color': '#ECE3FF', 'color': 'black'})  # Apply background and text color for the entire table
        #.apply(lambda x: x.round(2), subset=['Avl_Seats_by_Cap'])
        
 )
     st.dataframe(tmp_year_style)

with col2:
        result3 = df.groupby(by=df["Year"])["NET_REVENUE"].sum().reset_index()
        fig3 = px.pie(result3, names="Year", values="NET_REVENUE",title="Chart")
        fig3.update_layout(
        width=300,  # Set the width of the chart (adjust as necessary)
        height=200,  # Set the height of the chart (adjust as necessary)
        title_y=0.95,  # Adjust the title font size
        margin=dict(t=10, b=10, l=10, r=10)  # Reduce margins
    )
        st.plotly_chart(fig3, use_container_width=True)
