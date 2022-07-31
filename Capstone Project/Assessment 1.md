# Final Capstone Project

# Capstone 2

## How to get the nrows, ncolumns, datatype, summary stats of each column of a dataframe? Also get the array and list equivalent.

## Difficulty Level: L2

Get the number of rows, columns, datatype and summary statistics of each column of the Cars93 dataset. Also get the numpy array and list equivalent of the dataframe.

# Input

df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')


## --------------------------------------------------------------------------------------------


# Capstone 2

## How to use apply function on existing columns with global variables as additional arguments?

## Difficulty Level: L3

In df, use apply method to replace the missing values in Min.Price with the column’s mean and those in Max.Price with the column’s median.

# Input

df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')


## --------------------------------------------------------------------------------------------


# Capstone 3

## How to change the order of columns of a dataframe?

## Difficulty Level: L3

## Actually 3 questions.

1. In df, interchange columns 'a' and 'c'.
2. Create a generic function to interchange two columns, without hardcoding column names.
3. Sort the columns in reverse alphabetical order, that is colume 'e' first through column 'a' last.

# Input

df = pd.DataFrame(np.arange(20).reshape(-1, 5), columns=list('abcde'))
