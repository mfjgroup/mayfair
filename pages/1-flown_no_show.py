import pandas as pd
import streamlit as st
import datetime
import plotly.express as px
import plotly.graph_objects as go
import os 
import numpy as np
# Set up Streamlit page configuration
st.set_page_config(page_title='Flown & No Show', page_icon="✈", layout="wide", initial_sidebar_state="expanded")
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
     <center><h1 class="title-test"> 🛩 Flown & No Show Summary 👤 </h1></center>
     </div>
"""
st.markdown(html_title, unsafe_allow_html=True)
st.markdown("""
    <style>
        .stSidebar 
        {
            background-color: #E6E6FA;
        }
    </style>
""", unsafe_allow_html=True)
st.markdown("""
     <style>
        .metric-card1 {
            background-color: #DDA0DD;  
            padding: 5% 5% 5% 10%;
            color:#000000;
            border-radius: 5px;
            display: inline-block;
            width: 60%;
        }
        .metric-label1 {
            font-size: 16px;
            font-weight: bold;
        }
        </style>
        """,unsafe_allow_html=True)
st.markdown("")
st.markdown("")

st.markdown("""
<style>
        input[type="radio"]:checked + label {
            background-color: blue !important;
            color: white !important;  /* Change text color to white */
        }
</style>
""",unsafe_allow_html=True)
st.markdown("""
    <style>
    span[data-baseweb="tag"] {
    background-color: Purple !important;
      }
   </style>
""",
    unsafe_allow_html=True,
)
genre = st.radio(
    "Choose Flown & No Show Type",
    ["Flown and No-Show % Rate","Flown and No-Show by Contributor"],
)

st.markdown("""
     <style>
        .metric-card {
            background-color: #FF00FF;  
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
         background-color: #FF00FF;   
        }
     </style>
     """, unsafe_allow_html=True)

df = pd.read_excel('020525_RMS_Raw_Data2.xlsx', sheet_name='PRL')
df['Dep Date']=df['Travel Date'].dt.strftime('%d %b %Y')
if genre=="Flown and No-Show % Rate":
 col1,col2=st.columns(2)
 #with col1:
  #  st.markdown(f"""
   #             <div class="metric-card1">
    #              <div class="metric-label1">Flown & No-Show Summary</div>
     #           </div>
      #            """,unsafe_allow_html=True)
 st.markdown("")
 st.markdown("")
 all_option_r = 'All'
 Route_1 = [all_option_r] + list(df["Route"].unique())
 Route_2 = st.sidebar.multiselect("Route:", options=Route_1)
 # If 'All' is selected, show all data; otherwise, filter based on selected sectors
 if all_option_r in Route_2 or len(Route_2) == 0:  # If 'All' is selected or nothing is selected
     filtered_data = df
 else:
     filtered_data = df[df["Route"].isin(Route_2)]
####################
 all_option_d = 'All'
 Day_1 = [all_option_d] + list(filtered_data["Day"].unique())
 Day_2 = st.sidebar.multiselect("Day:", options=Day_1)
# If 'All' is selected, show all data; otherwise, filter based on selected sectors
 if all_option_d in Day_2 or len(Day_2) == 0:  # If 'All' is selected or nothing is selected
     filtered_data = filtered_data
 else:
     filtered_data = filtered_data[filtered_data["Day"].isin(Day_2)]
#####################
 all_option_f = 'All'
 flt_1 = [all_option_f] + list(filtered_data["Flt_No."].unique())
 flt_2 = st.sidebar.multiselect("Flt_No.:", options=flt_1)
# If 'All' is selected, show all data; otherwise, filter based on selected sectors
 if all_option_f in flt_2 or len(flt_2) == 0:  # If 'All' is selected or nothing is selected
     filtered_data = filtered_data
 else:
     filtered_data = filtered_data[filtered_data["Flt_No."].isin(flt_2)]
#########################
 all_option_s = 'All'
 Sector_1 = [all_option_f] + list(filtered_data["Sector"].unique())
 Sector2 = st.sidebar.multiselect("Sector:", options=Sector_1)
# If 'All' is selected, show all data; otherwise, filter based on selected sectors
 if all_option_s in Sector2 or len(Sector2) == 0:  # If 'All' is selected or nothing is selected
     filtered_data = filtered_data
 else:
     filtered_data = filtered_data[filtered_data["Sector"].isin(Sector2)]
#########################
 all_option_dp = 'All'
 dp_1 = [all_option_dp] + list(filtered_data["Dep Date"].unique())
 dp_2 = st.sidebar.multiselect("Dep Date:", options=dp_1)
# If 'All' is selected, show all data; otherwise, filter based on selected sectors 
 if all_option_dp in dp_2 or len(dp_2) == 0:  # If 'All' is selected or nothing is selected
    filtered_data = filtered_data
 else:
    filtered_data = filtered_data[filtered_data["Dep Date"].isin(dp_2)]
#########################
 flown_count=filtered_data[filtered_data["Coupon Status"].isin(['Flown'])].groupby(['Route','Flt_No.','Coupon Status'],as_index=False)['PAX_COUNT'].sum()
 noshow_count=filtered_data[filtered_data["Coupon Status"].isin(['No Show'])].groupby(['Route','Flt_No.','Coupon Status'],as_index=False)['PAX_COUNT'].sum()
 merge_data=pd.merge(flown_count,noshow_count,on=['Route','Flt_No.'],how='outer')

 merge_data['Coupon Status_y']=merge_data['Coupon Status_y'].fillna("No Show")
 merge_data['Coupon Status_x']=merge_data['Coupon Status_x'].fillna("Flown")
 merge_data['PAX_COUNT_y']=merge_data['PAX_COUNT_y'].fillna(0)
 merge_data['PAX_COUNT_x']=merge_data['PAX_COUNT_x'].fillna(0)
 merge_data['Total Pax']=merge_data['PAX_COUNT_x']+merge_data['PAX_COUNT_y']
 merge_data['Flown%']=(merge_data['PAX_COUNT_x']/merge_data['Total Pax'])*100
 merge_data['Flown%']=merge_data['Flown%'].round()
 merge_data['No Show%']=(merge_data['PAX_COUNT_y']/merge_data['Total Pax'])*100
 merge_data['No Show%']=merge_data['No Show%'].round()
 merge_data=merge_data.iloc[:, [0,1,6,2,3,7,4,5,8]]
 st.dataframe(merge_data)
#########################

 col1,col2,col3,col4=st.columns(4)
 total_pax=merge_data['Total Pax'].sum()
 no_show=merge_data['PAX_COUNT_y'].sum()
 flown=merge_data['PAX_COUNT_x'].sum()
 with col1:
      st.markdown(f"""
                <div class="metric-card">
                  <div class="metric-label">Total Passenger</div>
                  <div class="metric-value">{total_pax:,.0f}</div>
                </div>
                  """,unsafe_allow_html=True)
 with col2: 
      st.markdown(f"""
                <div class="metric-card">
                  <div class="metric-label">Total No Show</div>
                  <div class="metric-value">{no_show:,.0f}</div>
                </div>
                  """,unsafe_allow_html=True)
 with col3: 
      st.markdown(f"""
                <div class="metric-card">
                  <div class="metric-label">Total Flown</div>
                  <div class="metric-value">{flown:,.0f}</div>
                </div>
                  """,unsafe_allow_html=True)


 fig3 = go.Figure()
# Add the first bar trace for Seats Booked
 st.subheader("Total Pax Per Coupon Status")

 result1 = merge_data.groupby(by=merge_data["Route"])[["Total Pax", "PAX_COUNT_x","PAX_COUNT_y"]].sum().reset_index()
###########FLOWN SCATTER

 merge_rout=merge_data.groupby(['Route'],as_index=False)['PAX_COUNT_x'].sum()
 merge_rout_2=merge_data.groupby(['Route'],as_index=False)['Total Pax'].sum()
 merge_rout_all=pd.merge(merge_rout,merge_rout_2,on=['Route'],how='inner')
 merge_rout_all['TotalPer%']= (merge_rout_all['PAX_COUNT_x']/merge_rout_all['Total Pax'])*100
 merge_rout_all['TotalPer%']=merge_rout_all['TotalPer%'].round()

#################NO SHOW SCATTER

 merge_rout_n=merge_data.groupby(['Route'],as_index=False)['PAX_COUNT_y'].sum()
 merge_rout_n_2=merge_data.groupby(['Route'],as_index=False)['Total Pax'].sum()
 merge_rout_all_n=pd.merge(merge_rout_n,merge_rout_n_2,on=['Route'],how='inner')
 merge_rout_all_n['TotalNoShow%']= (merge_rout_all_n['PAX_COUNT_y']/merge_rout_all_n['Total Pax'])*100
 merge_rout_all_n['TotalNoShow%']=merge_rout_all_n['TotalNoShow%'].round()

########################

 result1['Total Pax']=(result1['PAX_COUNT_x']+result1['PAX_COUNT_y'])
 fig3.add_trace(go.Bar(
    x=result1["Route"], 
    y=result1["PAX_COUNT_x"], 
    name="Flown Count", 
    marker=dict(color='DarkSlateGrey'),
    offsetgroup=0  # Keeps the bars for this trace in the first group
))

# Add the second bar trace for Available Seats by Cap
 fig3.add_trace(go.Bar(
     x=result1["Route"], 
     y=result1["PAX_COUNT_y"], 
    name="No Show Count", 
    marker=dict(color='#4CBCBC'),
    offsetgroup=0  # Keeps the bars for this trace in the second group
))

 fig3.add_trace(go.Scatter(
    x=merge_rout_all["Route"], 
    y=merge_rout_all["TotalPer%"], 
    mode="lines", 
    name="Flown Percent", 
    line=dict(color='#90EE90'),
    yaxis="y2"
))


 fig3.add_trace(go.Scatter(
    x=merge_rout_all_n["Route"], 
    y=merge_rout_all_n["TotalNoShow%"], 
    mode="lines", 
    name="No Show Percent", 
    line=dict(color='#FF4500'),
    yaxis="y2"
))


 fig3.update_layout(
    title="",
    xaxis=dict(title="Route"),
    yaxis=dict(
        title="Total", 
        showgrid=False
        ),
    yaxis2=dict(
        title="TotalPer%",
        overlaying="y",
        side="right"
    ),
    barmode="group",  # This arranges the bars side by side
    template="gridon",
    legend=dict(x=1, y=1),
)
# Plot the chart using Streamlit
 st.plotly_chart(fig3, use_container_width=True)
 #####################################################################

if  genre=="Flown and No-Show by Contributor":
 df2 = pd.read_excel('020525_RMS_Raw_Data2.xlsx', sheet_name='PRL')
 df2['Dep Date']=df2['Travel Date'].dt.strftime('%d %b %Y')

 st.markdown("")
 st.markdown("")
 #st.header('Flown & No-Show Per Contributors')
 all_option_r3 = 'All'
 Route_3 = [all_option_r3] + list(df2["Route"].unique())
 Route_4 = st.sidebar.multiselect("Route:", options=Route_3)
 # If 'All' is selected, show all data; otherwise, filter based on selected sectors
 if all_option_r3 in Route_4 or len(Route_4) == 0:  # If 'All' is selected or nothing is selected
     filtered_data_1 = df2
 else:
     filtered_data_1 = df2[df2["Route"].isin(Route_4)]
####################
 all_option_d = 'All'
 Day_1 = [all_option_d] + list(filtered_data_1["Day"].unique())
 Day_2 = st.sidebar.multiselect("Day:", options=Day_1)
# If 'All' is selected, show all data; otherwise, filter based on selected sectors
 if all_option_d in Day_2 or len(Day_2) == 0:  # If 'All' is selected or nothing is selected
     filtered_data_1 = filtered_data_1
 else:
     filtered_data_1 = filtered_data_1[filtered_data_1["Day"].isin(Day_2)]
#####################
 all_option_f = 'All'
 flt_1 = [all_option_f] + list(filtered_data_1["Flt_No."].unique())
 flt_2 = st.sidebar.multiselect("Flt_No.:", options=flt_1)
# If 'All' is selected, show all data; otherwise, filter based on selected sectors
 if all_option_f in flt_2 or len(flt_2) == 0:  # If 'All' is selected or nothing is selected
     filtered_data_1 = filtered_data_1
 else:
     filtered_data_1 = filtered_data_1[filtered_data_1["Flt_No."].isin(flt_2)]
#########################
 all_option_s = 'All'
 Sector_1 = [all_option_f] + list(filtered_data_1["Sector"].unique())
 Sector2 = st.sidebar.multiselect("Sector:", options=Sector_1)
# If 'All' is selected, show all data; otherwise, filter based on selected sectors
 if all_option_s in Sector2 or len(Sector2) == 0:  # If 'All' is selected or nothing is selected
     filtered_data_1 = filtered_data_1
 else:
     filtered_data_1 = filtered_data_1[filtered_data_1["Sector"].isin(Sector2)]
#########################
 all_option_dp = 'All'
 dp_1 = [all_option_dp] + list(filtered_data_1["Dep Date"].unique())
 dp_2 = st.sidebar.multiselect("Dep Date:", options=dp_1)
# If 'All' is selected, show all data; otherwise, filter based on selected sectors 
 if all_option_dp in dp_2 or len(dp_2) == 0:  # If 'All' is selected or nothing is selected
    filtered_data_1 = filtered_data_1
 else:
    filtered_data_1 = filtered_data_1[filtered_data_1["Dep Date"].isin(dp_2)]
############################
 all_option_cn = 'All'
 cnt_1 = [all_option_cn] + list(filtered_data_1["Contributors"].unique())
 cnt_2 = st.sidebar.multiselect("Contributors:", options=cnt_1)
# If 'All' is selected, show all data; otherwise, filter based on selected sectors 
 if all_option_cn in cnt_2 or len(cnt_2) == 0:  # If 'All' is selected or nothing is selected
    filtered_data_1 = filtered_data_1
 else:
    filtered_data_1 = filtered_data_1[filtered_data_1["Contributors"].isin(cnt_2)]
#############################
 pivote_table=pd.pivot_table(filtered_data_1, values='PAX_COUNT', index=['Contributors','Flt_No.','Dep Date','Sector'],
                       columns=['Coupon Status'], aggfunc="sum")
 coupon_status_values = ['Flown', 'No Show']
 pivote_table = pivote_table.reindex(columns=coupon_status_values, fill_value=0)
 pivote_table['Flown']=pivote_table['Flown'].fillna(0)
 pivote_table['No Show']=pivote_table['No Show'].fillna(0)
 col1,col2=st.columns(2)
 with col1:
  st.dataframe(pivote_table)
 col1,col2,col3,col4=st.columns(4)
 total_pax=pivote_table['Flown'].sum()
 st.markdown("""
     <style>
        .metric-card2 {
            background-color: #FF00FF;  
            padding: 5% 5% 5% 10%;
            color:#FFFFFF;
            border-radius: 10px;
            display: inline-block;
            width: 50%;
        }
        .metric-label2 {
            font-size: 16px;
            font-weight: bold;
        }
        .metric-value {
            font-size: 24px;
            color:#FFFFFF;
            font-weight:bold;
        }
        .metric_delta2 {
         background-color: #FF00FF;   
        }
     </style>
     """, unsafe_allow_html=True)
 col1,col2,col3=st.columns(3)
 with col1:
      st.markdown(f"""
                <div class="metric-card2">
                  <div class="metric-label2">Total Flown</div>
                  <div class="metric-value2">{total_pax:,.0f}</div>
                </div>
                  """,unsafe_allow_html=True)
 with col2:
      def graph3(filtered_data_1):
        fig1 = px.pie(filtered_data_1[filtered_data_1['Coupon Status'].isin(['Flown'])], names="Contributors", values="PAX_COUNT", title="Flown Percent")
        fig1.update_layout(
        width=300,  # Set the width of the chart (adjust as necessary)
        height=200,  # Set the height of the chart (adjust as necessary)
       title_font_size=16,
       title_y=1,  # Adjust the title font size
       margin=dict(t=20, b=20, l=20, r=20)  # Reduce margins
    )
        st.plotly_chart(fig1, use_container_width=True)
 
      if not filtered_data_1.empty:
              graph3(filtered_data_1)
 st.markdown("")
 total_pax_n=pivote_table['No Show'].sum()
 col1,col2,col3=st.columns(3)
 with col1:
      st.markdown(f"""
                <div class="metric-card2">
                  <div class="metric-label2">Total No Show</div>
                  <div class="metric-value2">{total_pax_n:,.0f}</div>
                </div>
                  """,unsafe_allow_html=True)
 with col2:
      def graph4(filtered_data_1):
        fig1 = px.pie(filtered_data_1[filtered_data_1['Coupon Status'].isin(['No Show'])], names="Contributors", values="PAX_COUNT", title="No Show Percent")
        fig1.update_layout(
        width=300,  # Set the width of the chart (adjust as necessary)
        height=200,  # Set the height of the chart (adjust as necessary)
       title_font_size=16,
       title_y=1,  # Adjust the title font size
       margin=dict(t=20, b=20, l=20, r=20)  # Reduce margins
    )
        st.plotly_chart(fig1, use_container_width=True)

      if not filtered_data_1.empty:
              graph4(filtered_data_1)