import pandas as pd
data = pd.read_csv("test_3.csv", header = None)
for i in range(len(data)):
    for x in data:
        if data[i] < x:
            data[i].append(0)
        else:
            data[i].append(1)

    print(data)
