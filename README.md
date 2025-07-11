# Sales KPI Dashboard with File Upload

A simple and interactive **Sales KPI Dashboard** built with **Python** and **Streamlit** that allows users to upload sales data files (CSV) via drag-and-drop and visualize key sales insights in real-time.

---

## Features

- **Drag-and-drop CSV upload** for quick and easy data loading  
- Calculates essential sales KPIs such as:  
  - Total Sales Revenue  
  - Average Order Value  
  - Units Sold  
- Interactive visualizations including:  
  - Sales Over Time (line chart)  
  - Sales by Region (bar chart)  
- Data preview for quick validation of uploaded files  
- Error handling for missing or incorrect columns in data  

---

## Getting Started

### Prerequisites

- Python 3.7+  
- Pip package manager  

### Installation

1. Clone the repository:  
   ```bash
   git clone https://github.com/yourusername/sales-kpi-dashboard.git  
   cd sales-kpi-dashboard  

2. Install required Python packages manually:

```bash
pip install streamlit pandas plotly
```
3. Run the Streamlit app with:

```bash
streamlit run app.py
```
## Using the Dashboard
Upload a CSV file containing your sales data with at least the following columns:
Date (YYYY-MM-DD format), Sales Amount, Units Sold, Region

## Sample Data
You can test the dashboard with the provided mock sales data file mock_sales_data.csv (or create your own).

## License
This project is open source and available under the MIT License.
