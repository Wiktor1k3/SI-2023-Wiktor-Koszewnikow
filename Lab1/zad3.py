import numpy as np

plik = "australian.txt"
plik_dane = np.loadtxt(plik, dtype=str)
plik2 = "australian-type.txt"

# a)
print("\n--------3_A:---------")
decyzyjne = set(np.loadtxt(plik,dtype=str,usecols=14))
print(decyzyjne)
print(" ")

# b)
print("--------3_B:---------")
elem_0 = np.count_nonzero(np.loadtxt(plik,dtype=float,usecols=14)==0)
elem_1 = np.count_nonzero(np.loadtxt(plik,dtype=float,usecols=14)==1)

print("Elemety z 0:" ,elem_0, "\nElemety z 1:" , elem_1 )
print(" ")

# c)
print("--------3_C:---------")
tab = np.loadtxt(plik2,dtype=str,usecols=1)=='n'
for i in range(len(tab)):
    if tab[i]==True:
        print('Max atrybut ',i+1,": ",max(np.loadtxt(plik,dtype=float,usecols=i)))
        print('Min atrybut ',i+1,": ",min(np.loadtxt(plik,dtype=float,usecols=i)))


# d)
print("--------3_D:---------")
for i in range(14):
    at = len(np.unique(np.loadtxt(plik, dtype=float, usecols=i)))
    print("Liczba unikalnych wartości atrybutu", i+1, ": ",at)
print(" ")

# e)
print("--------3_E:---------")
for i in range(14):
    at = set(np.unique(np.loadtxt(plik, dtype=float, usecols=i)))
    print("Unikalne wartości atrybutu", i+1, ": ",at)
print(" ")

# f)
print("--------3_F:---------")
print("Odchylenie standardowe atrybutów numerycznych:")
tab = np.loadtxt(plik2,dtype=str,usecols=1)=='n'
for i in range(len(tab)):
    if tab[i]==True:
        print('Atrybut ',i+1,": ",np.std(np.loadtxt(plik,dtype=float,usecols=i)))

print("\nOdchylenie standardowe klas decyzyjnych:")
print("Klasy decyzyjne: ",np.std([elem_0,elem_1]))