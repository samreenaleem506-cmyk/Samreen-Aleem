import streamlit as st # stremlit is a front-end web framwork of python

import pandas as pd # pandas is a data manipulation library of python.
import plotly.express as px # plotly is a dynamic visualization library of python.
from streamlit_option_menu import option_menu # for the purpose of navigator bar into the web.


st.cache_data.clear()
st.set_page_config(layout="wide") 
st.title("Cric Info App")

df=pd.read_csv("new_data.csv") # reading the data from csv file.

#st.dataframe(df) # displaying the data in the web app.

select= option_menu(
    menu_title=None,
    options=["Home","Player Analysis","Country Insights","Comparison","Data Explorer","About"],
    icons=["house","person","globe","bar-chart-line","table","info-circle"],
    orientation="horizontal",
)


##___________________________________Home______________________________


if select=="Home":
    st.title("Cricket Analysis Dashboard")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Players", df["player"].nunique())

    col2.metric("Total Runs", df["Runs"].sum())

    col3.metric("Countries", df["country"].nunique())

    col4.metric("Total Matches", df["matches"].sum())

    st.dataframe(df.head(10))

#------------------Player Analysis----------------------------

elif select=="Player Analysis":
    st.title("Player Analysis Stats")

    player = st.selectbox("Select Player", df["player"].unique())

    pdata = df[df["player"]==player]

    df2=pdata[["matches","Inns","high_score","avg","100","50","4s","6s"]]
    df3=df2.T.reset_index()
    st.dataframe(df3)

    fig = px.bar(df3, x="index", y=df3.columns[1], color="index", text=df3.columns[1], title=f"Player Analysis of {player}")
    
    
    df_pie=pdata[["100","50","4s","6s"]]
    pie1=df_pie.T.reset_index()
    fig_pie = px.pie(pie1, names="index", values=pie1.columns[1])
    
    col1, col2 = st.columns(2)

    with col1:
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        st.plotly_chart(fig_pie, use_container_width=True)

#------------------Country Insights----------------------------

elif select=="Country Insights":
    st.title("Country wise Cricket Analysis")

    scountry=st.selectbox("Select Country", df["country"].unique())
    
    col1, col2, col3, col4 = st.columns(4)
    
    cdata=df[df["country"]==scountry]

    player=cdata["player"].unique()
    total_runs=cdata["Runs"].sum()
    total_matches=cdata["matches"].sum()
    total_innings=cdata["Inns"].sum()

    col1.metric("total player", len(player))

    col2.metric("total runs", total_runs)

    col3.metric("total matches", total_matches)
    
    col4.metric("total innings", total_innings)

    df2 = cdata[["player","Runs"]]

    df3=cdata[["player","Runs","matches","100","6s"]]
    
    df4 =["Runs","matches","100","6s"]
    fig=px.pie(df2,names="player",values="Runs")

    selectc=st.selectbox("Select choice",df4)

    fig2=px.bar(df3,x="player",y=selectc,color="player")

    st.plotly_chart(fig2,use_container_width=True)



#---------------------Comparison----------------------------


elif select=="Comparison":

    st.title("Player Comparison")

    players = st.multiselect("compare players", df["player"], default=df["player"].head(3))

    compare = df[df["player"].isin(players)]

    fig=px.scatter(compare,x="strike_rate",y="avg",color="player",size="Runs",hover_data=["player","country"])

    st.plotly_chart(fig,use_container_width=True)

elif select=="Data Explorer":
    
    st.title("Data Exploration")

    st.dataframe(df)

elif select=="About":
    st.info("About this project")

    st.text("Project by: Hira Sulaiman")

    st.success("End to end streamlit Data analysis Dashboard using Python for Cricket Analysis ")

    url1 = "https://www.linkedin.com/in/hira-sulaiman-21181b29/"   
    st.markdown(f"[LinkedIn Profile]({url1})")

    url2 = "https://github.com/HiraSulaiman06"
    st.markdown(f"[GitHub Profile]({url2})")


