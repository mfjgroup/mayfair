import streamlit as st
import pandas as pd
from datetime import datetime
import plotly.express as px
#from streamlit_extras.dataframe_explorer import dataframe_explorer  # Optional, for exploring data
import plotly.graph_objects as go

# Streamlit config
st.set_page_config(
    page_title='Home',
    page_icon="✈",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Sample users dictionary (replace with a secure auth in production)
users = {
    "mayfairjets": "MFJ2025@rms",

}

# Initialize session state
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'username' not in st.session_state:
    st.session_state.username = ''

# ----------------------------
# LOGIN SECTION
# ----------------------------
if not st.session_state.logged_in:
    col1, col2, col3 = st.columns([1, 2, 1])  # Centering the form
    with col2:
        st.title("🔐 MFJ User Login")
        st.subheader("Login to Your Account")

        with st.form("login_form"):
            username = st.text_input("Username", placeholder="Enter your username")
            password = st.text_input("Password", placeholder="Enter your password", type="password")
            login_btn = st.form_submit_button("Login")

            if login_btn:
                if not username or not password:
                    st.warning("⚠️ Please fill in both username and password.")
                elif username in users and users[username] == password:
                    st.session_state.logged_in = True
                    st.session_state.username = username
                    st.rerun()
                else:
                    st.error("❌ Invalid username or password.")
else:
    # ----------------------------
    # LOGGED IN VIEW
    # ----------------------------
    st.success(f"✅ Welcome User, {st.session_state.username}!")
    #st.balloons()

    # Time display
    now = datetime.now()
    date_now = now.strftime("%d-%b-%y %H:%M:%S")
    st.markdown(f'<span style="color:#800080;font-weight:bold">Time is {date_now}</span>', unsafe_allow_html=True)

    # Header
    html_title = """
    <div class="container" style="text-align:center; background-color:#800080; color:white; padding:2px; border-radius:10px;">
        <h1 style="margin:0;">🛩 Revenue and Inventory Report 📊</h1>
    </div>
    """
    st.markdown(html_title, unsafe_allow_html=True)
    st.markdown("")
    st.markdown("")
    st.markdown("")
    sheets= st.radio("Select Tab",["Inventory","Transaction","Revenue"])  
    if sheets=='Inventory':
        col1,col2,col3,col4=st.columns(4)
        with col1:
         st.markdown("""
    <style>
        .metric-card {
            background-color: #000080;  
            padding: 5% 5% 5% 5%;
            display: inline-block;
            #border: 3px solid #FF7F50;
            width: 50%;
        }
     </style>
     """, unsafe_allow_html=True)

         st.markdown(f"""
                <div class="metric-card">
                  <div class="metric-label">Inventory Summary</div>
                </div>
                  """,unsafe_allow_html=True)
        df = pd.read_excel('020525_RMS_Raw_Data2.xlsx', sheet_name='Flight Rotation Weeks')
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

##############
        st.markdown("")
        st.markdown("")

        st.markdown('<span style="color:#008080;font-weight:bold">Select Flight Date:</span>', unsafe_allow_html=True)
        col1,col2,col3=st.columns(3)
        with col1:
          start_date = st.date_input(label="Start Date (YYYY/MM/DD)")
        with col2:
           end_date = st.date_input(label="End Date")
        st.markdown("")
        dataset2 = df[(df["DEP_DATE"] >= pd.to_datetime(start_date)) & (df["DEP_DATE"] <= pd.to_datetime(end_date))]
#################################### 
        all_option_fs = 'All'
        fs1_1 = [all_option_fs] + list(dataset2["FSCODE"].unique())
        fs2 = st.sidebar.multiselect("FSCODE:", options=fs1_1)
        if all_option_fs in fs2 or len(fs2) == 0:  # If 'All' is selected or nothing is selected
          filtered_data = dataset2
        else:
          filtered_data = dataset2[dataset2["FSCODE"].isin(fs2)]
####################################
        all_option_sc = 'All'
        shcd_1 = [all_option_sc] + list(filtered_data["SCHED_ID"].unique())
        shcd_2 = st.sidebar.multiselect("SCHED_ID:", options=shcd_1)
# If 'All' is selected, show all data; otherwise, filter based on selected sectors
        if all_option_sc in shcd_2 or len(shcd_2) == 0:  # If 'All' is selected or nothing is selected
           filtered_data = filtered_data
        else:
         filtered_data = filtered_data[filtered_data["SCHED_ID"].isin(shcd_2)]
############
        all_option_r = 'All'
        ROUTE1 = [all_option_r] + list(filtered_data["ROUTE"].unique())

# Use multiselect instead of selectbox to allow multiple selections
        ROUTE2 = st.sidebar.multiselect("ROUTE:", options=ROUTE1)
 
# If 'All' is selected, show all data; otherwise, filter based on selected sectors
        if all_option_r in ROUTE2 or len(ROUTE2) == 0:  # If 'All' is selected or nothing is selected
          filtered_data = filtered_data
        else:
         filtered_data = filtered_data[filtered_data["ROUTE"].isin(ROUTE2)]
########################################
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
########################################
        all_option_f = 'All'
        flt11 = [all_option_f] + list(filtered_data["FLT_NO"].unique())
 
# Use multiselect instead of selectbox to allow multiple selections
        flt22 = st.sidebar.multiselect("FLT_NO:", options=flt11)

# If 'All' is selected, show all data; otherwise, filter based on selected sectors
        if all_option_f in flt22 or len(flt22) == 0:  # If 'All' is selected or nothing is selected
          filtered_data = filtered_data
        else:
          filtered_data = filtered_data[filtered_data["FLT_NO"].isin(flt22)]

###################
        all_option_d = 'All'
        day1 = [all_option_d] + list(filtered_data["DAY"].unique())
 
# Use multiselect instead of selectbox to allow multiple selections
        day2 = st.sidebar.multiselect("DAY:", options=day1)

# If 'All' is selected, show all data; otherwise, filter based on selected sectors
        if all_option_d in day2 or len(day2) == 0:  # If 'All' is selected or nothing is selected
          filtered_data = filtered_data
        else:
           filtered_data = filtered_data[filtered_data["DAY"].isin(day2)]
##################
        all_option_fer = 'All'
        fer1 = [all_option_fer] + list(filtered_data["Ferry_Live"].unique())
 
# Use multiselect instead of selectbox to allow multiple selections
        fer2 = st.sidebar.multiselect("Ferry_Live:", options=fer1)

# If 'All' is selected, show all data; otherwise, filter based on selected sectors
        if all_option_fer in fer2 or len(fer2) == 0:  # If 'All' is selected or nothing is selected
           filtered_data = filtered_data
        else:
          filtered_data = filtered_data[filtered_data["Ferry_Live"].isin(fer2)]
#######################
        all_option_dir = 'All'
        dir1 = [all_option_dir] + list(filtered_data["DIRECTION"].unique())
 
# Use multiselect instead of selectbox to allow multiple selections
        dir2 = st.sidebar.multiselect("DIRECTION:", options=dir1)

# If 'All' is selected, show all data; otherwise, filter based on selected sectors
        if all_option_dir in dir2 or len(dir2) == 0:  # If 'All' is selected or nothing is selected
         filtered_data = filtered_data
        else:
          filtered_data = filtered_data[filtered_data["DIRECTION"].isin(dir2)]
########################
        y_capacity_T=filtered_data['Y_Capacity'].sum()
        seats_booked_t=filtered_data['Seats_Booked'].sum()
        avl_seat_cap_t=filtered_data['Avl_Seats_by_Cap'].sum()

        if y_capacity_T > 0:
          Bookload_t = (seats_booked_t / y_capacity_T) * 100
        else:
           Bookload_t = 0

        st.markdown("""
     <style>
        .metric-card {
            background-color: #6495ED;  
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
         background-color: #6495ED;   
        }
     </style>
     """, unsafe_allow_html=True)
        col1,col2,col3,col4=st.columns(4)
        with col1: 
         st.markdown(f"""
                <div class="metric-card">
                  <div class="metric-label">Total Capacity</div>
                  <div class="metric-value">{y_capacity_T:,.0f}</div>
                  <div class="metric_delta">💺</div>
                </div>
                  """,unsafe_allow_html=True)
        with col2: 
          st.markdown(f"""
                <div class="metric-card">
                  <div class="metric-label">Seats Booked</div>
                  <div class="metric-value">{seats_booked_t:,.0f}</div>
                  <div class="metric_delta">💺</div>
                </div>
                  """,unsafe_allow_html=True)
        with col3: 
           st.markdown(f"""
                <div class="metric-card">
                  <div class="metric-label">Avl Seats by Cap</div>
                  <div class="metric-value">{avl_seat_cap_t:,.0f}</div>
                  <div class="metric_delta">💺</div>
                </div>
                  """,unsafe_allow_html=True)
        with col4: 
         st.markdown(f"""
                <div class="metric-card">
                  <div class="metric-label">BookLoad</div>
                  <div class="metric-value">{Bookload_t:,.0f}%</div>
                </div>
                  """,unsafe_allow_html=True)
##############333
        st.markdown("")
        col1,col2,col3=st.columns(3)
        def graph3(filtered_data):
         fig1 = px.pie(filtered_data, names="SCHED_ID", values="Y_Capacity", title="Capacity")
         fig1.update_layout(
         width=300,  # Set the width of the chart (adjust as necessary)
         height=200,  # Set the height of the chart (adjust as necessary)
         title_font_size=16,
         title_y=0.99,  # Adjust the title font size
         margin=dict(t=30, b=30, l=30, r=30)  # Reduce margins
         )
         st.plotly_chart(fig1, use_container_width=True)
        with col1:
         if not filtered_data.empty:
             graph3(filtered_data)
        def graph(filtered_data):
         fig = px.pie(filtered_data, names="SCHED_ID", values="Seats_Booked", title="Seats")
         fig.update_layout(
         width=300,  # Set the width of the chart (adjust as necessary)
         height=200,  # Set the height of the chart (adjust as necessary)
         title_font_size=16,  # Adjust the title font size
         margin=dict(t=30, b=30, l=30, r=30)  # Reduce margins
    )
         st.plotly_chart(fig, use_container_width=True)
# Check if there is filtered data and run the graph function
        with col2:
         if not filtered_data.empty:
          graph(filtered_data)
        def graph2(filtered_data):
         fig1 = px.pie(filtered_data, names="SCHED_ID", values="Avl_Seats_by_Cap", title="Avl Seats")
         fig1.update_layout(
        width=300,  # Set the width of the chart (adjust as necessary)
        height=200,  # Set the height of the chart (adjust as necessary)
        title_font_size=16,  # Adjust the title font size
        margin=dict(t=30, b=30, l=30, r=30)  # Reduce margins
    )
         st.plotly_chart(fig1, use_container_width=True)
        with col3:
         if not filtered_data.empty:
          graph2(filtered_data)
################
        def highlight_lower_than_0(val):
         color = 'background-color:#FFC0CB' if val < 0 else ''
         return color
        def highlight_100_per(val2):
          color2 = 'background-color:#FFFF00' if val2 > 100 else ''
          return color2

###########
        filtered_data['DEP_DATE'] = pd.to_datetime(filtered_data['DEP_DATE'], errors='coerce')
        filtered_data['Dep Date'] = filtered_data['DEP_DATE'].dt.strftime('%d %b %Y')
        y_capacity=filtered_data.groupby(['SCHED_ID','FLT_NO','SECTOR','Dep Date','Ferry_Live'], as_index=False)['Y_Capacity'].sum()
        seats_booked=filtered_data.groupby(['SCHED_ID','FLT_NO','SECTOR','Dep Date','Ferry_Live'], as_index=False)['Seats_Booked'].sum()
        avl_seat_cap=filtered_data.groupby(['SCHED_ID','FLT_NO','SECTOR','Dep Date','Ferry_Live'], as_index=False)['Avl_Seats_by_Cap'].sum()
        f_merge=pd.merge(y_capacity,seats_booked,on=['SCHED_ID','FLT_NO','SECTOR','Dep Date','Ferry_Live'],how='inner')
        s_merge=pd.merge(f_merge,avl_seat_cap,on=['SCHED_ID','FLT_NO','SECTOR','Dep Date','Ferry_Live'],how='inner')

        s_merge['BookLoadAll'] = (s_merge['Seats_Booked'] / s_merge['Y_Capacity'].replace(0, pd.NA)) * 100
        s_merge['BookLoadAll'] = s_merge['BookLoadAll'].fillna(0)  # Replace NaN with 0 if no booking
        s_merge['BookLoadAll'] = s_merge['BookLoadAll'].round(0)  # Round to nearest whole number
        s_merge['BookLoadAll'] = s_merge['BookLoadAll'].astype(int)  # convert to int after rounding
#s_merge['Departure_Date'] = s_merge['DEP_DATE'].dt.strftime('%d %b %Y')

        s_merge=s_merge.rename(columns={
      "BookLoadAll":'BookLoad%' 
    }
    )

#st.dataframe(s_merge)
#styled_s_merge=s_merge.style.applymap(highlight_lower_than_0,subset=['Avl_Seats_by_Cap','BookLoad%'])
        styled_s_merge = s_merge.style.map(highlight_lower_than_0, subset=['Avl_Seats_by_Cap']) \
         .map(highlight_100_per, subset=['BookLoad%'])
#styled_s_merge2=style_table_summer1(styled_s_merge)
        def style_table_summer1(df):
         return df.style.set_table_styles(
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
        #'BookLoad%': '{:,.0f}%'  # Format percentage
    })
        st.markdown("")
        st.dataframe(styled_s_merge) 
    #result=st.dataframe(styled_s_merge) 
    #st.download_button(label='Download as pdf',data=result)  
#######$$$$$$$$$$$$$$$$$$$$

############3333FIGURES
        fig3 = go.Figure()
# Add the first bar trace for Seats Booked
        st.subheader("Total Seats & BookLoad Per Dep Date")
        result1 = s_merge.groupby(by=s_merge["SECTOR"])[["Seats_Booked", "BookLoad%","Avl_Seats_by_Cap"]].sum().reset_index()

        result1['totals']=(result1['Seats_Booked']+result1['Avl_Seats_by_Cap'])
        result1_sorted=result1.sort_values(by="Seats_Booked",ascending=False)
        result1['totals']=(result1['Seats_Booked']+result1['Avl_Seats_by_Cap'])
        result1_sorted=result1.sort_values(by="Seats_Booked",ascending=False)
        fig3.add_trace(go.Bar(
          x=result1["SECTOR"], 
          y=result1["Seats_Booked"], 
            name="Seats Book", 
           marker=dict(color='DarkGreen'),
         offsetgroup=0  # Keeps the bars for this trace in the first group
))

# Add the second bar trace for Available Seats by Cap
        fig3.add_trace(go.Bar(
     x=result1["SECTOR"], 
     y=result1["Avl_Seats_by_Cap"], 
    name="Avl_Seats_by_Cap", 
    marker=dict(color='DarkSeaGreen'),
    #text=result1['totals'],
    #textposition='outside',
    offsetgroup=0  # Keeps the bars for this trace in the second group
))

        fig3.add_trace(go.Bar(
    x=result1["SECTOR"], 
    y=result1["Seats_Booked"], 
    name="Seats Book", 
    marker=dict(color='DarkGreen'),
    offsetgroup=0  # Keeps the bars for this trace in the first group
))


# Add the scatter plot for Book Load %
        fig3.add_trace(go.Scatter(
     x=result1["SECTOR"], 
    y=result1["BookLoad%"], 
    mode="lines", 
    name="BookLoad", 
    marker=dict(color='blue'),
    yaxis="y2"
))
#fig3.update_traces(textposition="outside")
# Update layout to specify title, axis labels, and positioning
        fig3.update_layout(
     title="Seat Booking vs Available Capacity",
    xaxis=dict(title="SECTOR"),
    yaxis=dict(
        title="Seats Booked", 
        showgrid=False
       # title_x= 20
        ),
    yaxis2=dict(
        title="BookLoad%",
        overlaying="y",
        side="right"
    ),
    barmode="group",  # This arranges the bars side by side
    template="gridon",
    legend=dict(x=1, y=1),
)

# Plot the chart using Streamlit
        st.plotly_chart(fig3, use_container_width=True)
########################333
        fig4=go.Figure()
        result2=filtered_data.groupby(by=filtered_data["ROUTE"])[["Seats_Booked","Avl_Seats_by_Cap"]].sum().reset_index()

        fig4.add_trace(go.Bar(x=result2["ROUTE"],
                      y=result2["Seats_Booked"],
                      name="Seats_Booked",
                      marker=dict(color='DarkBlue'),
                      offsetgroup=0
                      ))

        fig4.add_trace(go.Bar(
                      x=result2["ROUTE"],
                      y=result2["Avl_Seats_by_Cap"],
                      name="Avl_Seats_by_Cap",
                      marker=dict(color='DeepSkyBlue'),
                      offsetgroup=0
                     ))

        fig4.add_trace(go.Bar(x=result2["ROUTE"],
                      y=result2["Seats_Booked"],
                      name="Seats_Booked",
                      marker=dict(color='DarkBlue'),
                      offsetgroup=0
                      ))

        fig4.update_layout(
     barmode="group",  # This arranges the bars side by side
     template="gridon",
     xaxis=dict(title="Route"),
    
     legend=dict(x=1, y=1)
)
        st.plotly_chart(fig4,use_container_width=True)
#########
        pd.set_option('display.max_colwidth', None) 
        pd.set_option('display.width', 1000) 
        st.markdown("""
    <style>
        .stSidebar {
            background-color: #E6E6FA;
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
     
    # Hide sidebar toggle
        st.markdown(
        """
        <style>
            div[data-testid="collapsedControl"] {
                visibility: hidden;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Optional: Image background container (commented out if no image is provided)
        st.markdown(
        """
        <style>
        .image-container {
            display: flex;
            justify-content: center;
            align-items: center;
            background-size: cover;
            height: 400px;
            width: 100%;
        }
        </style>
        <div class="image-container"></div>
        """,
        unsafe_allow_html=True
    )
    if  sheets=='Transaction':
       col1,col2,col3,col4=st.columns(4)
       with col1:
         st.markdown("""
    <style>
        .metric-card {
            background-color: #000080;  
            padding: 5% 5% 5% 5%;
            display: inline-block;
            #border: 3px solid #FF7F50;
            width: 50%;
        }
     </style>
     """, unsafe_allow_html=True)

         st.markdown(f"""
                <div class="metric-card">
                  <div class="metric-label">Transaction Summary</div>
                </div>
                  """,unsafe_allow_html=True)
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
    if sheets=='Revenue':
       col1,col2,col3,col4=st.columns(4)
       with col1:
         st.markdown("""
    <style>
        .metric-card {
            background-color: #000080;  
            padding: 5% 5% 5% 5%;
            display: inline-block;
            #border: 3px solid #FF7F50;
            width: 50%;
        }
     </style>
     """, unsafe_allow_html=True)

         st.markdown(f"""
                <div class="metric-card">
                  <div class="metric-label">Revenue Summary</div>
                </div>
                  """,unsafe_allow_html=True)

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

       all_option_fs = 'All'

       dataset2=dataset2[dataset2["SCHED_ID"].isin
([
'E25-02A','E25-02B','E25-03B','E25-04','E25-05A','E25-05B','E25-08','E25-09A','E25-09B','E25-10','S25-01','S25-02',
'S25-03','S25-04','S25-06','S25-07','S25-08','S25-12','S25-13','S25-14','S25-15','S25-16','S25-17','S25-18',
'S25-19','S25-20','S25-22','S25-23','S25-24','S25-26','S25-27'
])]

       fs1 = [all_option_fs] + list(dataset2["FSCODE"].unique())

# Use multiselect instead of selectbox to allow multiple selections
       fs2 = st.sidebar.multiselect("FSCODE:", options=fs1)

# If 'All' is selected, show all data; otherwise, filter based on selected sectors
       if all_option_fs in fs2 or len(fs2) == 0:  # If 'All' is selected or nothing is selected
        filtered_data = dataset2
       else:
         filtered_data = dataset2[dataset2["FSCODE"].isin(fs2)]   

##################### 
       all_option_sc = 'All'
       sc1 = [all_option_sc] + list(filtered_data["SCHED_ID"].unique())

# Use multiselect instead of selectbox to allow multiple selections
       sc2 = st.sidebar.multiselect("SCHED_ID", options=sc1)

# If 'All' is selected, show all data; otherwise, filter based on selected sectors
       if all_option_sc in sc2 or len(sc2) == 0:  # If 'All' is selected or nothing is selected
         filtered_data = filtered_data
       else:
          filtered_data = filtered_data[filtered_data["SCHED_ID"].isin(sc2)]  
##################### 
       all_option_r = 'All'
       ROUTE1 = [all_option_r] + list(filtered_data["ROUTE"].unique())

# Use multiselect instead of selectbox to allow multiple selections
       ROUTE2 = st.sidebar.multiselect("ROUTE:", options=ROUTE1)

# If 'All' is selected, show all data; otherwise, filter based on selected sectors
       if all_option_r in ROUTE2 or len(ROUTE2) == 0:  # If 'All' is selected or nothing is selected
         filtered_data = filtered_data
       else:
         filtered_data = filtered_data[filtered_data["ROUTE"].isin(ROUTE2)]   
##################### 
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

####################
       dfn = pd.read_excel('020525_RMS_Raw_Data2.xlsx', sheet_name='Flight Plan Budget')
       #dfn['Start Date'] = dfn['START'].dt.strftime('%d %b %Y')
       #dfn['End Date'] = dfn['END'].dt.strftime('%d %b %Y')

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
    # Logout button
    if st.button("🔓 Logout"):
        st.session_state.logged_in = False
        st.session_state.username = ''
        st.rerun()


