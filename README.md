# 🧪 Test Log Analytics Dashboard

This project simulates and analyzes test execution logs to uncover trends in software testing, such as pass/fail rates, execution time patterns, environment performance, and tester activity.



## 📂 Project Structure
test-log-analytics-dashboard/
│
├── data/
│ └── fake_test_logs.csv # Simulated dataset
│
├── notebooks/
│ └── test_log_analysis.ipynb # Analysis & visualizations
│
├── scripts/
│ └── generate_fake_logs.py # Script to generate fake dataset
│
├── README.md # Project documentation
└── requirements.txt # Dependencies

## 📊 Features
- Generate a **synthetic dataset** of test execution logs.
- Analyze test outcomes (**Pass vs Fail**).
- Track **execution time trends**.
- Compare executions by **environment** and **tester**.
- Monitor **daily execution activity**.
- Visualize **Pass vs Fail trend over time**.
- Summarize **Key Insights** for QA/Dev teams.


# Tech Stack

Python (Pandas, Matplotlib)
Jupyter Notebook for analysis
VS Code for development

# Future Improvements

Add interactive dashboards (Plotly/Dash/Streamlit).
Integrate with real test logs from CI/CD pipelines.
Automate report generation (PDF/HTML).
