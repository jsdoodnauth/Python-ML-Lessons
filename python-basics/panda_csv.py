import pandas as pd
from pandas.plotting import scatter_matrix
from matplotlib import pyplot

csv_file = "../data/movies.csv"
col_names = ['Film','Genre','Lead-Studio','Audience-score','Profitability','Rotten-Tomatoes','Worldwide-Gross','Year']
df = pd.read_csv(csv_file)

print('Shape: {}'.format(df.shape))
print(df.head())
print('=========================================')
print('DESCRIBE ================================')
print(df.describe())

print('=========================================')
print('GROUP ================================')
print(df.groupby('Genre').size())

# df.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
# pyplot.show()

# Historgram
# df.hist()
# pyplot.show()

# scatter plot matrix
col = df[['Audience score %','Profitability','Rotten Tomatoes %']]
scatter_matrix(col)
pyplot.show()