import pandas as pd
import streamlit as st
import plotly.express as px
#from streamlit_extras.dataframe_explorer import dataframe_explorer  # Optional, for exploring data
import plotly.graph_objects as go
from datetime import datetime
import os 
# Set up Streamlit page configuration
st.set_page_config(page_title='Revenue', page_icon="✈", layout="wide", initial_sidebar_state="expanded")

st.set_page_config(page_title='Revenue Management System', page_icon="✈", layout="wide", initial_sidebar_state="expanded")
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
     <center><h1 class="title-test">🛩 Revenue Summary  📊 </h1></center>

     <center><h1 class="title-test">🛩 Revenue Sumarry </h1></center>
     </div>
"""
st.markdown(html_title, unsafe_allow_html=True)

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
df=pd.read_excel('020525_RMS_Raw_Data2.xlsx',sheet_name='Flight Rotation Weeks')
st.sidebar.markdown('<span style="color:Black">Filter: </span>', unsafe_allow_html=True)
#st.sidebar.title("Please Filter Here")
st.markdown("")
st.markdown("")
st.markdown('<span style="color:DarkCyan;font-weight:bold">Select Flight Date: </span>', unsafe_allow_html=True)
#st.sidebar.title ("Select Flight Date")
col1,col2,col3=st.columns(3)
#with col1:
 #st.markdown('<span style="color:Black">FSCODE: </span>', unsafe_allow_html=True)
 #fsc = st.multiselect("Filter By FSCODE:", options=df["FSCODE"].unique(), default=df["FSCODE"].unique())
 #dataset2 = df[df["FSCODE"].isin(fsc)]
with col1:
     start_date = st.date_input(label="Start Date (YYYY/MM/DD)")
with col2:
     end_date = st.date_input(label="End Date")
 
# Filter the dataset based on the selected date range
 #st.error(f"You have chosen analytics from: {start_date} to {end_date}")
st.markdown("")
dataset2 = df[(df["DEP_DATE"] >= pd.to_datetime(start_date)) & (df["DEP_DATE"] <= pd.to_datetime(end_date))]
##########################

all_option_r = 'All'
ROUTE1 = [all_option_r] + list(dataset2["ROUTE"].unique())

# Use multiselect instead of selectbox to allow multiple selections
ROUTE2 = st.sidebar.multiselect("ROUTE:", options=ROUTE1)

# If 'All' is selected, show all data; otherwise, filter based on selected sectors
if all_option_r in ROUTE2 or len(ROUTE2) == 0:  # If 'All' is selected or nothing is selected
    filtered_data = dataset2
else:
    filtered_data = dataset2[dataset2["ROUTE"].isin(ROUTE2)]   

all_option = 'All'
routes = [all_option] + list(df["ROUTE"].unique())  # 'All' added to the options
Rout = st.sidebar.selectbox("Route", options=routes)
# Filter the data based on the selected route
if Rout == all_option:
    filtered_data = dataset2  # No filtering if 'All' is selected
else:
    filtered_data = dataset2[dataset2["ROUTE"] == Rout] #Filter based on selected route

# Sector filter
all_option_s='All'
SECTOR=[all_option_s]+list(filtered_data["SECTOR"].unique())
SECTOR2= st.sidebar.multiselect("Sector:", options=SECTOR)

if all_option_s in SECTOR2 or len(SECTOR2) == 0:  # If 'All' is selected or nothing is selected
    filtered_data = filtered_data
else:
    filtered_data = filtered_data[filtered_data["SECTOR"].isin(SECTOR2)] 

all_option_f='All'
FLT_NO=[all_option_f]+list(filtered_data["FLT_NO"].unique())
FLT_NO2= st.sidebar.multiselect("FLT_NO:", options=FLT_NO)

if all_option_f in FLT_NO2 or len(FLT_NO2) == 0:  # If 'All' is selected or nothing is selected
    filtered_data = filtered_data
else:
    filtered_data = filtered_data[filtered_data["FLT_NO"].isin(FLT_NO2)] 

all_option_d='All'
DAY=[all_option_d]+list(filtered_data["DAY"].unique())
DAY2= st.sidebar.multiselect("DAY:", options=DAY)

if all_option_f in DAY2 or len(DAY2) == 0:  # If 'All' is selected or nothing is selected
    filtered_data = filtered_data
else:
    filtered_data = filtered_data[filtered_data["DAY"].isin(DAY2)] 


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
####################
dfn = pd.read_excel('020525_RMS_Raw_Data2.xlsx', sheet_name='Flight Plan Budget')
start_end_char_cost = dfn.groupby(['SCHED_ID', 'START', 'END', 'ROUTING'], as_index=False)['Net Cost'].sum()
tax_dfn = filtered_data.groupby(['SCHED_ID'], as_index=False)["Total Taxes"].sum()
NET_REVENUE = df.groupby(['SCHED_ID'], as_index=False)["NET_REVENUE"].sum()
agg_data1 = pd.merge(start_end_char_cost, tax_dfn, on=['SCHED_ID'], how='inner')
agg_data1['Total Net Cost']=agg_data1['Net Cost']+agg_data1['Total Taxes']
#st.dataframe(agg_data1)
agg_data2=pd.merge(agg_data1,NET_REVENUE,on=['SCHED_ID'],how='inner')
#st.dataframe(agg_data2)
agg_data2['Balance']=agg_data2['NET_REVENUE']-agg_data2['Total Net Cost']
#st.dataframe(agg_data2)
if agg_data2['Total Net Cost'].sum() > 0 :
  agg_data2['Rev & Net Cost(%)']=(agg_data2['NET_REVENUE']/agg_data2['Total Net Cost'].fillna(0))*100
elif agg_data2['Total Net Cost'].sum() == 0:
    agg_data2['Rev & Net Cost(%)']= 0
agg_data2['Rev & Net Cost(%)']=agg_data2['Rev & Net Cost(%)'].fillna(0)
agg_data2['Net Cost'] = agg_data2['Net Cost'].round(0).astype(int)
agg_data2['Total Taxes']=agg_data2['Total Taxes'].fillna(0) 
agg_data2['Total Taxes']=agg_data2['Total Taxes'].round(0)
agg_data2['Total Taxes']=agg_data2['Total Taxes'].astype(int)

agg_data2['Total Net Cost']=agg_data2['Total Net Cost'].fillna(0) 
agg_data2['Total Net Cost']=agg_data2['Total Net Cost'].round(0)
agg_data2['Total Net Cost']=agg_data2['Total Net Cost'].astype(int)

agg_data2['NET_REVENUE']=agg_data2['NET_REVENUE'].fillna(0) 
agg_data2['NET_REVENUE']=agg_data2['NET_REVENUE'].round(0)
agg_data2['NET_REVENUE']=agg_data2['NET_REVENUE'].astype(int)


agg_data2['Balance']=agg_data2['Balance'].fillna(0) 
agg_data2['Balance']=agg_data2['Balance'].round(0)
agg_data2['Balance']=agg_data2['Balance'].astype(int)


agg_data2['Rev & Net Cost(%)']=agg_data2['Rev & Net Cost(%)'].fillna(0) 

agg_data2['Rev & Net Cost(%)']=agg_data2['Rev & Net Cost(%)'].round(0).astype(int)

agg_data2['Rev & Net Cost(%)']=agg_data2['Rev & Net Cost(%)'].round(0)

#st.dataframe(agg_data2)
def highlight_colors(val):
     color = 'color:red' if val < 0 else 'color:LimeGreen'
     return color

pd.set_option('display.max_colwidth', 10000) 

style_agg_data2=agg_data2.style.map(highlight_colors,subset=['Balance'])
#style_agg_data2 = agg_data2.replace(['inf'], 0)
#st.dataframe(style_agg_data2)


agg_data2 = agg_data2.rename(columns={
    "SCHED_ID": 'SCHED_ID',
    "START": 'Start Date',
    "END": 'End Date',
    "ROUTING": 'Routing',
    "Net Cost": 'Charter Cost(€)',
    "Total Taxes": 'Total Taxes(€)',
    "NET_REVENUE": 'Revenue(€)',
    "Balance":'Balance(€)',
    "Revenue vs NetCost":'Rev vs NetCost(%)',
    "Total Net Cost": 'Total Net Cost(€)'
})

###################
def highlight_colors(val):
     color = 'color:red' if val < 0 else 'color:LimeGreen'
     return color

pd.set_option('display.max_colwidth', 10000) 
#pd.set_option('display.width', 1000) 
#st.dataframe(style_table_summer(agg_data2),use_container_width=True)
style_agg_data2=agg_data2.style.map(highlight_colors,subset=['Balance(€)'])
st.dataframe(style_agg_data2)



#################################################
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
     </style>
     """, unsafe_allow_html=True)

col1,col2,col3=st.columns(3)
c_cost=agg_data2["Charter Cost(€)"].sum()
t_taxes=agg_data2["Total Taxes(€)"].sum()
t_net=agg_data2["Total Net Cost(€)"].sum()

with col1:
     st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Total Charter Cost</div>
            <div class="metric-value">{c_cost:,.0f}€</div>
        </div>
    """, unsafe_allow_html=True)
with col2:
      st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Total Taxes</div>
            <div class="metric-value">{t_taxes:,.0f}€</div>
        </div>
    """, unsafe_allow_html=True)
with col3:
      st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Total Net Cost</div>
            <div class="metric-value">{t_net:,.0f}€</div>
        </div>
    """, unsafe_allow_html=True)
st.markdown("")
col1,col2,col3=st.columns(3)
t_net_r=agg_data2["Revenue(€)"].sum()
t_balance2=agg_data2["Balance(€)"].sum()
#t_net_c=(t_net_r/t_net)*100
if t_net > 0:
     t_net_c = (t_net_r / t_net) * 100
else:
     t_net_c = 0

with col1:
      st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Total Net Revenue</div>
            <div class="metric-value">{t_net_r:,.0f}€</div>
        </div>
    """, unsafe_allow_html=True)
with col2:
      st.markdown(f"""
        <div class="metric-card">

            <div class="metric-label">Net Profit</div>

            <div class="metric-label">Total Balance</div>

            <div class="metric-value">{t_balance2:,.0f}€</div>
        </div>
    """, unsafe_allow_html=True)
with col3:
      st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Revenue & Net Cost</div>
            <div class="metric-value">{t_net_c:,.0f}%</div>
        </div>
    """, unsafe_allow_html=True)
# Display the final result
st.markdown("")
st.markdown("")
col1,col2=st.columns(2)
def graph2(agg_data2):
     fig1 = px.pie(agg_data2, names="SCHED_ID", values="Revenue(€)", title="Revenue")
     fig1.update_layout(
        width=300,  # Set the width of the chart (adjust as necessary)
        height=200,  # Set the height of the chart (adjust as necessary)
        title_font_size=16,
        title_y=0.95,  # Adjust the title font size
        margin=dict(t=10, b=10, l=10, r=10)  # Reduce margins
    )
     st.plotly_chart(fig1, use_container_width=True)
with col1:
     if not agg_data2.empty:
      graph2(agg_data2)
     def graph2(agg_data2):
      fig1 = px.pie(agg_data2, names="SCHED_ID", values="Total Net Cost(€)", title="Net Cost")
      fig1.update_layout(
        width=300,  # Set the width of the chart (adjust as necessary)
        height=200,  # Set the height of the chart (adjust as necessary)
        title_font_size=16,  # Adjust the title font size
        title_y=0.95,
        margin=dict(t=10, b=10, l=10, r=10)  # Reduce margins
    )
      st.plotly_chart(fig1, use_container_width=True)
with col2:
     if not agg_data2.empty:
      graph2(agg_data2)
################
st.markdown(""" <style>
        .label-custom {
        background-color: #f5b7b1;
        color: #333;
        padding: 20px 100px;
        border-radius: 12px;
        font-size: 14px;
        font-weight:bold
    }
    </style>
    """, unsafe_allow_html=True)
st.markdown('<span class="label-custom">All Schedule:</span>', unsafe_allow_html=True)










st.markdown("")
col1,col2=st.columns(2)
group_seats_book=df.groupby(['SCHED_ID','FLT_NO','SECTOR','Sector Tax'], as_index=False)['Seats_Booked'].sum()
group_seats_total_tax=df.groupby(['SCHED_ID','FLT_NO','SECTOR','Sector Tax'], as_index=False)['Total Taxes'].sum()

Total_Capacity_a = df.groupby(['SCHED_ID','FLT_NO', 'SECTOR','Sector Tax'])['Y_Capacity'].sum()
Total_seats_a=df.groupby(['SCHED_ID','FLT_NO', 'SECTOR','Sector Tax'])['Seats_Booked'].sum()
BookLoadAll=(Total_seats_a/Total_Capacity_a.replace(0,pd.NA))*100
BookLoadAll=BookLoadAll.fillna(0)
BookLoadAll = BookLoadAll.round(0)
BookLoadAll.name='BookLoadAll'
agg_data_a = pd.merge(group_seats_book, group_seats_total_tax, on=['SCHED_ID', 'FLT_NO', 'SECTOR','Sector Tax'], how='inner')
agg_data_v=pd.merge(agg_data_a,BookLoadAll,on=['SCHED_ID', 'FLT_NO', 'SECTOR','Sector Tax'],how='inner')
agg_data_v = agg_data_v.rename(columns={
               'SCHED_ID': 'Sched_ID',
               'FLT_NO': 'Flight No',
               'SECTOR': 'Sector',
               'Sector Tax': 'Sector Tax',
               'Seats_Booked': 'Seats Booked',
               'Total Taxes': 'Total Taxes',
                'BookLoadAll':'BookLoad%'
            })
st.dataframe(agg_data_v)
##########total
seat_all = df['Seats_Booked'].sum()
tax_all=df['Total Taxes'].sum()
Total_Capacity_2=df['Y_Capacity'].sum()
if Total_Capacity_2 > 0 :
     bookloadall2=(seat_all/Total_Capacity_2)*100
else:
     bookloadall2=0
col1,col2,col3,col4=st.columns(4)
with col1:
     st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Total Seats</div>
            <div class="metric-value">{seat_all:,.0f}</div>
        </div>
    """, unsafe_allow_html=True)
with col2:
     st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Total Taxes</div>
            <div class="metric-value">{tax_all:,.0f}€</div>
        </div>
    """, unsafe_allow_html=True)
with col3:
     st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">BookLoad</div>
            <div class="metric-value">{bookloadall2:,.0f}%</div>
        </div>
    """, unsafe_allow_html=True)
st.markdown("")
 ########33pie#######3
#elif page =="Rev & Seats Per Sched":
st.markdown("")
#st.markdown('<span class="label-custom">All Schedule:</span>', unsafe_allow_html=True)
total_rev=df["NET_REVENUE"].sum()
total_sts=df["Seats_Booked"].sum()
col1,col2=st.columns(2)
st.markdown("""
     <style>
        .metric-cardr {
            background-color: #008080;  
            padding: 5% 5% 5% 10%;
            border-radius: 10px;
            display: inline-block;
            width: 60%;
        }
        .metric-labelr {
            font-size: 16px;
            font-weight: bold;
            color:#FFFFFF
        }
        .metric-valuer {
            font-size: 24px;
            color:#FFFFFF
        }
     </style>
     """, unsafe_allow_html=True)
with col1:
      #st.metric(label="Total Revenue", value=f"{total_rev:,.0f}€", delta="💶")
      #st.metric(label="Total Seats Booked", value=f"{total_sts:,.0f}", delta="💺")
      st.markdown(f"""
        <div class="metric-cardr">
            <div class="metric-labelr">Total Net Revenue</div>
            <div class="metric-valuer">{total_rev:,.0f}€</div>
            <div class="metric-labelr">💶</div>
        </div>
    """, unsafe_allow_html=True)
      st.markdown("")
      st.markdown(f"""
        <div class="metric-cardr">
            <div class="metric-labelr">Total Seats</div>
            <div class="metric-valuer">{total_sts:,.0f}€</div>
            <div class="metric-labelr">💺</div>
        </div>
    """, unsafe_allow_html=True)
      net_revenue=df.groupby("SCHED_ID")["NET_REVENUE"].sum()
      total_seats=df.groupby("SCHED_ID")["Seats_Booked"].sum()
      merge_rev_s=pd.merge(net_revenue,total_seats,on=['SCHED_ID'],how='inner')
with col2:
       st.dataframe(merge_rev_s)
st.subheader("Revenue & Seats per Sched")
st.markdown("")
 ##########33
col1,col2=st.columns(2)

def graph(filtered_data):
       fig = px.pie(filtered_data, names="SCHED_ID", values="Seats_Booked", title="Seats")
       fig.update_layout(
        width=300,  # Set the width of the chart (adjust as necessary)
        height=200,  # Set the height of the chart (adjust as necessary)
        title_font_size=16,  # Adjust the title font size
        margin=dict(t=30, b=30, l=30, r=30)  # Reduce margins
    )
       st.plotly_chart(fig, use_container_width=True)
with col1:
       if not df.empty:
        graph(df)
def graph(filtered_data):
       fig = px.pie(filtered_data, names="SCHED_ID", values="NET_REVENUE", title="Revenue")
       fig.update_layout(
        width=300,  # Set the width of the chart (adjust as necessary)
        height=200,  # Set the height of the chart (adjust as necessary)
        title_font_size=16,  # Adjust the title font size
        margin=dict(t=30, b=30, l=30, r=30)  # Reduce margins
      )
       st.plotly_chart(fig, use_container_width=True)
with col2:
       if not df.empty:
        graph(df)
result = df.groupby(by=df["SCHED_ID"])["NET_REVENUE"].sum().reset_index()
fig1 = px.line(result, x="SCHED_ID", y="NET_REVENUE", title="", template="gridon")
st.plotly_chart(fig1, use_container_width=True)
st.markdown("")
###########3REVENUE BY CONTRIBUTOR
# Apply the custom label style
#elif page=="Rev & Seats Per Contributor":
st.markdown("")
###############
df4=pd.read_excel('020525_RMS_Raw_Data2.xlsx',sheet_name='Booking_Data')
st.markdown('<span class="label-custom">Revenue Per Contributor:</span>', unsafe_allow_html=True)
st.markdown("")
cont_rev=df4.groupby("CONTRIBUTOR")["NET_REVENUE"].sum()
cont_seat=df4.groupby("CONTRIBUTOR")["SEATS_BOOKED"].sum()
merge_cont=pd.merge(cont_rev,cont_seat,on=('CONTRIBUTOR'),how='inner')
##total reve & seats
t_con_rev=df4["NET_REVENUE"].sum()
t_con_seats=df4["SEATS_BOOKED"].sum()
col1,col2=st.columns(2)
with col1:
       st.dataframe(merge_cont)
with col2:
        st.markdown(f"""
        <div class="metric-cardr">
            <div class="metric-labelr">Total Revenue</div>
            <div class="metric-valuer">{t_con_rev:,.0f}€</div>
            <div class="metric-labelr">💶</div>
        </div>
    """, unsafe_allow_html=True)
        st.markdown("")
        st.markdown(f"""
        <div class="metric-cardr">
            <div class="metric-labelr">Total Seats</div>
            <div class="metric-valuer">{t_con_seats:,.0f}€</div>
            <div class="metric-labelr">💺</div>
        </div>""", unsafe_allow_html=True)

result1 = df4.groupby(by=df4["CONTRIBUTOR"])[["NET_REVENUE"]].sum().reset_index()
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

    #%%%%%%%%%%%
st.markdown("""
    <style>
        .stSidebar {
            background-color: #E6E6FA;
            #width=1000 !important; 
        }
    </style>
""", unsafe_allow_html=True)
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
st.markdown("""
    <style>
        /* Adjust the width and height of the selectbox */
         .stMultiSelect {
            width: 250px !important;    /* Set the width of the select box */
            #height: 300px !important;    /* Set the height of the select box */
        }
        </style>
            """, unsafe_allow_html=True)




# Custom CSS for radio buttons
st.markdown("""
    <style>
          .stRadio>label {
            color: #FF0000;  /* Change text color of the radio button */
        }
        .stRadio input[type='radio']:checked + label > div {
            background-color: #FFA500;  /* Change background color when selected */
            border-color: #FFA500;
    </style>
""", unsafe_allow_html=True)
##############
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
""", unsafe_allow_html=True)






