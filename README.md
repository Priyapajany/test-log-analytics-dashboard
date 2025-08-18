# Test Log Analytics Dashboard

## Project Overview
This project analyzes **QA test execution logs** to uncover insights into test quality, failure trends, and execution times.  
It transforms raw logs into **interactive dashboards** to help QA teams monitor and improve testing efficiency.  

## Objectives
- Parse and clean raw test execution logs.  
- Identify trends in pass/fail results across modules and time.  
- Visualize execution times and failure hotspots.  
- Build an interactive dashboard for monitoring.  

## Tech Stack
- **Python** (Pandas, Matplotlib, Plotly)  
- **Streamlit / Power BI** for dashboards  
- **Jupyter Notebook** for analysis  

## Dataset
- Source: Simulated/real QA logs (CSV format).  
- Columns: `date`, `test_case_id`, `module`, `status`, `execution_time`, `error_message`.  

## Key Features
- Test execution trends (daily/weekly).  
- Top failing modules.  
- Average execution time analysis.  
- Interactive filters by module/date.  

## Results
- Insert screenshots of dashboards here.  
- Example: *“Module X failed 35% more often compared to other modules.”*  

## How to Run
```bash
git clone <repo_url>
cd test-log-analytics
pip install -r requirements.txt
streamlit run dashboard.py
