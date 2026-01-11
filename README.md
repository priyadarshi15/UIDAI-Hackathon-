# Aadhaar-Pulse: Predictive Resource Optimization for Patna

## Project Overview
Aadhaar-Pulse is a data-driven framework developed for the **UIDAI Hackathon 2026**. Our goal is to analyze demographic update trends in Patna, Bihar, to identify service gaps and predict demand surges. By transforming raw CSV data into actionable insights, we help UIDAI optimize the deployment of Mobile Update Vans and staff allocation.

## Key Features
- **Surge Detection:** Uses Z-score statistical analysis to identify abnormal spikes in update demand (e.g., the March 1st anomaly).
- **Service Desert Mapping:** Categorizes PIN codes into High Demand, Stable, and Low Access zones using quantile-based segmentation.
- **Resource Optimization:** Recommends specific locations for Mobile Aadhaar Vans based on the "Low Access" demographic data.

## Technical Analysis
Our analysis of 6,500+ records revealed:
- **Temporal Trends:** Massive single-day spikes (Anomalies) linked to government deadlines.
- **Demographic Gaps:** A significant lag in child biometric updates (ages 5-17) compared to adults.
- **Spatial Clusters:** High concentration of demand in specific urban PIN codes like 804453.

## Tech Stack
- **Language:** Python 3.x
- **Libraries:** Pandas (Data Manipulation), Matplotlib/Seaborn (Visualization), NumPy (Numerical Analysis).

## The Team
- **Mayank Priyadarshi** - ITER, Siksha ‘O’ Anusandhan University
- **Afreen Khan** - Banasthali Vidyapith
