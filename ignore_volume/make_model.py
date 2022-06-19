

# import pathlib

# import matplotlib.pyplot as plt
# import pandas as pd
# import seaborn as sns
# import tensorflow as tf

# from tensorflow import keras



column_names = []
column_names.append('price')
for i in range(99):
    column_names.append('{}_minutes_ago_price'.format(str(i+1)))
column_names.append('after_5_minutes_price')

print(column_names)
print(len(column_names))

# raw_dataset = pd.read_csv('./2022-06-10-0925_2022-06-14-1538.csv', names=column_names, na_values='?', comment='\t',sep=',', skipinitialspace=True)

# dataset = raw_dataset.copy()
# dataset.tail()

# train_dataset = dataset.sample(frac=0.8, random_state=0)
# test_dataset = dataset.drop(train_dataset.index)


# sns.pairplot(train_dataset[ ['Hajime', 'Takane', 'Yasune', 'Owarine', 'Dekidaka']], diag_kind="kde")