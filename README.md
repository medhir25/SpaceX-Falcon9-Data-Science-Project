# SpaceX-Falcon9-Data-Science-Project
End-to-end data science project analyzing SpaceX Falcon 9 launch data, featuring an interactive data visualization dashboard built with Plotly Dash.
# Applied Data Science Capstone: SpaceX Falcon 9 Launch Analytics

This repository contains the complete portfolio of data science and machine learning labs completed for the IBM Applied Data Science Capstone project. The core focus of this project is to analyze historical SpaceX Falcon 9 launch data, discover key operational patterns, and build predictive tools to forecast first-stage booster landing outcomes.

## Repository Contents
* **`spacex-dash-app.py`**: A real-time, interactive data visualization web application built using **Plotly Dash**. 
* **`Jupyter Notebooks`**: A comprehensive series of standalone analytical notebooks covering the entire end-to-end data science lifecycle:
  * **Data Collection**: Fetching data from the SpaceX REST API and web scraping Wikipedia data via `BeautifulSoup`.
  * **Data Wrangling**: Cleaning missing entries, structuring target indicators, and performing key transformations.
  * **EDA with SQL**: Querying structural databases to establish payload patterns and site histories.
  * **EDA with Folium**: Mapping launch site locations and calculating geographical proximity to landmarks.
  * **Machine Learning Prediction**: Training and optimizing Classification models (Logistic Regression, SVM, Decision Tree, and Random Forest) to project booster landings.

---

## Interactive Dashboard Overview
The Plotly Dash web interface provides analytical flight-performance insights by processing variables across separate structural tasks:

* **Task 1: Launch Site Dropdown Filter**: Allows a seamless switch between viewing composite metrics across "All Sites" or drilling down into explicit locations (`CCAFS LC-40`, `VAFB SLC-4E`, `KSC LC-39A`, `CCAFS SLC-40`).
* **Task 2: Dynamic Success/Failure Pie Charts**: Automatically calculates the proportion of successful flights across selected locations or details specific success-to-failure ratios.
* **Task 3: Interactive Payload Slider**: A range selector bounding structural payload parameters from 0 kg up to 10,000 kg to isolate performance by mass boundaries.
* **Task 4: Color-Coded Success Scatter Plots**: Maps payload thresholds against categorical launch outcomes, segmented visually by **Booster Version Category** to isolate mechanical efficiency.

### Dashboard Core Tech Stack
* Python 3.11
* Plotly Dash & Dash Core Components
* Pandas (Boolean Masking & Data Formatting)
* Plotly Express (Interactive Plot Engines)

---

## Key Data Insights Discovered

1. **Launch Success Proportions**: `KSC LC-39A` yields the highest structural share of total successful launches across the historical data timeline.
2. **Launch Efficiency**: `KSC LC-39A` maintains the highest overall proportion of successful missions relative to its individual failure count.
3. **Optimal Payload Ranges**: Payloads falling strictly between **2,000 kg and 4,000 kg** achieve the highest cluster density of successful outcomes.
4. **Sub-optimal Payload Ranges**: Heavy-class payloads ranging from **5,000 kg to 7,000 kg** reflect the lowest visual landing success rates across multiple launch facilities.
5. **Top Performing Hardware**: The **FT (Full Thrust)** and **B5** booster version categories display the highest historical operational reliability.
