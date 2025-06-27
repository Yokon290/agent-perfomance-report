import pandas as pd

df = pd.read_csv("support_tickets.csv")

closed_tickets = df[df["status"] == "Closed"]

report = closed_tickets.groupby("agent_name").agg(
    closed_tickets_count=pd.NamedAgg(column="ticket_id", aggfunc="count"),
    average_response_time=pd.NamedAgg(column="response_time_minutes", aggfunc="mean")
).reset_index()

print("📈 Agent Perfomance Report:")
print(report)

report.to_csv("agent_perfomance_report.csv", index=False)
print("\n✅ Report saved to 'agent_perfomance_report.csv'")