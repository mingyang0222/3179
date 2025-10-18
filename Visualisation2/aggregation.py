import pandas as pd

# INPUT: original dataset you uploaded
INPUT = "death-rates-from-air-pollution.csv"

# OUTPUT: aggregated CSV for all countries (and World)
OUTPUT = "deaths_airpollution_all_entities.csv"

# Column in your dataset that contains the death rate (age-standardized rate)
RATE_COL = "Deaths - Air pollution - Sex: Both - Age: Age-standardized (Rate)"

# Read the CSV
df = pd.read_csv(INPUT)

# Quick check: print columns if you need to verify names
print("Columns available:", df.columns.tolist())

# Keep only the fields we need
df_small = df[["Entity", "Year", RATE_COL]].copy()

# Remove rows with missing values (optional but clean)
df_small = df_small.dropna(subset=["Entity", "Year", RATE_COL])

# Aggregate — if there are duplicates for same Entity-Year, take mean
agg = (
    df_small.groupby(["Entity", "Year"], as_index=False)[RATE_COL]
    .mean()
    .rename(columns={RATE_COL: "DeathRate"})
)

# Save aggregated CSV
agg.to_csv(OUTPUT, index=False)
print(f"✅ Saved {OUTPUT} ({len(agg)} rows)")
print(agg.head(12))
