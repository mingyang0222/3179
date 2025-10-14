# import pandas as pd

# df = pd.read_csv("WorldCups.csv")

# df['Winner'] = df['Winner'].replace({
#     'Germany FR': 'Germany',
#     'England': 'United Kingdom'
# })

# winners_count = df['Winner'].value_counts().reset_index()

# winners_count.columns = ['Country', 'Number_of_Wins']

# winners_count.to_csv("fifa_winners.csv", index=False)



import pandas as pd

# Step 1: Read the CSV file
# Replace 'renewables.csv' with your actual filename
df = pd.read_csv('renewable-share-energy.csv')

# Step 2: Filter for year 2022
df_2022 = df[df['Year'] == 2022]

# Step 3: Select only relevant columns
df_2022 = df_2022[['Entity', 'Code', 'Year', 'Renewables (% equivalent primary energy)']]

# Step 4: Drop rows with missing values (optional)
df_2022 = df_2022.dropna(subset=['Renewables (% equivalent primary energy)'])

# Step 5: Save to new CSV
df_2022.to_csv('renewables_2022.csv', index=False)

print("✅ Data for year 2022 has been saved to 'renewables_2022.csv'")
