## 出来高あり、直近１２０分で１分毎安値、高値、始値、終値を１レコード

レコード件数: 14353件


```
# Layer
layers.Dense(4, activation='relu'),
layers.Dense(4, activation='relu'),
layers.Dense(4, activation='relu'),
layers.Dense(4, activation='relu'),
layers.Dense(4, activation='relu'),
layers.Dense(1)

# 結果 平均誤差 = 17095.11
45/45 - 0s - loss: 437196736.0000 - mae: 17095.1133 - mse: 437196736.0000
Testing set Mean Abs Error: 17095.11 after_5_minutes_price
```


```
# Layer
layers.Dense(4, activation='relu', input_shape=[len(train_dataset.keys())]),
layers.Dense(4, activation='relu'),
layers.Dense(1)

# 結果 平均誤差 = 9928.28
45/45 - 0s - loss: 188575200.0000 - mae: 9928.2803 - mse: 188575200.0000
Testing set Mean Abs Error: 9928.28 after_5_minutes_price
```

```
# Layer 
layers.Dense(2, activation='relu', input_shape=[len(train_dataset.keys())]),
layers.Dense(2, activation='relu'),
layers.Dense(1)

# 結果 平均誤差 = 9928.28
45/45 - 0s - loss: 178250176.0000 - mae: 9363.3926 - mse: 178250176.0000
Testing set Mean Abs Error: 9363.39 after_5_minutes_price
```

レコード件数: 17194件
```
# Layer
layers.Dense(2, activation='relu', input_shape=[len(train_dataset.keys())]),
layers.Dense(2, activation='relu'),
layers.Dense(1)

# 結果 平均誤差 = 11434.55
54/54 - 0s - loss: 231422192.0000 - mae: 11434.5469 - mse: 231422192.0000
Testing set Mean Abs Error: 11434.55 after_5_minutes_price
```