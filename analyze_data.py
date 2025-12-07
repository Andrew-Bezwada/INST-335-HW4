# analyze_data.py

import pandas as pd
import os

# Define the file path relative to the script's location
FILE_PATH = os.path.join('data', 'fastfood.csv') 

print("=" * 50)
print("--- 1. Importing Data ---")
try:
    
    # Reading the CSV using the default index (RangeIndex)
    df = pd.read_csv(FILE_PATH)
    print(f"Successfully loaded data from: {FILE_PATH}\n")

except FileNotFoundError:
    
    print(f"Error: The file '{FILE_PATH}' was not found.")
    print("Please ensure your dataset 'fastfood.csv' is in the 'data/' folder.")
    exit()
    
# Initial checks
print("--- DataFrame Head (First 5 Rows) ---")
print(df.head().to_markdown(index=False))
print("\n" + "=" * 50 + "\n")

print("--- DataFrame Structure (info()) ---")
df.info()
print("\n" + "=" * 50 + "\n")

print("--- Numerical Statistics Summary (describe()) ---")
print(df.describe().to_markdown())
print("\n" + "=" * 50 + "\n")


print("--- 2. Data Access Examples (Using Default Index) ---")

# Accessing the row with index label 10
ROW_LABEL = 10 
print(f"a. Single row by its label ({ROW_LABEL}) using loc[]:")
print(df.loc[ROW_LABEL].to_markdown(numalign = "left", stralign = "left"))
print("-" * 20)

# Accessing the 11th row (position 10)
ROW_POSITION = 10
print(f"b. Single row by its position ({ROW_POSITION}) using iloc[]:")
print(df.iloc[ROW_POSITION].to_markdown(numalign = "left", stralign = "left"))
print("-" * 20)

# Slice of rows by label (index labels 20 to 24, inclusive)
print("c. Slice of rows by label (20 to 24) using loc[]:")
print(df.loc[20:24].to_markdown(index=False))
print("-" * 20)

# Slice of rows by position (position 30 up to, but not including, 35)
print("c. Slice of rows by position (30 to 34) using iloc[]:")
print(df.iloc[30:35].to_markdown(index=False))
print("-" * 20)

# Single column by name
COLUMN_NAME = 'restaurant' 
print(f"d. Single column ('{COLUMN_NAME}'). Head of the column:")
print(df[COLUMN_NAME].head())
print("-" * 20)

# Single cell by row label 5 and column label 'calories'
CELL_ROW = 5
CELL_COLUMN = 'calories'
print(f"e. Single cell by row label ({CELL_ROW}) and column label ('{CELL_COLUMN}') using loc[]:")
print(df.loc[CELL_ROW, CELL_COLUMN])
print("\n" + "="*50 + "\n")


print("--- 3. Filtering Data ---")

# Filter 1: Single Boolean condition (e.g., 'calories' greater than 800)
CALORIE_LIMIT = 800
print(f"Filter 1: Rows where 'calories' > {CALORIE_LIMIT}")
df_filtered_1 = df[df['calories'] > CALORIE_LIMIT]
print(df_filtered_1.head().to_markdown(index = False))
print("-" * 20)

# Filter 2: Combined Boolean conditions (e.g., 'restaurant' is 'Sonic' AND 'trans_fat' is greater than 1.5)
RESTAURANT_NAME = 'Sonic'
TRANS_FAT_LIMIT = 1.5
print(f"Filter 2: Rows where 'restaurant' == '{RESTAURANT_NAME}' AND 'trans_fat' > {TRANS_FAT_LIMIT}")
df_filtered_2 = df[(df['restaurant'] == RESTAURANT_NAME) & (df['trans_fat'] > TRANS_FAT_LIMIT)]
print(df_filtered_2.head().to_markdown(index=False))
print("\n" + "=" * 50 + "\n")

print("--- 4. Adding and Removing Columns ---")

# Create a new column 'sodium_per_calorie'
df['sodium_per_calorie'] = df['sodium'] / df['calories']
print("Added new column 'sodium_per_calorie' (sodium / calories). Head of the new column:")
print(df['sodium_per_calorie'].head())
print("-" * 20)

# Remove a column that has many missing values: 'vit_a'
COLUMN_TO_DROP = 'vit_a' 
df_after_drop = df.drop(COLUMN_TO_DROP, axis=1)
print(f"Removed column '{COLUMN_TO_DROP}' using .drop(axis=1).")
print("New list of columns:")
print(df_after_drop.columns.tolist())

print("\n" + "=" * 50 + "\n")

print("--- 5. Groupby() Operation (Split-Apply-Combine) ---")

GROUP_COLUMN = 'restaurant' # Categorical column
AGGREGATE_COLUMN = 'calories' # Numerical column

# Group by 'restaurant' and calculate the mean of 'calories' for each category
avg_calories_by_restaurant = df.groupby(GROUP_COLUMN)[AGGREGATE_COLUMN].mean()

print(f"Mean '{AGGREGATE_COLUMN}' grouped by '{GROUP_COLUMN}':")
print(avg_calories_by_restaurant.to_markdown())

print("\n" + "=" * 50 + "\n")
print("Analysis script execution complete.")