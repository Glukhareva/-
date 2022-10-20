import pandas as pd
data = pd.read_csv("test_3.csv", header = None)
for i in range(len(data)):
    if data[i] == data.max():
        data[i].append(1)
    else:
        data[i].append(0)
print(data)
