import pandas as pd
import numpy as np
data = {'city': ['Miami', 'New York', 'Tokyo'], 'Age':[31, 32, 34], 'Name': ['Gabriela', 'Nuria', 'Angel'] }
labels = [1,2,3]
dataframe = pd.DataFrame(data=data, index=labels)
cities = dataframe['city']
dfdatacsv = pd.read_csv('C:\\Users\\jyoji\\Downloads\\Students Score for Experimentation.csv')
print(dfdatacsv.to_string())