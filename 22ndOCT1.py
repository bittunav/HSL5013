
import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
df = pd.read_csv(r"D:\HSL5013\golf_ball_launch_speed_distance.csv")

# Display data
print(df.head())
print(df.describe())

# Actual column names from CSV
speed = "launch_speed_m_s"
distance = "distance_m"

# 1. Histogram of launch speed
plt.figure(figsize=(8, 5))

plt.hist(df[speed].dropna(), bins=20, edgecolor="black")

plt.xlabel("Launch Speed (m/s)")
plt.ylabel("Frequency")
plt.title("Distribution of Golf Ball Launch Speed")

plt.tight_layout()
plt.savefig("launch_speed_histogram.png", dpi=300)
plt.show()

# 2. Scatter plot
plt.figure(figsize=(8, 5))

plt.scatter(df[speed], df[distance], edgecolor="black")

plt.xlabel("Launch Speed (m/s)")
plt.ylabel("Distance (m)")
plt.title("Launch Speed versus Distance")

plt.tight_layout()
plt.savefig("speed_distance_scatter.png", dpi=300)
plt.show()
