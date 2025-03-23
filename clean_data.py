import pandas as pd

# Load data
df = pd.read_csv("powerconsumption.csv")

# Convert Datetime column
df["Datetime"] = pd.to_datetime(df["Datetime"])

# Check for missing values
missing_values = df.isnull().sum().sum()

# Detect outliers in WindSpeed using IQR method
Q1 = df["WindSpeed"].quantile(0.25)
Q3 = df["WindSpeed"].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Count outliers
outliers = df[(df["WindSpeed"] < lower_bound) | (df["WindSpeed"] > upper_bound)]
outlier_count = outliers.shape[0]

# Replace outliers with median
median_windspeed = df["WindSpeed"].median()
df.loc[df["WindSpeed"] < lower_bound, "WindSpeed"] = median_windspeed
df.loc[df["WindSpeed"] > upper_bound, "WindSpeed"] = median_windspeed

# Save cleaned file
df.to_csv("cleaned_powerconsumption.csv", index=False)

# Print clean summary
print("✅ Data cleaning complete. Saved as 'cleaned_powerconsumption.csv'.")
print(f"- No missing values found." if missing_values == 0 else f"- Missing values: {missing_values}")
print("- Datetime converted to proper format.")
print(f"- {outlier_count} WindSpeed outliers replaced with median ({median_windspeed}).\n")

# Show dataset overview
print(f"Dataset Overview:\n{df.shape[0]} rows, {df.shape[1]} columns")
print(f"Memory usage: {df.memory_usage(deep=True).sum() / 1e6:.2f} MB\n")

# Show first 2 rows for a quick preview
print("Preview:")
print(df.head(2)[["Datetime", "Temperature", "Humidity", "WindSpeed", "PowerConsumption_Zone1"]])
