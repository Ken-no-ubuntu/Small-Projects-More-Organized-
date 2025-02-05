import numpy as py
import geopandas as gp
import matplotlib.pyplot as plt
import pandas as pd
plt.rcParams['font.family'] = 'MS Gothic'
geodat = gp.read_file(r"C:\Users\jyoji\Downloads\A002005212020DDSWC13-JGD2011.zip", rows= slice(200,5000), columns=("CITY_NAME", "GEOMETRY"))
geodat= geodat[geodat["CITY_NAME"].str.contains("区", case= False, na= False)]
fig, ax= plt.subplots()
ax.axis('off')
for spine in ax.spines.values():
    spine.set_visible(False)
geodat.plot(ax=ax,figsize=(100,100), cmap="OrRd")
for x, y, label in zip(geodat.geometry.centroid.x, geodat.geometry.centroid.y, geodat['CITY_NAME']):
    plt.text(x, y, label, fontsize=5, ha='center', va='center')
plt.show()
print(geodat["CITY_NAME"])