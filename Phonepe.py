import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import pymysql
import plotly.express as px
import sqlite3
import requests
import json
import plotly.graph_objects as go
import plotly.io as pio
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objs as go
from plotly.subplots import make_subplots


mydb = pymysql.connect(
                        user='root',
                        host='127.0.0.1',
                        password="shanmugam",
                        port=3306,
                        database='Phonepe'
                        )

mycursor=mydb.cursor()

query_1="Select * from Agg_insureance"
mycursor.execute(query_1)
data=mycursor.fetchall()
Agg_insureance=pd.DataFrame(data,columns=[i[0]for i in mycursor.description])

# Agg_transacation

query_2="Select * from Agg_transacation"
mycursor.execute(query_2)
data=mycursor.fetchall()
Agg_transacation=pd.DataFrame(data,columns=[i[0]for i in mycursor.description])

# Agg_user

query_3="Select * from Agg_user"
mycursor.execute(query_3)
data=mycursor.fetchall()
Agg_user=pd.DataFrame(data,columns=[i[0]for i in mycursor.description])

# map_Insurance

query_4="Select * from map_Insurance"
mycursor.execute(query_4)
data=mycursor.fetchall()
map_Insurance=pd.DataFrame(data,columns=[i[0]for i in mycursor.description])

# map_trans_list

query_5="Select * from map_trans_list"
mycursor.execute(query_5)
data=mycursor.fetchall()
map_trans_list=pd.DataFrame(data,columns=[i[0]for i in mycursor.description])

# map_user

query_6="Select * from map_user"
mycursor.execute(query_6)
data=mycursor.fetchall()
map_user=pd.DataFrame(data,columns=[i[0]for i in mycursor.description])

# Top_insurance

query_7="Select * from Top_insurance"
mycursor.execute(query_7)
data=mycursor.fetchall()
Top_insurance=pd.DataFrame(data,columns=[i[0]for i in mycursor.description])

# Top_Transacation

query_8="Select * from Top_Transacation"
mycursor.execute(query_8)
data=mycursor.fetchall()
Top_Transacation=pd.DataFrame(data,columns=[i[0]for i in mycursor.description])

# Top_User

query_9="Select * from Top_User"
mycursor.execute(query_9)
data=mycursor.fetchall()
Top_User=pd.DataFrame(data,columns=[i[0]for i in mycursor.description])



def Trasacation_amount_count_Y(df, year):
    TATCY=df [df["years"]==year]
    TATCY.reset_index(drop=True,inplace=True)
    grouped = TATCY.groupby("States")[["Transacationcount", "Transacationamount"]].sum()
    grouped.reset_index(inplace=True)

    # fig_bar_1 = px.bar(TATCY, x="States", y="Transacationcount",
                    #    title=f"{year} States and Transaction Count")
    # st.plotly_chart(fig_bar_1)

    # fig_bar_2 = px.bar(TATCY, x="States", y="Transacationamount",
                    #    title=f"{year} States and Transaction Amount")
    # st.plotly_chart(fig_bar_2)


    url="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
    response=requests.get(url)
    data_1=json.loads(response.content)
    print(data_1)
    states_name=[]
    for feature in data_1["features"]:
        states_name.append(feature["properties"]["ST_NM"])

    states_name.sort()


    ind_chart=px.choropleth(TATCY,geojson=data_1, locations="States", featureidkey="properties.ST_NM",
                                color="Transacationamount",hover_name="States", title= f"{year} Transacationamount",
                                fitbounds= "locations",height=800,width=800,
                                color_continuous_scale="Rainbow",
                                range_color=(TATCY["Transacationamount"].min(), TATCY["Transacationamount"].max()))



    ind_chart.update_geos(visible=False)
    st.plotly_chart(ind_chart)

    ind_chart_2=px.choropleth(TATCY,geojson=data_1, locations="States", featureidkey="properties.ST_NM",
                                color="Transacationcount",hover_name="States", title= f"{year} Transacationcount",
                                fitbounds= "locations",height=800,width=800,
                                color_continuous_scale="Rainbow",
                                range_color=(TATCY["Transacationcount"].min(), TATCY["Transacationcount"].max()))



    ind_chart_2.update_geos(visible=False)
    st.plotly_chart(ind_chart_2)

    # return TATCY





def Transaction_amount_count_quarter(df, year, quarter):

    TATCYq = df[(df["years"] == year) & (df["Quarter"] == quarter)]
    TATCYq.reset_index(drop=True, inplace=True)


    grouped_data = TATCYq.groupby("States")[["Transacationcount", "Transacationamount"]].sum().reset_index()
    grouped_data.reset_index(inplace=True)


    url="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
    response=requests.get(url)
    data_1=json.loads(response.content)
    print(data_1)
    states_name=[]
    for feature in data_1["features"]:
        states_name.append(feature["properties"]["ST_NM"])

    states_name.sort()


    ind_chart=px.choropleth(grouped_data,geojson=data_1, locations="States", featureidkey="properties.ST_NM",
                                color="Transacationamount",hover_name="States", title= f"{year} Transacationamount",
                                fitbounds= "locations",height=800,width=800,
                                color_continuous_scale="Rainbow",
                                range_color=(grouped_data["Transacationamount"].min(), grouped_data["Transacationamount"].max()))



    ind_chart.update_geos(visible=False)
    st.plotly_chart(ind_chart)

    ind_chart_2=px.choropleth(grouped_data,geojson=data_1, locations="States", featureidkey="properties.ST_NM",
                                color="Transacationcount",hover_name="States", title= f"{year} Transacationcount",
                                fitbounds= "locations",height=800,width=800,
                                color_continuous_scale="Rainbow",
                                range_color=(grouped_data["Transacationcount"].min(), grouped_data["Transacationcount"].max()))



    ind_chart_2.update_geos(visible=False)
    st.plotly_chart(ind_chart_2)



# Agg User
def Agg_user_plot(df, year):
    agueyr = df[df["years"] == year]
    agueyr.reset_index(drop=True, inplace=True)

    agueyrg = pd.DataFrame(agueyr.groupby("Brands")["Transacationcount"].sum())
    agueyrg.reset_index(inplace=True)


    fig_1 = px.bar(agueyrg, x="Brands", y="Transacationcount", title="Brands & Transactioncount")
    st.plotly_chart(fig_1)


def Agg_user_plot_qu(df, year, quarter):
    agupq = df[(df["years"] == year) & (df["Quarter"] == quarter)]
    agupq.reset_index(drop=True, inplace=True)

    agupqg = pd.DataFrame(agupq.groupby("Brands")["Transacationcount"].sum()).reset_index()

    fig_bar_2 = px.bar(agupqg, x="Brands", y="Transacationcount",
                       title=f"{year}, Q{quarter} Brands and Transaction Count")

    st.plotly_chart(fig_bar_2)

def map_amount_count_Y(df, year):
    MIY=df [df["years"]==year]
    MIY.reset_index(drop=True,inplace=True)
    grouped_MIY = MIY.groupby("States")[["Transacationcount", "TransacationAmount"]].sum()
    grouped_MIY.reset_index(inplace=True)


    url="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
    response=requests.get(url)
    data_3=json.loads(response.content)
    print(data_3)
    states_name=[]
    for feature in data_3["features"]:
        states_name.append(feature["properties"]["ST_NM"])

    states_name.sort()

    ind_chart_m=px.choropleth(grouped_MIY,geojson=data_3, locations="States", featureidkey="properties.ST_NM",
                                color="TransacationAmount",hover_name="States", title= f"{year} TransacationAmount",
                                fitbounds= "locations",height=1000,width=1000,
                                color_continuous_scale="Rainbow",
                                range_color=(grouped_MIY["TransacationAmount"].min(), grouped_MIY["TransacationAmount"].max()))



    ind_chart_m.update_geos(visible=False)
    st.plotly_chart(ind_chart_m)

    ind_chart_m_2=px.choropleth(grouped_MIY,geojson=data_3, locations="States", featureidkey="properties.ST_NM",
                                color="Transacationcount",hover_name="States", title= f"{year} Transacationcount",
                                fitbounds= "locations",height=800,width=800,
                                color_continuous_scale="Rainbow",
                                range_color=(grouped_MIY["Transacationcount"].min(), grouped_MIY["Transacationcount"].max()))



    ind_chart_m_2.update_geos(visible=False)
    st.plotly_chart(ind_chart_m_2)

    # return grouped_MIY

def map_amount_count_Q(df, year, quarter):
    MIYQ=df [df["years"]==year]
    MIYQ=df [df["Quarter"]==quarter]
    MIYQ.reset_index(drop=True,inplace=True)
    grouped_MIYQ = MIYQ.groupby("States")[["Transacationcount", "TransacationAmount"]].sum()
    grouped_MIYQ.reset_index(inplace=True)


    url="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
    response=requests.get(url)
    data_4=json.loads(response.content)
    print(data_4)

    states_name=[]
    for feature in data_4["features"]:
        states_name.append(feature["properties"]["ST_NM"])

    states_name.sort()

    ind_chart_q=px.choropleth(grouped_MIYQ,geojson=data_4, locations="States", featureidkey="properties.ST_NM",
                                color="TransacationAmount",hover_name="States", title= f"{year, quarter} TransacationAmount",
                                fitbounds= "locations",height=800,width=800,
                                color_continuous_scale="Rainbow",
                                range_color=(grouped_MIYQ["TransacationAmount"].min(), grouped_MIYQ["TransacationAmount"].max()))



    ind_chart_q.update_geos(visible=False)
    st.plotly_chart(ind_chart_q)

    ind_chart_q_2=px.choropleth(grouped_MIYQ,geojson=data_4, locations="States", featureidkey="properties.ST_NM",
                                color="Transacationcount",hover_name="States", title= f"{year, quarter,} Transacationcount",
                                fitbounds= "locations",height=800,width=800,
                                color_continuous_scale="Rainbow",
                                range_color=(grouped_MIYQ["Transacationcount"].min(), grouped_MIYQ["Transacationcount"].max()))



    ind_chart_q_2.update_geos(visible=False)
    st.plotly_chart(ind_chart_q_2)





def map_user_year(df, year):
    MUY = df[df["years"] == year]
    MUY.reset_index(drop=True, inplace=True)

    MUYg = pd.DataFrame(MUY.groupby("States")[["Register_user","App_opens"]].sum())
    MUYg.reset_index(inplace=True)

    fig_line=px.line(MUYg, x="States", y=["Register_user", "App_opens"], title=f"{year} Registeruser APPOpens", width=1000, height=800,markers=True)
    st.plotly_chart(fig_line)

    # return MUY

def map_user_Quarter(df,year,quarter):
    MUYq = df[df["years"] == year]
    MUYq = df[df["Quarter"] == quarter]
    MUYq.reset_index(drop=True, inplace=True)

    MUYgq = pd.DataFrame(MUYq.groupby("States")[["Register_user","App_opens"]].sum())
    MUYgq.reset_index(inplace=True)

    fig_line_2=px.line(MUYgq, x="States", y=["Register_user", "App_opens"], title=f"{quarter} Registeruser APPOpens", width=1000, height=800,markers=True)
    st.plotly_chart(fig_line_2)

def top_amount_count_Y(df, year):
    TIY=df [df["years"]==year]
    TIY.reset_index(drop=True,inplace=True)
    grouped_TIY = TIY.groupby("States")[["count", "Amount"]].sum()
    grouped_TIY.reset_index(inplace=True)



    url="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
    response=requests.get(url)
    data_5=json.loads(response.content)
    print(data_5)
    states_name=[]
    for feature in data_5["features"]:
        states_name.append(feature["properties"]["ST_NM"])

    states_name.sort()

    ind_chart_t=px.choropleth(grouped_TIY,geojson=data_5, locations="States", featureidkey="properties.ST_NM",
                                color="Amount",hover_name="States", title= f"{year} TransactionAmount",
                                fitbounds= "locations",height=800,width=800,
                                color_continuous_scale="Rainbow",
                                range_color=(grouped_TIY["Amount"].min(), grouped_TIY["Amount"].max()))



    ind_chart_t.update_geos(visible=False)
    st.plotly_chart(ind_chart_t)


    ind_chart_t_2=px.choropleth(grouped_TIY,geojson=data_5, locations="States", featureidkey="properties.ST_NM",
                                color="count",hover_name="States", title= f"{year} Transacationcount",
                                fitbounds= "locations",height=800,width=800,
                                color_continuous_scale="Rainbow",
                                range_color=(grouped_TIY["count"].min(), grouped_TIY["count"].max()))



    ind_chart_t_2.update_geos(visible=False)
    st.plotly_chart(ind_chart_t_2)

def top_amount_count_Y_amount_count_quarter(df, year, quarter):
    TATCYq=df [df["years"]==year]
    TATCYq=df [df["Quarter"]==quarter]
    TATCYq.reset_index(drop=True,inplace=True)
    grouped_top = TATCYq.groupby("States")[["count", "Amount"]].sum()
    grouped_top.reset_index(inplace=True)




    url="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
    response=requests.get(url)
    data_6=json.loads(response.content)
    print(data_6)
    states_name=[]
    for feature in data_6["features"]:
        states_name.append(feature["properties"]["ST_NM"])

    states_name.sort()

    ind_chart_tq=px.choropleth(grouped_top,geojson=data_6, locations="States", featureidkey="properties.ST_NM",
                                color="Amount",hover_name="States", title= f"{year, quarter} Amount",
                                fitbounds= "locations",height=800,width=800,
                                color_continuous_scale="Rainbow",
                                range_color=(grouped_top["Amount"].min(), grouped_top["Amount"].max()))



    ind_chart_tq.update_geos(visible=False)
    st.plotly_chart(ind_chart_tq)

    ind_chart_tq_2=px.choropleth(grouped_top,geojson=data_6, locations="States", featureidkey="properties.ST_NM",
                                color="count",hover_name="States", title= f"{year, quarter,} count",
                                fitbounds= "locations",height=800,width=800,
                                color_continuous_scale="Rainbow",
                                range_color=(grouped_top["count"].min(), grouped_top["count"].max()))



    ind_chart_tq_2.update_geos(visible=False)
    st.plotly_chart(ind_chart_tq_2)

def Top_User_y(df, year):

    TUY = Top_User[Top_User["years"] == year]
    TUY.reset_index(drop=True, inplace=True)


    TUYg = pd.DataFrame(TUY.groupby(["States"])["Register_user"].sum())
    TUYg.reset_index(inplace=True)


    PXbar_plot_TU=px.bar(TUYg, x="States", y=["Register_user"], title=f"{year} Registeruser", width=1000, height=1000,hover_name="States")
    st.plotly_chart(PXbar_plot_TU)

def Top_User_y_Q(df, year,Quarter):

    TUYq = Top_User[Top_User["years"] == year]
    TUYq = df[df["Quarter"] == Quarter]
    TUYq.reset_index(drop=True, inplace=True)


    TUYqg = pd.DataFrame(TUYq.groupby(["States","Quarter"])["Register_user"].sum())
    TUYqg.reset_index(inplace=True)


    PXbar_plot_TUQ=px.bar(TUYqg, x="States", y=["Register_user"], title=f"{year,Quarter} Registeruser",color="Quarter", width=1000, height=1000,hover_name="States")
    st.plotly_chart(PXbar_plot_TUQ)

def Top_10_Transacation_amount_Insurance(table_name):

    mydb = pymysql.connect(
                            user='root',
                            host='127.0.0.1',
                            password="shanmugam",
                            port=3306,
                            database='Phonepe'
                            )

    mycursor=mydb.cursor()

    query= f"""Select States, sum(Transacationamount) as Trasacationamount
    from {table_name}
    group by States
    order by Trasacationamount desc
    limit 10"""

    mycursor.execute(query)
    table=mycursor.fetchall()
    mydb.commit()

    df=pd.DataFrame(table,columns=["States", "Transactionamount"])


    fig_1 = px.bar(df, x="States", y="Transactionamount", title="States & TransactionAmount")

    st.plotly_chart(fig_1)

def Agg_Top_Transacationcount(table_name):

    mydb = pymysql.connect(
                            user='root',
                            host='127.0.0.1',
                            password="shanmugam",
                            port=3306,
                            database='Phonepe'
                            )

    mycursor=mydb.cursor()


    query_least= f"""Select States, sum(Transacationcount) as Transacationcount
                from {table_name}
                group by States
                order by Transacationcount desc
                limit 10"""

    mycursor.execute(query_least)
    table_1=mycursor.fetchall()
    mydb.commit()

    df_1=pd.DataFrame(table_1,columns=["States", "Transacationcount"])


    fig_2 = px.bar(df_1, x="States", y="Transacationcount", title=" top 10 Transactioncount & States")

    st.plotly_chart(fig_2)

def Avg_Transacation_Amount(table_name):

    mydb = pymysql.connect(
                            user='root',
                            host='127.0.0.1',
                            password="shanmugam",
                            port=3306,
                            database='Phonepe'
                            )

    mycursor=mydb.cursor()


    query_Avg= f"""Select States, avg(Transacationamount) as Trasacationamount
                from {table_name}
                group by States
                order by Trasacationamount"""

    mycursor.execute(query_Avg)
    table_2=mycursor.fetchall()
    mydb.commit()

    df_2=pd.DataFrame(table_2,columns=["States", "Transactionamount"])


    fig_3 = px.bar(df_2, x="States", y="Transactionamount", title="States & AVG TransactionAmount")

    st.plotly_chart(fig_3)

def map_Top_Transacation_Amount(table_name):

    mydb = pymysql.connect(
                            user='root',
                            host='127.0.0.1',
                            password="shanmugam",
                            port=3306,
                            database='Phonepe'
                            )

    mycursor=mydb.cursor()

    query_top= f"""Select States, sum(TransacationAmount) as TransacationAmount
    from {table_name}
    group by States
    order by TransacationAmount desc
    limit 10"""

    mycursor.execute(query_top)
    table=mycursor.fetchall()
    mydb.commit()

    df=pd.DataFrame(table,columns=["States", "TransacationAmount"])


    fig_1 = px.bar(df, x="States", y="TransacationAmount", title="Top 10 States & TransactionAmount")

    st.plotly_chart(fig_1)

def Top_Avg_Transacation_Amount(table_name):

    mydb = pymysql.connect(
                            user='root',
                            host='127.0.0.1',
                            password="shanmugam",
                            port=3306,
                            database='Phonepe'
                            )

    mycursor=mydb.cursor()


    query_Avg= f"""Select States, avg(Amount) as Trasacationamount
                from {table_name}
                group by States
                order by Trasacationamount"""

    mycursor.execute(query_Avg)
    table_2=mycursor.fetchall()
    mydb.commit()

    df_2=pd.DataFrame(table_2,columns=["States", "Amount"])


    fig_3 = px.bar(df_2, x="States", y="Amount", title="States & AVG TransactionAmount")

    st.plotly_chart(fig_3)

def map_Top_Transacation_count(table_name):

    mydb = pymysql.connect(
                            user='root',
                            host='127.0.0.1',
                            password="shanmugam",
                            port=3306,
                            database='Phonepe'
                            )

    mycursor=mydb.cursor()

    query_top= f"""Select States, sum(Transacationcount) as Transacationcount
    from {table_name}
    group by States
    order by Transacationcount desc
    limit 10"""

    mycursor.execute(query_top)
    table=mycursor.fetchall()
    mydb.commit()

    df=pd.DataFrame(table,columns=["States", "Transacationcount"])


    fig_1 = px.bar(df, x="States", y="Transacationcount", title="Top 10 States & Transaction Count")

    st.plotly_chart(fig_1)

def least_Transacation_Count(table_name):

    mydb = pymysql.connect(
                            user='root',
                            host='127.0.0.1',
                            password="shanmugam",
                            port=3306,
                            database='Phonepe'
                            )

    mycursor=mydb.cursor()


    query_least= f"""Select States, sum(count) as Transacationcount
                from {table_name}
                group by States
                order by Transacationcount
                limit 10"""

    mycursor.execute(query_least)
    table_2=mycursor.fetchall()
    mydb.commit()

    df_2=pd.DataFrame(table_2,columns=["States", "count"])


    fig_3 = px.bar(df_2, x="States", y="count", title="States & Top TransactionCount")

    st.plotly_chart(fig_3)




# streamlit part

st.set_page_config(layout='wide')
st.title("Phonepe Pulse Data Visualization and Exploration")

with st.sidebar:
     selected = option_menu(
            "Main Menu",
            ["Home", "Yearly Data","Quarter Data","Analysis"],
            icons=["house", "calendar","table","question"])

if selected=="Home":
    st.header("Welcome to the Phonepe Pulse Dashboard")

elif selected =="Yearly Data":
    column_1, column_2, column_3 = st.tabs(["Agg_Analysis", "Map_Analysis", "Top_Analysis"])

    with column_1:
        method = st.radio("select the data",["Agg Insurane Analysis","Agg Transacation Analysis","Agg User Analysis"])
        # st.write(method)
        if method == "Agg Insurane Analysis":

            unique_years = Agg_insureance["years"].unique()
            year = st.slider("Select Year AI", int(unique_years.min()), int(unique_years.max()))
            Agg_Insurance_y= Trasacation_amount_count_Y (Agg_insureance, year)


        elif method == "Agg Transacation Analysis":

            unique_years = Agg_transacation["years"].unique()
            year = st.slider("Select Year AT", int(unique_years.min()), int(unique_years.max()))
            Trasacation_amount_count_Y(Agg_transacation, year)

        elif method == "Agg User Analysis":

            unique_years = Agg_user["years"].unique()
            year = st.selectbox("Select Year AT", unique_years)
            Agg_user_plot(Agg_user, year)

    with column_2:
        method_2=st.radio("select the data",["Map Insurance","Map Transacation","Map user"])
        st.write(method_2)
        if method_2 == "Map Insurance":
            unique_years = map_Insurance["years"].unique()
            year = st.slider("Select Year", int(unique_years.min()), int(unique_years.max()))
            map_amount_count_Y(map_Insurance, year)

        elif method_2 == "Map Transacation":

            unique_years = map_trans_list["years"].unique()
            year = st.slider("Select Year MT", int(unique_years.min()), int(unique_years.max()))
            map_amount_count_Y(map_trans_list, year)

        elif method_2 == "Map user":
            unique_years = map_user["years"].unique()
            year = st.slider("Select Year MU", int(unique_years.min()), int(unique_years.max()))
            map_user_year(map_user, year)

    with column_3:
        method_3=st.radio("select the data",["Top Insurance","Top Transacation","Top user"])

        if method_3 == "Top Insurance":
            unique_years = Top_insurance["years"].unique()
            year = st.slider("Select Year TI", int(unique_years.min()), int(unique_years.max()))
            top_amount_count_Y(Top_insurance, year)

        elif method_3 == "Top Transacation":
            unique_years = Top_Transacation["years"].unique()
            year = st.slider("Select Year", int(unique_years.min()), int(unique_years.max()))
            top_amount_count_Y(Top_Transacation, year)

        elif method_3 == "Top user":
            unique_years = Top_User["years"].unique()
            year = st.slider("Select Year", int(unique_years.min()), int(unique_years.max()))
            Top_User_y(Top_User, year)

elif selected =="Quarter Data":
    column_1, column_2, column_3 = st.tabs(["Agg_Analysis","Map_Analysis","Top_Analysis"])

    with column_1:
        method = st.radio("select the data",["Agg Insurane Analysis","Agg Transacation Analysis","Agg User Analysis"])

        if method == "Agg Insurane Analysis":
            unique_years = Agg_insureance["years"].unique()
            year = st.slider("Select Year QAI", int(Agg_insureance["years"].min()), int(Agg_insureance["years"].max()))
            quarter = st.selectbox("Select Quarter", [1, 2, 3, 4])
            Transaction_amount_count_quarter(Agg_insureance, year, quarter)

        elif method == "Agg Transacation Analysis":
            unique_years = Agg_transacation["years"].unique()
            year = st.slider("Select Year QAT", int(unique_years.min()), int(unique_years.max()))
            quarter = st.selectbox("Select Quarter", [1, 2, 3, 4])
            Transaction_amount_count_quarter(Agg_transacation, year, quarter)

        elif method == "Agg User Analysis":
            unique_years = Agg_user["years"].unique()
            year = st.slider("Select Year QAU", int(unique_years.min()), int(unique_years.max()))
            quarter = st.selectbox("Select Quarter", [1, 2, 3, 4])
            Agg_user_plot_qu(Agg_user, year, quarter)


    with column_2:
        method_2=st.radio("select the data",["Map Insurance","Map Transacation","Map user"])

        if method_2 == "Map Insurance":
            unique_years = map_Insurance["years"].unique()
            year = st.slider("Select Year QMI", int(map_Insurance["years"].min()), int(map_Insurance["years"].max()))
            quarter = st.slider("Select Quarter MI", 1, 4)
            map_amount_count_Q(map_Insurance, year, quarter)

        elif method_2 == "Map Transacation":
            unique_years = map_trans_list["years"].unique()
            year = st.slider("Select Year QMI", int(map_trans_list["years"].min()), int(map_trans_list["years"].max()))
            quarter = st.slider("Select Quarter MT", 1, 4)
            map_amount_count_Q(map_trans_list, year, quarter)

        elif method_2 == "Map user":
            unique_years = map_user["years"].unique()
            year = st.slider("Select Year QMT", int(map_user["years"].min()), int(map_user["years"].max()))
            quarter = st.selectbox("Select Quarter MU", [1,2,3,4])
            map_user_Quarter(map_user, year, quarter)

    with column_3:
        method_3=st.radio("select the data",["Top Insurance", "Top Transacation", "Top user"])

        if method_3 == "Top Insurance":
            unique_years = Top_insurance["years"].unique()
            year = st.slider("Select Year TI", int(Top_insurance["years"].min()), int(Top_insurance["years"].max()))
            quarter = st.slider("Select Quarter", 1, 4)
            top_amount_count_Y_amount_count_quarter(Top_insurance, year, quarter)

        elif method_3 == "Top Transacation":
            unique_years = Top_Transacation["years"].unique()
            year = st.slider("Select Year TT", int(Top_Transacation["years"].min()), int(Top_Transacation["years"].max()))
            quarter = st.slider("Select Quarter TTQ", 1, 4)
            top_amount_count_Y_amount_count_quarter(Top_Transacation, year, quarter)

        elif method_3 == "Top user":
            unique_years = Top_User["years"].unique()
            year = st.slider("Select Year TU", int(Top_User["years"].min()), int(Top_User["years"].max()))
            Quarter = st.slider("Select Quarter", 1, 4)
            Top_User_y_Q(Top_User, year, Quarter)

elif selected=="Analysis":

    analysis_choice = st.selectbox("Select the Questions",["1.Top 10 States of Transaction Amount for Agg Insurance",
                                                        "2.Top 10 States of Transaction count for Agg Insurance",
                                                        "3.Avg Transaction Amount of States for Agg Insurance",
                                                        "4.Avg Transaction Amount of States for Agg Transacation",
                                                        "5.Top 10 States of Transaction Amount for Agg Transacation",
                                                        "6.Top 10 States of Transaction Amount for Map Insurance",
                                                        "7.Top 10 States of Transaction Amount for Map Transacation",
                                                        "8.Avg Transaction Amount of States for Top Transacation",
                                                        "9.Top 10 States of Transaction Count for Map Insurance",
                                                        "10.Least 10 States of Transaction Count for Top_Transacation"])

    if analysis_choice == "1.Top 10 States of Transaction Amount for Agg Insurance":
        table_name = "Agg_insureance"
        Top_10_Transacation_amount_Insurance(table_name)

    elif analysis_choice == "2.Top 10 States of Transaction count for Agg Insurance":
        table_name = "Agg_insureance"
        Agg_Top_Transacationcount(table_name)

    elif analysis_choice == "3.Avg Transaction Amount of States for Agg Insurance":
        table_name = "Agg_insureance"
        Avg_Transacation_Amount(table_name)

    elif analysis_choice == "4.Avg Transaction Amount of States for Agg Transacation":
        table_name = "Agg_transacation"
        Avg_Transacation_Amount(table_name)

    elif analysis_choice == "5.Top 10 States of Transaction Amount for Agg Transacation":
        table_name = "Agg_transacation"
        Top_10_Transacation_amount_Insurance(table_name)

    elif analysis_choice == "6.Top 10 States of Transaction Amount for Map Insurance":
        table_name = "map_Insurance"
        map_Top_Transacation_Amount(table_name)

    elif analysis_choice == "7.Top 10 States of Transaction Amount for Map Transacation":
        table_name = "map_trans_list"
        map_Top_Transacation_Amount(table_name)

    elif analysis_choice == "8.Avg Transaction Amount of States for Top Transacation":
        table_name = "Top_Transacation"
        Top_Avg_Transacation_Amount(table_name)

    elif analysis_choice == "9.Top 10 States of Transaction Count for Map Insurance":
        table_name = "map_Insurance"
        map_Top_Transacation_count(table_name)

    elif analysis_choice == "10.Least 10 States of Transaction Count for Top_Transacation":
        table_name = "Top_Transacation"
        least_Transacation_Count(table_name)
