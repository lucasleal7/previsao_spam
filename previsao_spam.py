# -*- coding: utf-8 -*-
"""previsao_spam.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1JvrCyHhfNKntXoFXXRktf0Dh_rxpYxyn

# Definição do Problema

Este projeto tem como objetivo desenvolver um modelo de machine learning para classificar mensagens de texto como spam ou não-spam (ham).

O problema consiste em analisar um conjunto de dados contendo mensagens de texto e seus respectivos rótulos (spam ou ham) para treinar um modelo

capaz de identificar automaticamente mensagens indesejadas, como propagandas ou conteúdos promocionais, distinguindo-as de mensagens legítimas.

A solução utiliza um Pipeline que combina pré-processamento de texto (via CountVectorizer ou TfidfVectorizer) com um classificador MLPClassifier,

visando maximizar a acurácia e o recall para a classe spam, minimizando falsos negativos (spams classificados como ham).

# 1. Importação de bibliotecas
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, classification_report

"""O que faz: Importa as bibliotecas necessárias:

*  pandas: Para manipulação de dados.
*  train_test_split: Para dividir os dados em treinamento, validação e teste.
*  CountVectorizer: Para transformar texto em matrizes de contagem de palavras.
*  Pipeline: Para encadear pré-processamento e modelagem.
*  MLPClassifier: Para criar a rede neural perceptron multicamadas.
*  accuracy_score e classification_report: Para avaliar o desempenho do modelo.

# 2. Carregamento dos dados
"""

# subindo dataframe em cvs

df=pd.read_csv('/content/spam.csv')

"""# 3. Exploração dos dados"""

# vizualizando a tabela
df

#visualizando as colunas
df.columns

# verificando informação sobre o datframe
df.info()

#verificando dados nulos

df.isna().sum()

"""# 4. Pré-processamento: Criação da coluna Spam"""

#uma nova coluna Spam convertendo Category (ham/spam) em valores numéricos:

df['Spam']=df['Category'].apply(lambda x:1 if x=='spam' else 0)
df.head(5)

"""# 5. Divisão dos dados"""

# aqui eu sepraie 20% para teste
#Dos 80% restantes, 75% para treianemnto
# e 25% para validação


X_temp, X_test, y_temp, y_test = train_test_split(df.Message, df.Spam, test_size=0.20, random_state=42)

X_train, X_val, y_train, y_val = train_test_split(X_temp, y_temp, test_size=0.25, random_state=42)

"""# 6. Criação do Pipeline"""

#O Pipeline automaticamente aplica o CountVectorizer aos dados de entrada (ex.: X_train) para transformá-los em uma matriz de contagem e, em seguida, passa essa matriz para o MLPClassifier.

clf = Pipeline([
    ('vectorizer', CountVectorizer()),
    ('mlp', MLPClassifier(hidden_layer_sizes=(100,), max_iter=500, random_state=42))
])

"""# 7. Treinamento do modelo"""

clf.fit(X_train, y_train)

"""# 8. Avaliação no conjunto de validação"""

y_val_pred = clf.predict(X_val)
print("Acurácia na validação:", accuracy_score(y_val, y_val_pred))
print("Relatório de classificação (validação):\n", classification_report(y_val, y_val_pred))

# Fazer previsões no conjunto de teste
y_test_pred = clf.predict(X_test)
print("Acurácia no teste:", accuracy_score(y_test, y_test_pred))
print("Relatório de classificação (teste):\n", classification_report(y_test, y_test_pred))

emails=[
    'Sounds great! Are you home now?',
    'Will u meet ur dream partner soon? Is ur career off 2 a flyng start? 2 find out free, txt HORO followed by ur star sign, e. g. HORO ARIES'
]

clf.predict(emails)

clf.score(X_test,y_test)

"""# Conclusão

O modelo desenvolvido, utilizando um Pipeline com CountVectorizer e MLPClassifier, alcançou excelente desempenho na classificação de mensagens como spam ou não-spam. As acurácias obtidas foram de 98.3% no conjunto de validação e 98.9% no conjunto de teste, demonstrando alta precisão na identificação de mensagens. O recall para a classe spam atingiu 88% na validação e 92% no teste, indicando que o modelo é eficaz na detecção de spams. O uso do MLPClassifier, combinado com a vetorização de texto, proporcionou uma solução robusta para o problema, com resultados consistentes e confiáveis nos conjuntos de validação e teste.
"""