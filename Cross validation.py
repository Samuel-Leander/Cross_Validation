import pandas as pd
from sklearn.model_selection import cross_val_score, KFold
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from scipy import stats

dataset_credit = pd.read_csv('C:/Users/samue/OneDrive/Documentos/Ciência de dados/Ciência de dados/Programação/Python/Pandas, Numpy e Estatística/credit_data.csv')
dataset_credit.dropna(inplace=True) # Remove rows with missing values

X = dataset_credit.iloc[:, 1:4].values
Y = dataset_credit.iloc[:,4].values

resultados_naive_bayes_cv = []
resultados_logistics_cv = []
resultados_forest_cv = []

for i in range(30):
    kFold = KFold(n_splits = 10,shuffle = True, random_state = i) #dividir a base em 10 partes e shuffle faz o sorteio dos registros

    naive_bayes = GaussianNB()
    scores = cross_val_score(naive_bayes, X, Y, cv = kFold)
    resultados_naive_bayes_cv.append(scores.mean())

    logistics = LogisticRegression()
    scores = cross_val_score(logistics, X, Y, cv = kFold)
    resultados_logistics_cv.append(scores.mean())
    
    forest = RandomForestClassifier()
    scores = cross_val_score(forest, X, Y, cv = kFold)
    resultados_forest_cv.append(scores.mean())

print(scores) # scores é uma lista com os resultados de cada fold / 10*30

print(scores.mean())

print(resultados_naive_bayes_cv,("\n"))
print(resultados_forest_cv,("\n"))
print(resultados_logistics_cv,("\n"))

# COEFICIENTE DE VARIAÇÃO
print(stats.variation(resultados_naive_bayes_cv),("\n"), stats.variation(resultados_forest_cv),("\n"),stats.variation(resultados_logistics_cv))