import numpy as np


# definicja funkcji aktywacji
def step(x):
    return 1 if x >= 0 else 0


# definicja perceptronu
class Perceptron:
    def __init__(self, weights, bias):
        self.weights = weights
        self.bias = bias

    def feedforward(self, inputs):
        # suma ważona wejść i wag
        weighted_sum = np.dot(inputs, self.weights) + self.bias
        # zwrócenie wyniku po przejściu przez funkcję aktywacji
        return step(weighted_sum)


# definicja wag i progu aktywacji
weights = np.array([1, -1])
bias = -0.1

# stworzenie perceptronu
perceptron = Perceptron(weights, bias)

# testowanie perceptronu na wejściach (1,0) - powinno zwrócić 1
inputs = np.array([1, 0])
print(perceptron.feedforward(inputs))

# testowanie perceptronu na wejściach (0,0) - powinno zwrócić 0
inputs = np.array([0, 0])
print(perceptron.feedforward(inputs))
