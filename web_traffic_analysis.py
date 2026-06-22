import pandas as pd

df = pd.read_csv("website_traffic.csv")

print("Website Traffic Data")
print(df)

total_users = len(df)

avg_pageviews = df["PageViews"].mean()
avg_session = df["SessionDuration"].mean()

dropoff = df["ExitPage"].value_counts()

print("\nTotal Users:", total_users)
print("Average Page Views:", round(avg_pageviews,2))
print("Average Session Duration:", round(avg_session,2))

print("\nDrop-Off Points")
print(dropoff)

with open("traffic_report.txt","w") as f:
    f.write("WEB TRAFFIC ANALYTICS REPORT\n\n")
    f.write(f"Total Users: {total_users}\n")
    f.write(f"Average Page Views: {round(avg_pageviews,2)}\n")
    f.write(f"Average Session Duration: {round(avg_session,2)}\n\n")
    f.write("Drop-Off Points:\n")
    f.write(str(dropoff))

print("\nReport Generated Successfully")