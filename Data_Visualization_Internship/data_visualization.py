import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("iris.csv")

# 1. BAR CHART
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x="species")
plt.title("Iris Species Count")
plt.xlabel("Species")
plt.ylabel("Count")
plt.savefig("bar_chart.png")
plt.close()

# 2. PIE CHART
plt.figure(figsize=(6, 4))
df["species"].value_counts().plot(
    kind="pie", autopct="%1.1f%%"
)
plt.title("Iris Species Distribution")
plt.ylabel("")
plt.savefig("pie_chart.png")
plt.close()

# 3. LINE GRAPH
avg = df.groupby("species").mean(numeric_only=True)

plt.figure(figsize=(8, 5))
sns.lineplot(data=avg.T, markers=True, dashes=False)
plt.title("Average Iris Measurements")
plt.xlabel("Measurements")
plt.ylabel("Average Values")
plt.savefig("line_graph.png")
plt.close()

print("All 3 charts created successfully!")