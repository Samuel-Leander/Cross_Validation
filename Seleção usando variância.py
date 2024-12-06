import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler #transformar os dados para a mesma escala
from sklearn.feature_selection import VarianceThreshold # remover as variáveis com baixa variação
from sklearn.naive_bayes import GaussianNB # modelo de classificação
from sklearn.metrics import accuracy_score # calcular a precisão do modelo

dataset = pd.read_csv('C:/Users/samue/OneDrive/Documentos/Ciência de dados/Ciência de dados/Programação/Python/Pandas, Numpy e Estatística/credit_data.csv')
dataset.dropna(inplace=True) # Remove linhas com valores faltantes
# print(dataset.describe())

X = dataset.iloc[:, 1:4].values # Carregar os dados de entrada
Y = dataset.iloc[:, 4].values # Carregar os dados de saída

scaler = MinMaxScaler()# Transformar os dados para a mesma escala
X = scaler.fit_transform(X)
# print(X)

selecao = VarianceThreshold(threshold=0.027)# Seleção de características
X_novo = selecao.fit_transform(X)
print(X_novo, X_novo.shape)

print(np.var(X[0]),('\n'), np.var(X[1]),('\n'), np.var(X[2]))

naive_bayes_sem_selecao = GaussianNB()# Criar um modelo de Naive Bayes
naive_bayes_sem_selecao.fit(X, Y)# Treinar o modelo
previsoes = naive_bayes_sem_selecao.predict(X) # Fazer previsões
print(accuracy_score(previsoes, Y))# Avaliar o modelo

naive_bayes_com_selecao = GaussianNB()
naive_bayes_com_selecao.fit(X_novo, Y)
previsoes = naive_bayes_com_selecao.predict(X_novo)
print(accuracy_score(previsoes, Y))