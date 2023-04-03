import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Dane wejściowe
X = np.array([[2000], [2002], [2005], [2007], [2010]])
y = np.array([6.5, 7.0, 7.4, 8.2, 9.0])

# Model regresji liniowej
model = LinearRegression().fit(X, y)

# Przewidywanie ile będzie wynosić bezrobocie w danym roku
rok = 2022
y_pred = model.predict([[rok]])

# Wyświetlenie wyników
print("Współczynnik nachylenia (w1):", round(model.coef_[0], 3))
print("Współczynnik przesunięcia (w0):", round(model.intercept_, 3))
print("R^2 score:", round(model.score(X, y), 3))
print("Przewidując w roku "+str(rok)+" bezrobocie będzie wynosić:",round(y_pred[0],1))

#Określanie w którym roku bezrobocie przekroczy 12%
proc_wyliczany = 12

okreslanie =(proc_wyliczany+(model.intercept_*(-1)))/model.coef_[0]
print("Bezrobocie przekroczy "+str(proc_wyliczany)+"% w", int(round(okreslanie,0)))

# Wykres regresji liniowej
plt.scatter(X, y)
plt.plot(X, model.predict(X), color='red')
plt.title("Regresja liniowa procentu bezrobotnych")
plt.xlabel("Rok")
plt.ylabel("Procent bezrobotnych")
plt.show()
