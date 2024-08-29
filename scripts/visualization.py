import pandas as pd
import matplotlib.pyplot as plt

# Load processed data
data = pd.read_csv('data/processed/processed_media_data.csv')

# Example visualization
plt.figure(figsize=(10, 6))
plt.plot(data['Date'], data['EngagementMetric'], label='Customer Engagement')
plt.xlabel('Date')
plt.ylabel('Engagement Metric')
plt.title('Customer Engagement Over Time')
plt.legend()
plt.savefig('output/engagement_trend.png')
plt.show()
