import pandas as pd
import numpy as np


filename = 'aadhaar_patna_data.csv' 
df = pd.read_csv(filename)
df['date'] = pd.to_datetime(df['date'], dayfirst=True)


pincode_stats = df.groupby('pincode')['demo_age_17_'].agg(['mean', 'std']).reset_index()
df = df.merge(pincode_stats, on='pincode')

df['z_score'] = (df['demo_age_17_'] - df['mean']) / (df['std'] + 1e-9)


anomalies = df[df['z_score'] > 3].sort_values(by='z_score', ascending=False)
print("--- TOP SERVICE SURGE ANOMALIES ---")
print(anomalies[['date', 'pincode', 'demo_age_17_', 'z_score']].head())


pincode_summary = df.groupby('pincode').agg({
    'demo_age_17_': 'sum',
    'demo_age_5_17': 'sum'
}).reset_index()


q_high = pincode_summary['demo_age_17_'].quantile(0.75)
q_low = pincode_summary['demo_age_17_'].quantile(0.25)

def categorize(row):
    if row['demo_age_17_'] >= q_high: return 'High Demand Zone'
    if row['demo_age_17_'] <= q_low: return 'Low Access Zone'
    return 'Stable Zone'

pincode_summary['Segment'] = pincode_summary.apply(categorize, axis=1)


pincode_summary.to_csv('aadhaar_pulse_segments.csv', index=False)
print("\n--- SEGMENTATION COMPLETE: File saved as aadhaar_pulse_segments.csv ---")