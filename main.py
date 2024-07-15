import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Load the CSV file
file_path = 'Bethany House residents.xlsx - with length of stay.csv'
df = pd.read_csv(file_path)

# Ensure date columns are in datetime format
df['Move in date'] = pd.to_datetime(df['Move in date'], errors='coerce')
df['Move out date'] = pd.to_datetime(df['Move out date'], errors='coerce')
df['DOB'] = pd.to_datetime(df['DOB'], errors='coerce')

# Calculate Age at Move-in
def calculate_age(born, move_in):
    return move_in.year - born.year - ((move_in.month, move_in.day) < (born.month, born.day))

df['Age at Move-in'] = df.apply(lambda row: calculate_age(row['DOB'], row['Move in date']) if pd.notnull(row['DOB']) and pd.notnull(row['Move in date']) else None, axis=1)

# 1. Distribution of Length of Stay
plt.figure(figsize=(12, 6))
sns.histplot(data=df, x='Length of Stay (# of days)', bins=30, kde=True)
plt.title('Distribution of Length of Stay')
plt.xlabel('Days')
plt.ylabel('Frequency')
plt.savefig('length_of_stay_distribution.png')
plt.close()

# 2. Top 10 Countries of Origin
top_countries = df['COO'].value_counts().head(10)
plt.figure(figsize=(12, 6))
top_countries.plot(kind='bar')
plt.title('Top 10 Countries of Origin')
plt.xlabel('Country')
plt.ylabel('Number of Residents')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('top_10_countries.png')
plt.close()

# 3. Move-ins and Move-outs over time
df['Year'] = df['Move in date'].dt.year
yearly_moves = df.groupby('Year').size().reset_index(name='Count')
yearly_moves['Move_outs'] = df.groupby(df['Move out date'].dt.year).size()

plt.figure(figsize=(12, 6))
plt.plot(yearly_moves['Year'], yearly_moves['Count'], label='Move-ins', marker='o')
plt.plot(yearly_moves['Year'], yearly_moves['Move_outs'], label='Move-outs', marker='o')
plt.title('Move-ins and Move-outs Over Time')
plt.xlabel('Year')
plt.ylabel('Number of Residents')
plt.legend()
plt.grid(True)
plt.savefig('moves_over_time.png')
plt.close()

# 4. Age Distribution at Move-in
plt.figure(figsize=(12, 6))
sns.histplot(data=df, x='Age at Move-in', bins=20, kde=True)
plt.title('Age Distribution at Move-in')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.savefig('age_distribution.png')
plt.close()

# 5. Correlation between Age and Length of Stay
plt.figure(figsize=(10, 8))
sns.scatterplot(data=df, x='Age at Move-in', y='Length of Stay (# of days)')
plt.title('Correlation between Age and Length of Stay')
plt.xlabel('Age at Move-in')
plt.ylabel('Length of Stay (days)')
plt.savefig('age_vs_stay_correlation.png')
plt.close()

print("Visualizations have been saved as PNG files in the current directory.")

# Additional statistics
print("\nAdditional Statistics:")
print(f"Total number of residents: {len(df)}")
print(f"Average length of stay: {df['Length of Stay (# of days)'].mean():.2f} days")
print(f"Median length of stay: {df['Length of Stay (# of days)'].median()} days")
print(f"Longest stay: {df['Length of Stay (# of days)'].max()} days")
print(f"Shortest stay: {df['Length of Stay (# of days)'].min()} days")
print(f"\nMost common country of origin: {df['COO'].mode().values[0]}")
print(f"Average age at move-in: {df['Age at Move-in'].mean():.2f} years")