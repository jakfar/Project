import pandas as pd

# Load the CSV, skipping metadata lines before the actual data
df = pd.read_csv('smhi-opendata_1_98230_202301_202412.csv', sep=';', skiprows=9)

# Combine 'Datum' and 'Tid (UTC)' into a datetime column
df['Datetime'] = pd.to_datetime(df['Datum'] + ' ' + df['Tid (UTC)'])

# Keep and rename relevant columns
df = df[['Datetime', 'Lufttemperatur']].copy()
df.columns = ['Datetime', 'Temperature_C']

# Convert temperature to numeric
df['Temperature_C'] = pd.to_numeric(df['Temperature_C'], errors='coerce')

# Extract time from datetime
df['Time'] = df['Datetime'].dt.time

# Optional: display the result
print(df.head())
