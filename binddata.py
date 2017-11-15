import os
import pandas as pd
os.getcwd()
os.chdir('E:/data')

os.getcwd()
test = os.listdir()
type(test)
test[0]
len(test)

data = pd.read_excel(test[0])

for i in range(1,len(test)):
    data1 = pd.read_excel(test[i])
    data = pd.concat([data1,data])