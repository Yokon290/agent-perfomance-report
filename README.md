# 📈 Agent Performance Report

This is a real-world data analysis task that simulates work as a junior data analyst.

---

## 🧩 Problem Description

You are given support ticket data from customer service. Your job is to:
- Filter only tickets marked as `"Closed"`
- Count how many closed tickets each agent resolved
- Calculate the average response time per agent
- Export the results into a clean CSV report

---

## 🛠️ Tools Used

- **Python** 🐍
- **Pandas** for data analysis 📊

---

## 📁 Files in This Project

| File Name | Description |
|-----------|-------------|
| `support_tickets.csv` | Raw ticket data for analysis |
| `perfomance_report.py` | Python script that filters, analyzes, and exports the report |
| `agent_perfomance_report.csv` | Final generated report (created after running the script) |

---

## ✅ How to Run It

1. Make sure you have **Pandas** installed:
   pip install pandas

Run the script:
python perfomance_report.py

The report will be saved as:
agent_perfomance_report.csv

🧪 Example Output
agent_name  closed_tickets_count  average_response_time
Alice       2                     27.5
Bob         1                     35.0
Charlie     1                     45.0
Denise      2                     35.0


💼 Why This Matters
This project shows:
I can clean and analyze real-world data
I understand groupby, filtering, and aggregations in Pandas
I can deliver usable reports for business decision-making

