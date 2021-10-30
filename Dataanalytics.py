import pandas as pd

"""
A Series, by contrast, is a sequence of data values.
 If a DataFrame is a table, 
a Series is a list. And in fact you can 
create one with nothing more than a list:

"""

"""


dt = pd.DataFrame({
    'Yes': [50, 29],
    'No': [23, 53]
})

dt = pd.DataFrame({
    'John': ['Why is that'],
    'Jane': ['What is this']
}, index=['Person A', 'Person B'])

dt = pd.Series([1, 2, 3, 4, 5])

dt = pd.Series([30, 23, 50], index=['2012', '2013 well', '2021 wow'],
               name='Stuff')
               
               

founders_file = pd.read_csv("D:/PERSONALPROJECTS/Python/Founders.csv", index_col=0)

founders_file.shape
founders_file.head()
with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    # This method generates a high-level summary of
    # the attributes of the given column. It is type-aware,
    # meaning that its output changes based on the data type
    # of the input. The output above only makes
    # sense for numerical data; for string data here's what we get:
    # print(founders_file.Gender.describe())

    # to see the mean of the points allotted
    # print(founders_file.Gender.mean())

    # To see a list of unique values we can use the unique()
    # print(founders_file.Company.unique())

    # To see a list of unique values and how often they
    # occur in the dataset, we can use the value_counts() method:
    # print(founders_file.Company.value_counts())
    

buildings_file = pd.read_csv(
    "D:/ALL/CSV files/datasets-master/Buildings.csv",
    index_col=0)
# A map is a term, borrowed from mathematics,
# for a function that takes one set of values and "maps"
# them to another set of values. In data science
# we often have a need for creating new representations
# from existing data, or for transforming data from the
# format it is in now to the format that we want it to
# be in later. Maps are what handle this work, making
# them extremely important for getting your work done!
# There are two mapping methods that you will use often.
# map() is the first, and slightly simpler one. For example,
# suppose that we wanted to re mean the scores the wines
# received to 0. We can do this as follows:

buildings_file.shape
buildings_file.head()
with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    psd_mean = buildings_file.mean()
    psd = buildings_file.Floors.map(lambda p: p - psd_mean)


#  print(psd)
# The function you pass to map() should expect a single value
# from the Series (a point value, in the above
# example), and return a transformed version
# of that value. map() returns a new Series where
# all the values have been transformed by your function.
# apply() is the equivalent method if we want to transform
# a whole DataFrame by calling a custom method on each row.
def re_mean_floors(row):
    row.Floors = row.Floors - psd_mean
    return row


pd = buildings_file.apply(re_mean_floors, axis='columns')
print(pd)

"""