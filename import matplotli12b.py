import pandas as pn
import numpy as np
import matplotlib.pyplot as plt
df = pn.read_excel(r"C:\Users\jyoji\Downloads\FEH_00200502_240813125814.xlsx", usecols="B:AK", skiprows=8)
# Example data
prefectures = df['AREA']
expenditures = df['#D0330703_Health expenditure per capita (Prefecture + Municipality)[thousand yen]']  # Average expenditure in yen
plt.figure(figsize=(10, 6))
plt.scatter(prefectures, expenditures, alpha=0.5, cmap='coolwarm')
# Adding titles and labels
plt.xlabel("Prefectures")
plt.ylabel("Average Expenditure (Yen)")
plt.title("Average Expenditure per Prefecture in Japan")
plt.colorbar(label="Expenditure (Yen)")

# Display the chart
#plt.show()
print(prefectures)
