import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned data
df = pd.read_csv("cleaned_powerconsumption.csv")

# Convert Datetime column again (for safety)
df["Datetime"] = pd.to_datetime(df["Datetime"])

# Set Datetime as index for time-series analysis
df.set_index("Datetime", inplace=True)

# 🔹 1️⃣ Basic Statistical Summary
print("\n🔍 Basic Statistical Summary:")
print(df.describe()[["Temperature", "Humidity", "WindSpeed", 
                     "PowerConsumption_Zone1", "PowerConsumption_Zone2", "PowerConsumption_Zone3"]])

# 🔹 2️⃣ Histograms of key features
df[["Temperature", "Humidity", "WindSpeed", "PowerConsumption_Zone1"]].hist(figsize=(12, 8), bins=30)
plt.suptitle("Feature Distributions", fontsize=16)
plt.show()

# 🔹 3️⃣ Time-Series Plot of Power Consumption with Rolling Average
# Time-Series Plot with Trend (New Colors)
plt.figure(figsize=(12, 5))
plt.plot(df.index, df["PowerConsumption_Zone1"], label="Zone 1 Power Consumption", color='#9467bd', alpha=0.6)
plt.plot(df["PowerConsumption_Zone1"].rolling(window=100).mean(), label="Rolling Avg (100)", color='#ffbf00', linewidth=2)
plt.xlabel("Date")
plt.ylabel("Power Consumption")
plt.title("Power Consumption Over Time with Trend")
plt.legend()
plt.show()


# 🔹 4️⃣ Correlation Heatmap (Improved Readability)
plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5, vmin=-1, vmax=1)
plt.title("Feature Correlation Heatmap")
plt.show()

print("\n✅ EDA Completed. Statistical summary and correlation analysis added.")
