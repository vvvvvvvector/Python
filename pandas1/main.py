import os  # os.remove(filePathX)
import pandas

name = ['Bob', 'Jess', 'Jess', 'Marta', 'Janek', 'Melania', 'Jess', 'Melania']
year = [1968, 1999, 1955, 2013, 1977, 1978, 2003, 2017]

dataSet1 = list(zip(name, year))  # connecting 2 lists

dataFrame = pandas.DataFrame(data=dataSet1, columns=['Name', 'Year of Birth'])
# print(dataFrame)

# noinspection PyTypeChecker
# dataFrame.to_csv('Files/YearOfBirth.csv', index=False, header=False)  # index - row names, header - columns names
# noinspection PyTypeChecker
# dataFrame.to_csv('Files/YearOfBirth.txt', index=False, header=False, sep=' ')
# dataFrame.to_excel('Files/YearOfBirth.xlsx', index=False)

filePath0 = r'Files/YearOfBirth.csv'
filePath1 = r'Files/YearOfBirth.xlsx'

# myData0 = pandas.read_csv(filePath0)  # header first line of file?
# myData1 = pandas.read_csv(filePath0, header=None)  # columns names: 0, 1, ..
# myData2 = pandas.read_csv(filePath0, names=['Name', 'Year Of Birth'])  # naming columns

# myData3 - dataFrame type
myData3 = pandas.read_excel(filePath1)  # index_col = 1 ???

# dataSort3 - dataFrame type
dataSort3 = myData3.sort_values('Year of Birth', ascending=False)  # 2017 ... 1955
# print(dataSort3.head(8))

maxYear = dataSort3['Year of Birth'].max()
# print(maxYear)  # 2017
minYear = dataSort3['Year of Birth'].min()
# print(minYear)  # 1955

# values -> to_numpy - convert dataFrame to NumPy array
maxYearName = dataSort3['Name'][dataSort3['Year of Birth'] == maxYear].to_numpy()
# print(maxYearName)  # ['Melania']
minYearName = dataSort3['Name'][dataSort3['Year of Birth'] == minYear].values
# print(minYearName)  # ['Jess']

# will print boolean values
# print(myData3['Year of Birth'] < 2000)

# print names and years of persons which 'Year of Birth' < 2000
# print(myData3[myData3['Year of Birth'] < 2000])

# print unique names
# print(myData3['Name'].unique())
# generate descriptive statistics.
# print(myData3['Name'].describe())

# group dataFrame by names then sum years of birth
# nameGroup = myData3.groupby('Name')
# print(nameGroup.sum())

# rename columns
myData3.columns = ['names', 'birth']
# create new column 'new' which contains value = 10
# myData3['new'] = 10
# delete new column
# del myData3['new']
# new indexes instead 0, ... , 7 -> a, ... , h
i = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# change old indexes to new
myData3.index = i

# new values of column instead years
# myData3['birth'] = [1, 2, 3, 4, 5, 6, 7, 8]

# print info about row indexed like 'c'
# print(myData3.loc['c'])

# print info about rows from index 'a' to 'd'
# print(myData3.loc['a':'d'])

# dataFrame -> smaller independent dataFrame
# ubDataFrame = myData3.loc['a':'d', ['names', 'birth']]
# print(subDataFrame)

# transposition of dataFrame row <-> column
# print(myData3.T)

print(pandas.crosstab(myData3.names, myData3.birth))

