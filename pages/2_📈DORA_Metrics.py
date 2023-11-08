import streamlit as st
import csv
import random
from datetime import datetime, timedelta
import pandas as pd
import matplotlib.pyplot as plt

# Define the default start and end dates for the last 2 years
end_date = datetime.now()
start_date = end_date - timedelta(days=730)  # 2 years

# Define the teams
teams = ["Team A", "Team B", "Team C"]

# Create a Streamlit app
st.title("DORA Metrics")

# Create and open the CSV file for writing
with st.spinner('Generating data...'):
    with open('dora_metrics.csv', mode='w', newline='') as file:
        fieldnames = ['Date', 'Team', 'DeploymentFrequency', 'LeadTime', 'ChangeFailureRate', 'MTTR']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        # Write the header row
        writer.writeheader()

        # Generate and write data for each month in the date range
        current_date = start_date
        data = []

        while current_date <= end_date:
            for team in teams:
                deployment_frequency = random.randint(1, 30)
                lead_time = round(random.uniform(1, 30), 1)
                change_failure_rate = round(random.uniform(1, 10), 1)
                mttr = round(random.uniform(1.0, 7), 1)

                data.append({
                    'Date': current_date.strftime('%Y-%m-%d'),
                    'Team': team,
                    'DeploymentFrequency': deployment_frequency,
                    'LeadTime': lead_time,
                    'ChangeFailureRate': change_failure_rate,
                    'MTTR': mttr
                })

            current_date = current_date + timedelta(days=30)  # Assuming 30 days in a month

        writer.writerows(data)


df = pd.read_csv('dora_metrics.csv')

st.write(df)

# # Create a team-based filter
selected_team = st.selectbox("Select a team", teams)

# Filter data based on the selected team
if 'df' in locals():
    if selected_team != "All Teams":
        df_filtered = df[df['Team'] == selected_team]
        st.write(f"## Data for {selected_team}")
        st.write(df_filtered)
    else:
        st.write("## Data for All Teams")
        st.write(df)

# Calculate overall data for the last month and change from the previous month
last_month = df['Date'].max()
previous_month = (datetime.strptime(last_month, '%Y-%m-%d') - timedelta(days=30)).strftime('%Y-%m-%d')
overall_data_last_month = df[df['Date'] == last_month].mean()
overall_data_previous_month = df[df['Date'] == previous_month].mean()
change_data = (overall_data_last_month - overall_data_previous_month) / overall_data_previous_month * 100

st.write("## Overall Data for the Last Month")
st.write(overall_data_last_month)

st.write("## Change from Previous Month")
st.write(change_data)

st.metric(label="Deployment Frequency",
          value=f"{overall_data_last_month['DeploymentFrequency']:.2f}",
          delta=f"{change_data['DeploymentFrequency']:.2f}")
st.metric(label="Lead Time",
          value=f"{overall_data_last_month['LeadTime']:.2f}",
          delta=f"{change_data['LeadTime']:.2f}")
st.metric(label="Change Failure Rate",
          value=f"{overall_data_last_month['ChangeFailureRate']:.2f}%",
          delta=f"{change_data['ChangeFailureRate']:.2f}%")
st.metric(label="MTTR",
          value=f"{overall_data_last_month['MTTR']:.2f}",
          delta=f"{change_data['MTTR']:.2f}")

# Create charts and graphs
if 'df' in locals():

    # Deployment Frequency Chart
    st.subheader("Deployment Frequency")
    for name, group in df.groupby('Team'):
        plt.plot(group['Date'], group['DeploymentFrequency'], label=name)
    plt.xlabel("Date")
    plt.ylabel("Deployment Frequency")
    plt.legend()
    st.pyplot()

    # Lead Time Chart
    st.subheader("Lead Time ")
    for name, group in df.groupby('Team'):
        plt.plot(group['Date'], group['LeadTime'], label=name)
    plt.xlabel("Date")
    plt.ylabel("Lead Time")
    plt.legend()
    st.pyplot()

    # Change Failure Rate Chart
    st.subheader("Change Failure Rate")
    for name, group in df.groupby('Team'):
        plt.plot(group['Date'], group['ChangeFailureRate'], label=name)
    plt.xlabel("Date")
    plt.ylabel("Change Failure Rate (%)")
    plt.legend()
    st.pyplot()

    # MTTR Chart
    st.subheader("MTTR")
    for name, group in df.groupby('Team'):
        plt.plot(group['Date'], group['MTTR'], label=name)
    plt.xlabel("Date")
    plt.ylabel("MTTR")
    plt.legend()
    st.pyplot()
