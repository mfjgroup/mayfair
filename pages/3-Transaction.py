import pandas as pd
import streamlit as st
import plotly.express as px
#from streamlit_extras.dataframe_explorer import dataframe_explorer  # Optional, for exploring data
import plotly.graph_objects as go
import os 
# Set up Streamlit page configuration

st.set_page_config(page_title='Transaction', page_icon="✈", layout="wide", initial_sidebar_state="expanded")

if 'logged_in' not in st.session_state or not st.session_state.logged_in:
    st.error("Access denied. Please log in from the Home page.")
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
     <center><h1 class="title-test"> 🛩 Transaction Summary </h1></center>
     </div>
"""
st.markdown(html_title, unsafe_allow_html=True)
###############

st.markdown("""
    <style>
        .metric-card {
            background-color: #008080;  
            padding: 5% 5% 5% 5%;
            display: inline-block;
            #border: 3px solid #FF7F50;
            width: 50%;
        }
        .metric-label {
            font-size: 16px;
            font-weight: bold;
            color: #FFFFFF;
        }
        .metric-value {
            font-size: 24px;
            color: #FFFFFF;
        }
     </style>
     """, unsafe_allow_html=True)
##############
st.markdown("")

#pd.set_option('display.max_colwidth', None) 
pd.set_option('display.width', 2000) 
#st.sidebar.image("images/logo.jpg",caption="")
# Load the dataset
df = pd.read_excel('020525_RMS_Raw_Data2.xlsx', sheet_name='Booking_Data')
  # Specify the sheet index or name

    # Load selected sheet into a DataFrame
st.sidebar.markdown('<span style="color:Black">Please Filter Here: </span>', unsafe_allow_html=True)
st.markdown("")
st.markdown('<span style="color:DarkCyan;font-weight:bold">Select Flight Date: </span>', unsafe_allow_html=True)
col1,col2,col3=st.columns(3)
with col1:
      start_date = st.date_input(label="Start Date (YYYY/MM/DD)")
with col2:
      end_date = st.date_input(label="End Date")
# Filter the dataset based on the selected date range
dataset2 = df[(df["FLIGHT_DATE"] >= pd.to_datetime(start_date)) & (df["FLIGHT_DATE"] <= pd.to_datetime(end_date))]
##########################
st.markdown("""
       <style>
        .stSidebar {
            background-color: #E6E6FA;
        }
    </style>
""", unsafe_allow_html=True)

###################

# Add an "All" option at the start

all_option_r = 'All'
ROUTE1 = [all_option_r] + list(dataset2["ROUTE"].unique())

# Use multiselect instead of selectbox to allow multiple selections
ROUTE2 = st.sidebar.multiselect("ROUTE:", options=ROUTE1)

# If 'All' is selected, show all data; otherwise, filter based on selected sectors
if all_option_r in ROUTE2 or len(ROUTE2) == 0:  # If 'All' is selected or nothing is selected
    filtered_data = dataset2
else:
    filtered_data = dataset2[dataset2["ROUTE"].isin(ROUTE2)]

# Display the filtered data (or whatever content you want)
##############
# Sector filter
all_option_s = 'ALL'

sector1 = [all_option_s] + list(filtered_data["SECTOR"].unique())
sector2=st.sidebar.multiselect("Sector",options=sector1)
if all_option_s in  sector2 or len(sector2)==0:
   filtered_data=filtered_data
else :
   filtered_data=filtered_data[filtered_data["SECTOR"].isin(sector2)]
############
all_option_f='All'
FLT_NO=[all_option_f]+list(filtered_data["FLT_NO"].unique())
FLT_NO2= st.sidebar.multiselect("Flight No:", options=FLT_NO)

if all_option_f in  FLT_NO2 or len(FLT_NO2)==0:
   filtered_data=filtered_data
else :
   filtered_data=filtered_data[filtered_data["FLT_NO"].isin(FLT_NO2)]

###################
all_option_d='All'
DAY=[all_option_d]+list(filtered_data["DAY"].unique())
DAY2= st.sidebar.multiselect("DAY:", options=DAY)

if all_option_d in  DAY2 or len(DAY2)==0:
   filtered_data=filtered_data
else :
   filtered_data=filtered_data[filtered_data["DAY"].isin(DAY2)]

##################

all_option_c = 'ALL'

CATG1=[all_option_c]+ list(filtered_data["CATEGORY"].unique())
CATG2=st.sidebar.multiselect("CATEGORY:",options=CATG1)

if all_option_c in CATG2 or len(CATG2)==0:
    filtered_data=filtered_data
else:
    filtered_data=filtered_data[filtered_data["CATEGORY"].isin(CATG2)]

###################
all_option_j='ALL'
JOUR1=[all_option_j] + list (filtered_data["JOURNEY"].unique())
JOUR2= st.sidebar.multiselect("Journey",options=JOUR1)

if all_option_j in JOUR2 or len(JOUR2)==0:
    filtered_data=filtered_data
else:
    filtered_data=filtered_data[filtered_data["JOURNEY"].isin(JOUR2)]

#DIRECTION
all_option_di='All'
Direction=[all_option_di]+list(filtered_data["DIRECTION"].unique())
Direction2= st.sidebar.multiselect("Direction:", options=Direction)

if all_option_di in Direction2 or len(Direction2)==0:
    filtered_data=filtered_data
else:
    filtered_data=filtered_data[filtered_data["DIRECTION"].isin(Direction2)]

#######################
all_option_b='All'
BOOKING_STATUS=[all_option_b]+list(filtered_data["BOOKING_STATUS"].unique())
BOOKING_STATUS2= st.sidebar.multiselect("BOOKING_STATUS:", options=BOOKING_STATUS)


if all_option_b in BOOKING_STATUS2 or len(BOOKING_STATUS2)==0:
    filtered_data=filtered_data
else:
    filtered_data=filtered_data[filtered_data["BOOKING_STATUS"].isin(BOOKING_STATUS2)]

##################
all_option_c='All'
Status=[all_option_c]+list(filtered_data["CONTRACT_STATUS"].unique())
Status2= st.sidebar.multiselect("CONTRACT_STATUS:", options=Status)

if all_option_c in Status2 or len(Status2)==0:
    filtered_data=filtered_data
else:
    filtered_data=filtered_data[filtered_data["CONTRACT_STATUS"].isin(Status2)]

###contributor
all_option_co='All'
cont=[all_option_co]+list(filtered_data["CONTRIBUTOR"].unique())
cont2= st.sidebar.multiselect("CONTRIBUTOR:", options=cont)

if all_option_c in cont2 or len(cont2)==0:
    filtered_data=filtered_data
else:
    filtered_data=filtered_data[filtered_data["CONTRIBUTOR"].isin(cont2)]

#######################
col1,col2=st.columns(2)
 ######################
filtered_data['Date Booked'] = filtered_data['DATE_BOOKED'].dt.strftime('%d %b %Y')
filtered_data['Flgiht Date'] = filtered_data['FLIGHT_DATE'].dt.strftime('%d %b %Y')

seats_book=filtered_data.groupby(['Date Booked','CONTRIBUTOR','JOURNEY','DIRECTION','FLT_NO','SECTOR','Flgiht Date'], as_index=False)['SEATS_BOOKED'].sum()
#avg_fare=filtered_data.groupby(['CONTRIBUTOR','JOURNEY','DIRECTION','FLT_NO','SECTOR','FLIGHT_DATE'], as_index=False)['BASE_FARE'].mean()
net_revenue=filtered_data.groupby(['Date Booked','CONTRIBUTOR','JOURNEY','DIRECTION','FLT_NO','SECTOR','Flgiht Date'], as_index=False)['NET_REVENUE'].sum()
f_merge=pd.merge(seats_book,net_revenue,on=['Date Booked','CONTRIBUTOR','JOURNEY','DIRECTION','FLT_NO','SECTOR','Flgiht Date'],how='inner')

#s_merge=pd.merge(f_merge,net_revenue,on=['CONTRIBUTOR','JOURNEY','DIRECTION','FLT_NO','SECTOR','FLIGHT_DATE'],how='inner')

f_merge["avg_fare"]=f_merge["NET_REVENUE"]/f_merge["SEATS_BOOKED"]
s_merge=f_merge.rename(columns=
                           {
                     "avg_fare":'Avg Base Fare'         
                           })

def style_table_summer1(df):
       return df.style.set_table_styles (
        [
            {
                'selector': 'tfoot td',  # Styling footer (if any)
                'props': [('background-color', '#4CAF50'),
                          ('color', 'white'),
                          ('font-weight', 'bold'),
                          ('text-align', 'center')]
            },
        ],
    ).format({
        'Avg Base Fare': '{:,.0f}€', 
        'NET_REVENUE': '{:,.0f}€'  # Format percentage
    })

#######33per contributor only
seats_book_c=filtered_data.groupby(['CONTRIBUTOR'], as_index=False)['SEATS_BOOKED'].sum()
net_revenue_c=filtered_data.groupby(['CONTRIBUTOR'], as_index=False)['NET_REVENUE'].sum()
c_merge=pd.merge(seats_book_c,net_revenue_c,on=['CONTRIBUTOR'],how='inner')
seats_book_t=filtered_data['SEATS_BOOKED'].sum()
net_revenue_t=filtered_data['NET_REVENUE'].sum()
with col1:
      st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">💶 Total Revenue</div>
            <div class="metric-value">{net_revenue_t:,.0f}€</div>
        </div>
    """, unsafe_allow_html=True)
with col2:
      st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">💺Total Seats</div>
            <div class="metric-value">{seats_book_t:,.0f}</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("")
st.markdown("") 
seats_book_c=filtered_data.groupby(['CONTRIBUTOR'], as_index=False)['SEATS_BOOKED'].sum()
net_revenue_c=filtered_data.groupby(['CONTRIBUTOR'], as_index=False)['NET_REVENUE'].sum()
c_merge=pd.merge(seats_book_c,net_revenue_c,on=['CONTRIBUTOR'],how='inner')
seats_book_t=filtered_data['SEATS_BOOKED'].sum()
net_revenue_t=filtered_data['NET_REVENUE'].sum()
st.markdown("")
col1,col2=st.columns(2)
def graph(c_merge):
 fig = px.pie(c_merge, names="CONTRIBUTOR", values="NET_REVENUE", hole=0.5,title="Graph1")
 fig.update_traces(text=c_merge["CONTRIBUTOR"], textposition="inside")
 fig.update_layout(
        width=400,  # Set the width of the chart (adjust as necessary)
        height=250,  # Set the height of the chart (adjust as necessary)
        title_font_size=16,
        title_y=0.95,  # Adjust the title font size
        margin=dict(t=10, b=10, l=10, r=10)  # Reduce margins
    )
 st.plotly_chart(fig, use_container_width=True)
st.write("Revenue Percentage Per Contributor")
    # Add the first graph (Pie chart)
with col1:
      if not filtered_data.empty:
        graph(c_merge)

    # Add the second graph (Total Revenue over time)
result = filtered_data.groupby(by=filtered_data["SECTOR"])["NET_REVENUE"].sum().reset_index()
fig1 = px.line(result, x="SECTOR", y="NET_REVENUE", title="Graph2", template="gridon")
fig1.update_layout(
        width=400,  # Set the width of the chart (adjust as necessary)
        height=250,  # Set the height of the chart (adjust as necessary)
        title_font_size=16,
        title_y=0.95,  # Adjust the title font size
        margin=dict(t=8, b=8, l=8, r=8)  # Reduce margins
    )
with col2:
      st.plotly_chart(fig1, use_container_width=True)
      st.write("Total Revenue Per Sector")
 
result1 = filtered_data.groupby(by=filtered_data["FLT_NO"])[["NET_REVENUE", "SEATS_BOOKED"]].sum().reset_index()    
fig3 = go.Figure()
fig3.add_trace(go.Bar(x=result1["FLT_NO"], y=result1["NET_REVENUE"], name="Total Revenue"))
fig3.add_trace(go.Scatter(x=result1["FLT_NO"], y=result1["SEATS_BOOKED"], mode="lines", name="Total Seats", yaxis="y2"))
fig3.update_layout(
        title="",
        xaxis=dict(
        title="Flight No",
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
st.dataframe(style_table_summer1(s_merge))
######33
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
#############
st.markdown("""
    <style>
    /* Change column width */
    .stDataFrame table th, .stDataFrame table td {
        width: 800px;  /* Adjust width as per your need */
    }

    /* Change row height */
    .stDataFrame table tr {
        height: 400px;  /* Adjust row height */
    }
    </style>
""", unsafe_allow_html=True)
st.markdown("""
    <style>
        /* Adjust the width and height of the selectbox */
        .stSelectbox, .stMultiSelect {
            width: 250px !important;    /* Set the width of the select box */
            #height: 300px !important;    /* Set the height of the select box */
        }
        </style>
""", unsafe_allow_html=True)
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