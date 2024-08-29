import pandas as pd
import powerbi

# Load processed data
data = pd.read_csv('data/processed/processed_media_data.csv')

# Example: Code to connect to Power BI and create a dashboard
# (Note: Actual Power BI connection will require proper API usage and setup)

# Save the dashboard (mockup)
dashboard = "Dashboard created using Power BI"
with open('output/dashboard.txt', 'w') as f:
    f.write(dashboard)
