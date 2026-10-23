import pandas as pd
import numpy as np

def boxplot(coluna):
    q1 = np.percentile(coluna, 25)
    q2 = np.percentile(coluna, 50)
    q3 = np.percentile(coluna, 75)

    print("Primeiro Quartil\n")
    print(q1)
    print("\nMediana\n")
    print(q2)
    print("\nTerceiro Quartil\n")
    print(q3)

    i = q3 - q1
    Limite_inferior = q1 - 1.5 * i

    Limite_max = q3 + 1.5 * i

    outliers = coluna[(coluna < Limite_inferior) | (coluna > Limite_max)]

    dentro = coluna[(coluna >= Limite_inferior) & (coluna <= Limite_max)]
    bigode_inf = dentro.min()
    bigode_sup = dentro.max()

    print("Limite inferior: \n")
    print(Limite_inferior)
    print("\nLimite Superior: \n")
    print(Limite_max)
    print("\nOutliers: \n")
    print(outliers)
    print("\nBigode inferior: \n")
    print(bigode_inf)
    print("\nbigode superior: \n")
    print(bigode_sup)

df = pd.read_csv(r"C:\Users\patrick.loureiro\Documents\Aulas\funcionarios - Null.csv")

print(df.isna().sum())

print("\n")


dfPreenchido = df.fillna({'departamento': "nenhum", 'lucro': 0}) 

print(dfPreenchido.isna().sum())

print("\n")

lucro = dfPreenchido["lucro"].to_numpy()
salario = dfPreenchido["salario"].to_numpy()

print(lucro)
print("\n")
print(salario)
print("\n")

print("Calculo de boxplot do lucro: \n")
boxplot(lucro)
print("\nCalculo de boxplot do salario: ")
boxplot(salario)



