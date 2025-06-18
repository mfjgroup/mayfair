import pandas as pd
import streamlit as st
import plotly.express as plt
#from streamlit_extras.dataframe_explorer import dataframe_explorer  # Optional, for exploring data
import plotly.graph_objects as go
import os
import numpy as np

# Set up Streamlit page configuration
st.set_page_config(page_title='Contributor', page_icon="✈", layout="wide", initial_sidebar_state="expanded")


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
     <center><h1 class="title-test"> 🛩 Contributor Summary 📊 </h1></center>
     </div>
"""
st.markdown(html_title, unsafe_allow_html=True)



df=pd.read_excel('020525_RMS_Raw_Data2.xlsx', sheet_name='LookUp')


st.markdown("")
st.markdown("")

select=st.radio("Select Season:",["Summer","Easter"])

if select == "Summer":
 col1,col2,col3,col4=st.columns(4)

 st.sidebar.markdown('<span style="color:#008080;font-weight:bold">Select Flight Date:</span>', unsafe_allow_html=True)
 default_start_date = pd.to_datetime('2025-06-28')
 default_end_date = pd.to_datetime('2026-02-01')
 
 with col1:
     start_date = st.sidebar.date_input(label="Start Date (YYYY/MM/DD)",value=default_start_date)
 with col2:
     end_date = st.sidebar.date_input(label="End Date",value=default_end_date)
 all_option_sc = 'All'
 dataset2 = df[(df["FLIGHT_DATE"] >= pd.to_datetime(start_date)) & (df["FLIGHT_DATE"] <= pd.to_datetime(end_date))]
 dataset2['Day_Booked'] = dataset2['DATE_BOOKED'].dt.strftime('%d %b %Y')
 dataset2['Flt_Date'] = dataset2['FLIGHT_DATE'].dt.strftime('%d %b %Y')
 df_s=dataset2[dataset2["SCHED_ID"].isin
([
'S25-01','S25-02','S25-03','S25-04','S25-05',
'S25-06','S25-07','S25-08','S25-09','S25-10',
'S25-11','S25-12','S25-13','S25-14','S25-15'
])]
 sch_3 = [all_option_sc] + list(df_s["SCHED_ID"].unique())
 sch_4 = st.sidebar.multiselect("SCHED_ID:", options=sch_3)
# If 'All' is selected, show all data; otherwise, filter based on selected sectors 
 if all_option_sc in sch_4 or len(sch_4) == 0:  # If 'All' is selected or nothing is selected
    filtered_data = dataset2
 else:
   filtered_data = dataset2[dataset2["SCHED_ID"].isin(sch_4)]

###########################
 # Route filter
 all_option_R='All'
 ROUTE1=[all_option_R]+list(filtered_data["ROUTE"].unique())
 ROUTE2= st.sidebar.multiselect("ROUTE:", options=ROUTE1)

 if all_option_R in ROUTE2 or len(ROUTE2) == 0:  # If 'All' is selected or nothing is selected
    filtered_data = filtered_data
 else:
    filtered_data = filtered_data[filtered_data["ROUTE"].isin(ROUTE2)] 
 ################
 # Sector filter
 all_option_s='All'
 SECTOR=[all_option_s]+list(filtered_data["SECTOR"].unique())
 SECTOR2= st.sidebar.multiselect("Sector:", options=SECTOR)

 if all_option_s in SECTOR2 or len(SECTOR2) == 0:  # If 'All' is selected or nothing is selected
    filtered_data = filtered_data
 else:
    filtered_data = filtered_data[filtered_data["SECTOR"].isin(SECTOR2)] 
 #################
 all_option_F='All'
 FLTNO1=[all_option_F]+list(filtered_data["FLT_NO"].unique())
 FLTNO2= st.sidebar.multiselect("FLT_NO:", options=FLTNO1)

 if all_option_F in FLTNO2 or len(FLTNO2) == 0:  # If 'All' is selected or nothing is selected
    filtered_data = filtered_data
 else:
    filtered_data = filtered_data[filtered_data["FLT_NO"].isin(FLTNO2)] 
 ####################
 table_s = filtered_data[filtered_data["FSCODE"].isin(['S25'])].pivot_table(values='SEATS_BOOKED', 
                       index=['SCHED_ID', 'SECTOR', 'FLT_NO', 'Flt_Date', 'Y_Capacity', 'Seats_Booked','Avl_Seats_by_Cap'], 
                       columns='CONTRIBUTOR', 
                       aggfunc='sum', 
                       fill_value=0).reset_index().round(2)
 #table_s
 ##########################
 # Defining table header and index styles
 headers = {
    'selector': 'th.col_heading',
    'props': [('background-color', '#5E17EB'), ('color', 'white')]
}

 index_style = {
    'selector': 'th.index_name',
    'props': [('background-color', '#5E17EB'), ('color', 'white')]
}
 table_s['Avl_Seats_by_Cap']=table_s['Avl_Seats_by_Cap'].astype(int).round() 
 table_s['Seats_Booked']=table_s['Seats_Booked'].astype(int).round() 
 table_s['Y_Capacity']=table_s['Y_Capacity'].astype(int).round() 
 
# Apply styles to the DataFrame using .style
 tmp_pivot_style1 = (
    table_s.style
        .set_table_styles([headers, index_style])  # Set header and index styles
        .set_properties(**{'background-color': '#ECE3FF', 'color': 'black'})  # Apply background and text color for the entire table
        .map(lambda val: 'background-color: #FD636B; color: white' if val < 0 else '', subset=pd.IndexSlice[:, 'Avl_Seats_by_Cap'])
        
 )

 st.markdown("")
 st.markdown("")
 st.dataframe(tmp_pivot_style1)     

if select == "Easter":
 
 df2=pd.read_excel('020525_RMS_Raw_Data2.xlsx', sheet_name='LookUp')
 col1,col2,col3,col4=st.columns(4)

 st.sidebar.markdown('<span style="color:#008080;font-weight:bold">Select Flight Date:</span>', unsafe_allow_html=True)
 default_start_date = pd.to_datetime('2025-03-01')
 default_end_date = pd.to_datetime('2025-06-01')
 
 with col1:
     start_date = st.sidebar.date_input(label="Start Date (YYYY/MM/DD)",value=default_start_date)
 with col2:
     end_date = st.sidebar.date_input(label="End Date",value=default_end_date)
 all_option_sc = 'All'
 dataset3 = df2[(df2["FLIGHT_DATE"] >= pd.to_datetime(start_date)) & (df["FLIGHT_DATE"] <= pd.to_datetime(end_date))]
 dataset3['Day_Booked'] = dataset3['DATE_BOOKED'].dt.strftime('%d %b %Y')
 dataset3['Flt_Date'] = dataset3['FLIGHT_DATE'].dt.strftime('%d %b %Y')


 all_option_s = 'All'
 
 df_e=dataset3[dataset3["SCHED_ID"].isin(['E25-02A','E25-02B','E25-02C','E25-03A',
'E25-03B','E25-03C','E25-04','E25-05A','E25-05B','E25-06','E25-07A',
'E25-07B','E25-08','E25-09A','E25-09B'
])]
 
 sch_5 = [all_option_s] + list(df_e["SCHED_ID"].unique())

 sch_6 = st.sidebar.multiselect("SCHED_ID:", options=sch_5)
# If 'All' is selected, show all data; otherwise, filter based on selected sectors 
 if all_option_s in sch_6 or len(sch_6) == 0:  # If 'All' is selected or nothing is selected
    filtered_data2 = dataset3
 else:
   filtered_data2 = dataset3[dataset3["SCHED_ID"].isin(sch_6)]
############################
 # Route filter
 all_option_Re='All'
 ROUTE3=[all_option_Re]+list(filtered_data2["ROUTE"].unique())
 ROUTE4= st.sidebar.multiselect("ROUTE:", options=ROUTE3)

 if all_option_Re in ROUTE4 or len(ROUTE4) == 0:  # If 'All' is selected or nothing is selected
    filtered_data2 = filtered_data2
 else:
    filtered_data2 = filtered_data2[filtered_data2["ROUTE"].isin(ROUTE4)] 
 ################
 # Sector filter
 all_option_se='All'
 SECTOR3=[all_option_se]+list(filtered_data2["SECTOR"].unique())
 SECTOR4= st.sidebar.multiselect("Sector:", options=SECTOR3)

 if all_option_se in SECTOR4 or len(SECTOR4) == 0:  # If 'All' is selected or nothing is selected
    filtered_data2 = filtered_data2
 else:
    filtered_data2 = filtered_data2[filtered_data2["SECTOR"].isin(SECTOR4)] 
 #################
 all_option_Fe='All'
 FLTNO3=[all_option_Fe]+list(filtered_data2["FLT_NO"].unique())
 FLTNO4= st.sidebar.multiselect("FLT_NO:", options=FLTNO3)

 if all_option_Fe in FLTNO4 or len(FLTNO4) == 0:  # If 'All' is selected or nothing is selected
    filtered_data2 = filtered_data2
 else:
    filtered_data2 = filtered_data2[filtered_data2["FLT_NO"].isin(FLTNO4)] 
 #################
 table_E = filtered_data2[filtered_data2["FSCODE"].isin(['E25'])].pivot_table(values='SEATS_BOOKED', 
                       index=['SCHED_ID', 'SECTOR', 'FLT_NO', 'Flt_Date', 'Y_Capacity', 'Seats_Booked','Avl_Seats_by_Cap'], 
                      columns='CONTRIBUTOR', 
                      aggfunc='sum', 
                       fill_value=0).reset_index().round(2)


 table_E['Avl_Seats_by_Cap']=table_E['Avl_Seats_by_Cap'].astype(int).round() 
 table_E['Seats_Booked']=table_E['Seats_Booked'].astype(int).round() 
 table_E['Y_Capacity']=table_E['Y_Capacity'].astype(int).round() 
# Apply styles to the DataFrame using .style
 tmp_pivot_style = (
    table_E.style
        #.set_table_styles([headers, index_style])  # Set header and index styles
        .set_properties(**{'background-color': '#ECE3FF', 'color': 'black'},subset=pd.IndexSlice[:, table_E.columns[4]])  # Apply background and text color for the entire table
        .map(lambda val: 'background-color: #FD636B; color: white' if val < 0 else '', subset=pd.IndexSlice[:, 'Avl_Seats_by_Cap'])   
             )
 #styled_pivot = table_E.style.set_properties(**{'font-weight': 'bold'}, subset=pd.IndexSlice[:, table_E.columns[0]])
 st.markdown("")
 st.markdown("")
 st.dataframe(tmp_pivot_style)    
 
 #st.dataframe(grandtotal)                  
st.markdown("""
    <style>
    span[data-baseweb="tag"] {
    background-color: Purple !important;
      }
   </style>
""",
    unsafe_allow_html=True,
)