# -*- coding: utf-8 -*-
"""T2.ModelosLineares.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/115NBhhJYhEGQRPUe2I0ABUgBnVg8tZCB

# Teste
"""

# import seaborn as sn
# import matplotlib.pyplot as plt
# import pandas as pd

# data=pd.read_csv('Well-knownCrypto(currency)2018-2023.csv')

# print(data.columns)
# print(data.info())
# print(data.isna().sum())
# print(data.describe())

# col=data.columns.values
# for i in col[2:]:
#     print(data[i].skew())
#     print(data[i].var())
#     print(data[i].describe())
#     sn.boxplot(data[i])
#     plt.show()

# sn.pairplot(data[col[2:]])
# plt.show()
# pr=data.Type.value_counts().to_dict()
# for kys,values in pr.items():
#     df=data[data['Type']==kys]
#     print(df.info())
#     print(df.isna().sum())
#     print(df.describe())
#     col=df.columns.values

#     for i in col[2:]:
#         plt.plot(df.Open.head(100),marker='o',color='red',label=f'Opening stock of {kys}')
#         plt.plot(df.Close.head(100),marker='o',color='blue',label=f'Closing stock of {kys}')
#         plt.title(f'opening and closing stock value of{kys} of starting 100 days ')
#         plt.legend()
#         plt.show()
#         plt.plot(df.High.head(100), marker='o', color='orange', label=f'High stock of {kys}')
#         plt.plot(df.Low.head(100), marker='o', color='blue', label=f'Low stock of {kys}')
#         plt.title(f'High  and Low stock value of {kys} of starting 100 days ')
#         plt.legend()
#         plt.show()
#         plt.plot(df.Open.head(100), marker='o', color='yellow', label=f'Opening stock of {kys}')
#         plt.plot(df.Volume.head(100), marker='o', color='orange', label=f'Volume stock of {kys}')
#         plt.title(f'opening and Volume stock value of {kys} of starting 100 days ')
#         plt.legend()
#         plt.show()
#         plt.plot(df.Open.head(100), marker='o', color='yellow', label=f'Opening stock of {kys}')
#         plt.plot(df.Date.head(100), marker='o', color='red', label=f'Date stock of {kys}')
#         plt.title(f'opening with Date stock value of {kys} of starting 100 days ')
#         plt.legend()
#         plt.show()
#         plt.plot(df.Close.head(100), marker='o', color='yellow', label=f'Close stock of {kys}')
#         plt.plot(df.Date.head(100), marker='o', color='Blue', label=f'Date stock of {kys}')
#         plt.title(f'Closing  and Date stock value of {kys} of starting 100 days ')
#         plt.legend()
#         plt.show()
#         plt.plot(df.Date.head(100), marker='o', color='Blue', label=f'Date stock of {kys}')
#         plt.plot(df.Volume.head(100), marker='o', color='orange', label=f'Volume stock of {kys}')
#         plt.title(f'Date and Volume stock value of {kys} of starting 100 days ')
#         plt.legend()
#         plt.show()
#         sn.boxplot(df[i])
#         plt.title(kys)
#         plt.legend()
#         plt.show()
#     sn.pairplot(data[data['Type']==kys])
#     plt.title(kys)
#     plt.legend()
#     plt.show()

# dados=pd.read_csv('wc_champions.csv')

# df = pd.DataFrame(data=dados,  columns=['champion', 'sum_total', 'lose_total', "winrate_total", "sum_bans", "ban_rate"])
# # df

# campeoes = df["champion"]
# quantidadePartidasJogadas = df["sum_total"]
# quantidadeDerrotas = df["lose_total"]
# quantidadeVitórias = []

# for i in range(len(quantidadePartidasJogadas)):
#   quantidadeVitórias.append(quantidadePartidasJogadas[i] - quantidadeDerrotas[i])


# for i in range(len(quantidadePartidasJogadas)):
#   print(f"Campeão:{campeoes[i]}\t\tPartidas:{quantidadePartidasJogadas[i]}\t\tWins: {quantidadeVitórias[i]}\t\tLoses: {quantidadeDerrotas[i]}")

# df
# for eachChamp in champions:
#   print(eachChamp)

# Importando bibliotecas
import matplotlib.pyplot as plt
import pandas as pd 
import math
import numpy as np

# Pegando dados
dados_csv = pd.read_csv("population_by_country_2020.csv")
x1_csv = dados_csv["Population (2020)"]
x2_csv = dados_csv["Density (P/Km²)"]
y_csv = dados_csv["Land Area (Km²)"]


x1, x2, y = [], [], []

for i in range(x_csv.shape[0]):
    x1.append(x1_csv[i])
    x2.append(x2_csv[i])
    y.append(y_csv[i])

# Gráfico de distribuição de X
plt.hist(x)
plt.show()

# Gráfico de distribuição de Y
plt.hist(y)
plt.show()

# Gráfico do Conjunto de Dados XY
plt.scatter(x,y)
plt.show()

# Coeficiente de Correlação
def CoeficienteCorrelacao(x, y):
  Sx = 0
  Sy = 0
  Sxy = 0
  Sxx = 0
  Syy = 0
  x_x_med = []
  y_y_med = []
  xx = []
  yy = []
  xy = []

  for i in range(len(x)):
      Sx += x[i]
      Sy += y[i]
  x_med = Sx/len(x)
  y_med = Sy/len(y)

  for i in range(len(x)):
      x_x_med.append((x[i] - x_med))
      y_y_med.append((y[i] - y_med))

  for i in range(len(x)):
      xx.append(x_x_med[i]**2)
      yy.append(y_y_med[i]**2)
      xy.append(y_y_med[i]*x_x_med[i])

  # Calculo do Rho
  for i in range(len(x)):
      Sxy += xy[i]
      Sxx += xx[i]
      Syy += yy[i]
  
  return { 'rho': Sxy / math.sqrt(Sxx*Syy), 'sxx': Sxx, 'sxy': Sxy, 'xMed': x_med, 'yMed': y_med} # RHO

print(f"O valor de RHO é: {CoeficienteCorrelacao(x,y)['rho']}")

"""## Hiperplano dos mínimos quadrados"""

# B1 = Sxy/Sxx
# B0 =y_med - B1*x_med
# sigma = Syy/len(x)

# print("A reta é -> y=",B0," + ",B1,"x")

"""## Calcula Beta Chapéu"""

def CalculaBeta(x, y):
  matrix = np.array(x)
  y = np.array(y)

  transposta = np.transpose(matrix)
  mult = np.dot(transposta,matrix)
  inversa = np.linalg.inv(mult)
  mult2 = np.dot(inversa, transposta)

  return np.dot(mult2,y) #Beta

print(f"""O valor de Beta é: {CalculaBeta([
      [1,31,4],
      [1,16,5],
      [1,29,3],
      [1,19,0],
      [1,27,2]
  ], [12,13,3,3,11])}""")