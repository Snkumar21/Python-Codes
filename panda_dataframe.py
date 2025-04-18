# create a dataframe using python list
import pandas as pd
# create a two-dimensional list
datal = [['AAA', 25, 'Pune'],
        ['BBB', 30, 'Mumbai'],
        ['CCC', 35, 'Nasik']]

# create a DataFrame from the list
df = pd.DataFrame(datal, columns=['Name', 'Age', 'City'])
print(df)