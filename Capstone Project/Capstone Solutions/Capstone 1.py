# How to get the nrows, ncolumns, datatype, summary stats of each column of a dataframe? Also get the array and list equivalent.

df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')

#  number of rows and columns
print(df.shape)

# datatypes
print(df.dtypes)

# how many columns under each dtype
print(df.get_dtype_counts())
print(df.dtypes.value_counts())

# summary statistics
df_stats = df.describe()

# numpy array 
df_arr = df.values

# list
df_list = df.values.tolist()

