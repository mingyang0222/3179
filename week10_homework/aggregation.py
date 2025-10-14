import pandas as pd

# INPUT: original dataset you uploaded
INPUT = "death-rates-from-air-pollution.csv"

# OUTPUT: filtered/aggregated CSV for the chart
OUTPUT = "deaths_airpollution_world_malaysia.csv"

# Column in your dataset that contains the death rate (age-standardized rate)
RATE_COL = "Deaths - Air pollution - Sex: Both - Age: Age-standardized (Rate)"

# Read
df = pd.read_csv(INPUT)

# Quick check: print columns if you need to verify names
print("Columns available:", df.columns.tolist())

# Keep only the fields we need
df_small = df[["Entity", "Year", RATE_COL]].copy()

# Filter to the two entities we want (World and Malaysia) -- adjust names if your file uses different Entity names
targets = ["World", "Malaysia"]

df_targets = df_small[df_small["Entity"].isin(targets)].copy()

# If there are duplicates for same Entity-Year, take mean
agg = df_targets.groupby(["Entity", "Year"], as_index=False)[RATE_COL].mean().rename(columns={RATE_COL: "DeathRate"})

# Save aggregated CSV
agg.to_csv(OUTPUT, index=False)
print(f"Saved {OUTPUT} ({len(agg)} rows). Sample:")
print(agg.head(12))
