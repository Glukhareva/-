import pandas as pd
data = pd.read_csv("test_3.csv", header = None)
data1 = data.to_numpy()
for i in range(len(data1)-1):
    for j in range(len(data1[i])):
        if data1[i][j] >= data1[i + 1][j]:
            np.append(data1[i], 0)
        else: 
            np.append(data1[i], 1)
print(data1)
