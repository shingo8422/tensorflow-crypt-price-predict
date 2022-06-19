# import csv

# with open('./2022-06-10-0925_2022-06-14-1538.csv') as csv_file:
#     spamreader = csv.reader(csv_file)
#     rows = [row for row in spamreader]
#     print(len(rows))

import pathlib

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import tensorflow as tf

from tensorflow import keras



column_names = ['Hajime', 'Takane', 'Yasune', 'Owarine', 'Dekidaka']

raw_dataset = pd.read_csv('./2022-06-10-0925_2022-06-14-1538.csv', names=column_names, na_values='?', comment='\t',sep=',', skipinitialspace=True)

dataset = raw_dataset.copy()
dataset.tail()

train_dataset = dataset.sample(frac=0.8, random_state=0)
test_dataset = dataset.drop(train_dataset.index)


sns.pairplot(train_dataset[ ['Hajime', 'Takane', 'Yasune', 'Owarine', 'Dekidaka']], diag_kind="kde")