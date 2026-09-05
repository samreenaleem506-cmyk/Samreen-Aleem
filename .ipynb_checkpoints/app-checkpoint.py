import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu
st.set_page_config(layout="wide")
st.title("cricinfo.csv")

df=pd.read_csv("new_data.csv")

st.dataframe(df.head(10))


select=option_menu(
    menu_title= "Cricket Analysis",options=["Home", "Players Analysis", "Country insights", "Comparison" , "Data Explorer" , "About"],
        orientation="horizontal",
        icons=["House" , "Person" , "Globe", "Bar Chat" , "Table" , "Line"])
    
    



    ##_________________Home_____________
if select=="Home":
    st.title("Cricket Analysis Dashboard")
    col1,col2,col3,col4 = st.columns(4)
    col1.metric("Total Players", df["player"].nunique())
    col2.metric("Total Runs", df["runs"].sum())
    col3.metric("Total Countries", df["country"].nunique())
    col4.metric("Total Matches", df["matches"].sum())
    st.dataframe(df.head(10))

elif select == "Players Analysis":
    st.title("Player Analysis Stats")
    player = st.selectbox("select player" , df["player"].unique())
    p_data = df[df["player"]==player]
    df2 = p_data[["matches" , "innings" , "high_score" , "average" , "100" , "50" , "4s" , "6s"]]
    st.dataframe(df2)
    df3 = df2.T.reset_index()
    st.dataframe(df3)

    fig = px.bar (df3, x="index", y=df3.columns[1])
    st.plotly_chart (fig, use_container_width=True)

    df_pie = p_data [["100", "50", "4s", "6s"]]
    pie1 = df_pie.T.reset_index()
    fig_pie = px.pie (pie1, names="index", values= pie1.columns[1])
    

    col1,col2=st.columns(2)

    with col1:
        st.plotly_chart (fig, width="stretch")

    with col2:
        st.plotly_chart (fig_pie, width="stretch")

elif select == "Country insights":
    st.title ("Country Wise Cricket Analysis")
    scountry = st.selectbox("Select Country" , df["country"].unique())
    col1,col2,col3,col4=st.columns(4)

    c_data = df[df["country"] == scountry]
    players = c_data["player"].nunique()
    total_runs = c_data["runs"].sum()
    total_innings = c_data["innings"].sum()
    total_matches = c_data["matches"].sum()
    col1.metric("Total Players" , players)
    col2.metric("Total Runs" , total_runs)  
    col3.metric("Total Innings" , total_innings)
    col4.metric("Total Matches" , total_matches)

    df2 = c_data[["player" , "runs"]]
    df3 = c_data[["player" , "runs" , "matches" , "100" , "6s"]]
    df4 = ["runs" , "matches" , "100" , "6s"]

    fig = px.pie (df2 , names="player" , values="runs")

    selectc = st.selection ("select choice" , df4)

    fig2 = px.bar (df3 , x="player" , y=selectc , color = "player")
    st.plotly_chart (fig2 , use_container_width=True)



#_________________Player comparison____________________#


elif select == "Comparison":

    st.title("Player Analysis")

    players = st.multiselect("compare players" , df["Player"] , default = df["Player"].head(5))

    compare = df [df["player"] . isin(players)]

    fig = px.scatter(compare , x="Strike_Rate" , y="Average" , size = "runs" , colour = "player" , hover_name = "Player")

    st.plotly_chart(fig , use_container_width=True)

elif select == "Data Explorer":

    st.title("Data Explorer")
    st.dataframe(df)

elif select == "About":

    st.info("About this App")
    st.text("This app is a cricket analysis dashboard that provides insights into player and country performance based on cricket statistics. It allows users to explore data, compare players, and visualize key metrics.")
    st.sucess("End to end streamlit data analysis dashboard using python for cricket analysis")

url1 = "https://www.linkedin.com/in/samreen-aleem-107408377/"

url2 = "https://github.com/samreenaleem506-cmyk/"

col1,col2,col3,col4 = st.columns(4)


with col1:
    st.link_button("LinkedIn", url1)

with col2:
    st.link_button("GitHub", url2)
    