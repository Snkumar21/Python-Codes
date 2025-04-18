import pandas as pd

# create a dictionary
datad = {'Name': ['AAA', 'BBB', 'CCC'],
        'Age': [25, 30, 35],
        'City': ['Pune', 'Mumbai', 'Nasik']}

# create a dataframe from the dictionary
df = pd.DataFrame(datad)
print(df)