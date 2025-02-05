import pandas as pd

# Corrected file path using a raw string
file_path = r'C:\Users\jyoji\Downloads\experiment_python_1.xlsx'
df = pd.read_excel(file_path)

print(df.head())