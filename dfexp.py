import numpy as py
import geopandas as gp
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_excel(r"C:\Users\jyoji\Downloads\FEH_00200502_240813125814.xlsx", usecols= "B, AK",skiprows=8).rename(columns={"#D0330703_Health expenditure per capita (Prefecture + Municipality)[thousand yen]":"Expend"}).dropna()
df["AREA"] = df["AREA"].str.replace("-ken","").str.replace("-to","").str.replace("-fu","")
#df = df.rename(columns={'AREA': 'NAME_1'})
geoval = gp.read_file(r"C:\Users\jyoji\Downloads\%E5%B9%B3%E6%88%90_27_%E5%B9%B4%E5%9B%BD%E5%8B%A2%E8%AA%BF%E6%9F%BB_%E9%83%BD%E9%81%93%E5%BA%9C%E7%9C%8C%E7%95%8C_-_Japan_Prefecture_Boundaries_ECM.zip")
geoval = pd.concat([geoval,df], axis=1)
A= geoval["AREA"]!=geoval["NAME_1"]
geoval["AREA"] = geoval["AREA"].str.replace("Gumma", "Gunma")
print(geoval.columns.values)
print(A)
print(geoval["NAME_1"])
print(geoval["AREA"])