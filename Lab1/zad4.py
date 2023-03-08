import numpy as np
import pandas as pd


plik = np.loadtxt("australian.txt")
plik2 = "australian-type.txt"

#  4 a)

plik4 = pd.read_csv("australian.txt", header=None, sep=" ")
stracone = plik4.mask(np.random.random(plik4.shape) <= 0.1)
stracone = stracone.fillna('?')
najczestsze = stracone.mode()
print("\nPrzed zamianą:")
print(stracone)
print("\nNajczęściej występująca wartość:")
najczestsze = plik4.mode()
print(plik4.mode())
print("\nPo zamianie:")
zamiana = stracone.replace("?", najczestsze.iloc[0])
print(zamiana)

# 4 b)

przedzialy = [(-1, 1), (0, 1), (-10, 10)]
tab = np.loadtxt(plik2,dtype=str,usecols=1)=='n'
tab2=[]
for i in range(len(tab)):
    if tab[i]==True:
        tab2.append(i)

for przedzial in przedzialy:
    ai, bi = przedzial
    i=0
    print("Przedział",przedzialy[i],":")
    for a in tab2:
        normalizacja = (((plik[:,a] - np.min(plik[:,a])) * (bi - ai))/ (np.max(plik[:,a]) - np.min(plik[:,a]))) + ai
        print("\nNormalizacja Atrybutu",a,":\n",normalizacja)
    i=i+1

# 4 c)

standaryzacja = (plik - np.mean(plik, axis=0)) / np.std(plik, axis=0)
print("\nPo standaryzacji:",standaryzacja)

srednie = np.mean(standaryzacja, axis=0)
print("\nŚrednie wartości atrybutów po standaryzacji:", srednie)

wariancje = np.var(standaryzacja, axis=0)
print("\nWariancje atrybutów po standaryzacji:", wariancje)

# 4 d)
plik4 = "Churn_Modelling.csv"
df = pd.read_csv(plik4, index_col=0)
print(df.head().to_string())

df_dummied = pd.get_dummies(df, columns=['Geography'])
df_dummied.drop('Geography_Germany', inplace=True, axis=1)
print(df_dummied.head().to_string())