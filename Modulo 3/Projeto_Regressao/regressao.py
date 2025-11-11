import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

dataset = pd.read_csv('Walmart_Vendas.csv')

x = dataset[['Vendas_Semanais']]
y = dataset[['Temperatura']]

x_treino, x_teste, y_teste, y_treino = train_test_split(x, y, test_size=1/3, random_state=0)

regressor = LinearRegression()

regressor.fit(x_treino, y_treino)
y_pred = regressor.predict(x_teste)

plt.figure(figsize=(15,8))
plt.plot(x,y, 'Dr')
plt.title('Teste de Regressão Linear de Vendas Semanais x Temperatura em Fahrenheit')
plt.xlabel('Vendas Semanais')
plt.ylabel('Temperatura em Fahrenheit')
plt.show()

lt.figure(figsize=(15,8))
plt.plot(x,y, 'Dr')
plt.plot(x_treino, regressor.predict(x_treino), color='blue')
plt.title('Teste de Regressão Linear de Vendas Semanais x Temperatura em Fahrenheit')
plt.xlabel('Vendas Semanais')
plt.ylabel('Temperatura em Fahrenheit')
plt.show()