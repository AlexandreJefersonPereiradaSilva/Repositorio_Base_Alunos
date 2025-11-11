import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

dataset = pd.read_csv('Walmart_Vendas.csv')

dataset[['Vendas_Diarias']] = dataset['Vendas_Semanais'].apply(lambda v: v / 7)
x = dataset[['Vendas_Diarias']]

dataset[['Temperatura_Celcius']] = dataset['Temperatura'].apply(lambda f: (f - 32) * 5/9)
y = dataset[['Temperatura_Celcius']]

x_treino, x_teste, y_teste, y_treino = train_test_split(x, y, test_size=1/3, random_state=0)

regressor = LinearRegression()

regressor.fit(x_treino, y_treino)
y_pred = regressor.predict(x_teste)

plt.figure(figsize=(15,8))
plt.plot(x,y, 'Dr')
plt.title('Teste de Regressão Linear de Vendas Diarias x Temperatura em Celcius')
plt.xlabel('Vendas Diarias')
plt.ylabel('Temperatura em Celcius')
plt.show()

plt.figure(figsize=(15,8))
plt.plot(x,y, 'Dr')
plt.plot(x_treino, regressor.predict(x_treino), color='blue')
plt.title('Regressao de Regressão Linear de Vendas Diarias x Temperatura em Celcius')
plt.xlabel('Vendas Diarias')
plt.ylabel('Temperatura em Celcius')
plt.show()