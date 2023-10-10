import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path
import duckdb
import altair as alt
from wordcloud import WordCloud
import matplotlib.pyplot as plt

st.set_page_config(page_title="Customer Engagement/ Sentiment", page_icon="📈", layout="wide")

# Establish Duck db connection
connection = duckdb.connect()

# Create customer_engagement data set CSV file path/ directory object
dir_path = Path('data/customer_engagement.csv')
df = pd.read_csv(dir_path)

review_dir_path = Path('data/review_comments_and_ratings.csv')
rdf = pd.read_csv(review_dir_path)

# Create a DuckDB table from the DataFrame
connection.register('customer_engagement', df)
connection.register('review_comments_and_ratings', rdf)

# Dashboards
st.title("Customer Engagement/ Sentiment ")

# Daily Click Through
st.sidebar.caption("Click-through Rate")
st.subheader("Click-through Rate")

daily_click_through_data = connection.execute('SELECT "Date", "User-Notification", "App-Open" FROM customer_engagement').fetchdf()
a = alt.Chart(daily_click_through_data).mark_line().interactive().encode(
    x="Date", y="User-Notification")
b = alt.Chart(daily_click_through_data).mark_area(color="#ff5f49").interactive().encode(
    x="Date", y="App-Open")

c = alt.layer(a, b)
st.altair_chart(c.interactive(), use_container_width=True)

# Engagement graph
st.sidebar.caption("Engagement Graph (DAU)")
st.subheader("Engagement Graph (DAU)")

engagement_sql_query = """
SELECT 100,
    "Date",
    "User-Notification",
    CASE
        WHEN "User-Notification" = 0 THEN 0
        ELSE ("App-Open" * 100.0) / "User-Notification"
    END AS "Click-through-percentage"
FROM
    customer_engagement
"""
engagement_graph = connection.execute(engagement_sql_query).fetchdf()
a = alt.Chart(engagement_graph).mark_line().interactive().encode(
    x="Date", y='100')
b = alt.Chart(engagement_graph).mark_area(color="#ff5f49").interactive().encode(
    x="Date", y="Click-through-percentage")

d = alt.layer(a, b)
st.altair_chart(d.interactive(), use_container_width=True)


# Survey
st.sidebar.caption("Survey response")
st.subheader("Survey response")
st.divider()
st.markdown(''' 
    **Question:** Thank you for using our App. Will you promote our App to your friends and Family ?  

    Options:  
    > **A. Yes, I already did**  
    > **B. Maybe**   
    > **C. Yes, if I get extra points to for referral**   
    > **D. No, I don't find it useful**''')
st.divider()
Results = {"A. Yes, I already did": 30, "B. Maybe": 2, "C. Yes, if I get extra points to for referral": 8, "D. No, I don't find it useful": 10}
fig1 = px.pie(names=Results.keys(), values=Results.values())
st.plotly_chart(fig1)

# Word Cloud
st.sidebar.caption("Word Cloud")
st.subheader("Word Cloud")

review_comments = connection.execute('SELECT "Review" FROM review_comments_and_ratings').fetchdf().to_string()
wc = WordCloud().generate(review_comments)
plt.imshow(wc)
plt.axis('off')
st.pyplot(plt)