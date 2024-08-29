import pandas as pd

# Load the data
data = pd.read_csv('data/raw/media_data.csv')

# Data cleaning and preprocessing
data['Date'] = pd.to_datetime(data['Date'])
data.dropna(inplace=True)

# Save processed data
data.to_csv('data/processed/processed_media_data.csv', index=False)
