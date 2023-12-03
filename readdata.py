import pandas as pd

# Replace 'your_file_path.csv' with the path of your uploaded CSV file

df = pd.read_csv('resources/fnew-2023-2.csv')
print(df.head(10))