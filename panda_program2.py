import pandas as pd 
# create a list
li = [1, 3, 5]
# create a series and specify labels
series1 = pd.Series(li, index = ["x", "y", "z"])
print(series1)
print(series1["y"])