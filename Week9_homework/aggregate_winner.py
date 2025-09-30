import pandas as pd

df = pd.read_csv("WorldCups.csv")

winners_count = df['Winner'].value_counts().reset_index()

winners_count.columns = ['Country', 'Number_of_Wins']

winners_count.to_csv("fifa_winners.csv", index=False)

