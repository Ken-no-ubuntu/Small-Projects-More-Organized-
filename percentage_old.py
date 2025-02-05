import numpy as py
import geopandas as gp
import matplotlib.pyplot as plt
import pandas as pd
plt.rcParams["font.family"]="MS Gothic"
old_df = pd.read_excel(r"C:\Users\jyoji\Downloads\a01200_2.xlsx", sheet_name= "第12表", usecols="T", skiprows=8, nrows=47).rename(columns={15.5:"Old Pop"}).dropna()
geoval = gp.read_file(r"C:\Users\jyoji\Downloads\%E5%B9%B3%E6%88%90_27_%E5%B9%B4%E5%9B%BD%E5%8B%A2%E8%AA%BF%E6%9F%BB_%E9%83%BD%E9%81%93%E5%BA%9C%E7%9C%8C%E7%95%8C_-_Japan_Prefecture_Boundaries_ECM.zip")
geoval = pd.concat([geoval, old_df], axis = 1)
ax1 = plt.subplot()
geoval.plot(figsize=(15,15),column='Old Pop', cmap='PuBu', legend=True, linewidth=0.2, edgecolor="black", ax= ax1)
ax1.axis("off")
plt.title("都道府県別75歳以上の人口割合")
for spine in ax1.spines.values():
    spine.set_visible(False)
plt.show()
print(old_df.tail())