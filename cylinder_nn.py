import os
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras import layers, models, optimizers
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import KFold, train_test_split
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

df = pd.read_excel(file_path)
df.isna().sum()

df.rename(columns={'x/D': 'length', 'z/D': 'height'}, inplace=True)

length, height, u, v, w, target = df['length'].to_numpy(), df['height'].to_numpy(), df['u'].to_numpy(), df['v'].to_numpy(), df['w'].to_numpy(), df['F'].to_numpy()
inputs = np.stack((length, height, u, v, w), axis=1)

def create_model(input_shape):
    inputs = layers.Input(shape=input_shape)
    layer = layers.Dense(256, activation='relu')(inputs)
    layer = layers.Dense(128, activation='relu')(layer)
    layer = layers.Dense(64, activation='relu')(layer)
    layer = layers.Dense(32, activation='relu')(layer)
    outputs = layers.Dense(1)(layer)
    model = models.Model(inputs, outputs)
    model.compile(optimizer='adam', loss='mean_squared_error', metrics=['mse'])
    return model

kf = KFold(n_splits=15, shuffle=True, random_state=50)
mse_scores = []

for fold, (train_index, val_index) in enumerate(kf.split(inputs)):
    x_train, x_val = inputs[train_index], inputs[val_index]
    scalar_x = StandardScaler()
    x_train = scalar_x.fit_transform(x_train)
    x_val = scalar_x.transform(x_val)
    y_train, y_val = target[train_index], target[val_index]
    y_train = y_train.reshape(-1, 1)
    y_val = y_val.reshape(-1, 1)
    scalar_y = StandardScaler()
    y_train = scalar_y.fit_transform(y_train)
    y_val = scalar_y.transform(y_val)
    model = create_model(inputs.shape[1])
    y_train = y_train.flatten()
    y_val = y_val.flatten()
    model.fit(x_train, y_train, epochs=100, batch_size=16, verbose=0)
    y_pred = model.predict(x_val)
    y_pred = scalar_y.inverse_transform(y_pred)
    y_val = scalar_y.inverse_transform(y_val.reshape(-1, 1)).flatten()
    mse = mean_squared_error(y_val, y_pred)
    mse_scores.append(mse)
    plt.figure(figsize=(8, 6))
    plt.scatter(y_val, y_pred, alpha=0.6)
    plt.plot([y_val.min(), y_val.max()], [y_val.min(), y_val.max()], 'r--', lw=2)
    plt.xlabel('Actual Values')
    plt.ylabel('Predicted Values')
    plt.title(f'Fold {fold+1}: Actual vs Predicted')
    plt.show()
    plt.savefig('/content/drive/My Drive/Turbulence Program/fig{}.png'.format(fold+1))
print(f'Mean MSE: {np.mean(mse_scores)}')
plt.plot(range(1, len(mse_scores) + 1), mse_scores)
plt.xlabel('Fold')
plt.ylabel('MSE')
plt.title('MSE across folds')
plt.show()
