import random
import csv
from datetime import datetime, timedelta

# Initialize lists to store the data for each column
column1 = []
column2 = []
date_values = []

# Define the start date
start_date = datetime(2022, 1, 1)

# Generate random data for 365 iterations
for _ in range(365):
    # Generate a random value for column 1 between 50 and 90
    notifications_sent = random.randint(1200, 2000)

    # Calculate a corresponding value for column 2 between 80% and 90% of column 1
    corresponding_value = round(notifications_sent * random.uniform(0.55, 0.9))

    # Append the values to their respective columns
    column1.append(notifications_sent)
    column2.append(corresponding_value)

    # Add date to the date_values list
    date_values.append(start_date.strftime("%Y-%m-%d"))

    # Increment the date for the next iteration
    start_date += timedelta(days=1)

# Write the data to a CSV file
with open('customer_engagement.csv', mode='w', newline='') as csv_file:
    writer = csv.writer(csv_file)

    # Write the header row
    writer.writerow(['Date', 'UserNotification', 'AppOpen'])

    # Write the data rows
    for date, c1, c2 in zip(date_values, column1, column2):
        writer.writerow([date, c1, c2])

print("Data has been saved to 'customer_engagement.csv'.")
