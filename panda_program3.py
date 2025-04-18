import pandas as pd
# Create Series from python dictionary
# create a dictionary
grades = {"Semester1": 4.25, "Semester2": 4.28, "Semester3": 4.75}
# create a series from the dictionary
seriesd = pd.Series(grades)
# display the series
print(seriesd)
# select specific dictionary items using index argument
seriesd = pd.Series(grades, index = ["Semester1", "Semester2"])
print(seriesd)