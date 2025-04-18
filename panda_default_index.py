#default index

import pandas as pd

datadd = {'Name': ['AAA', 'BBB', 'CCC'],
        'Age': [25, 28, 32],
        'City': ['PUNE', 'MUMBAI', 'NASIK']}

df = pd.DataFrame(datadd)
print(df)