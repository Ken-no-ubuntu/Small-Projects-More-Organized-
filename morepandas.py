import pandas as pd
from functools import lru_cache

@lru_cache(maxsize=1)
def get_dataframe():
    return pd.read_excel(r"C:\Users\jyoji\Downloads\a01200_2.xlsx")
df = get_dataframe()
#df = df.dropna
print(df.plot.hist())
df.plot.hist()