import numpy as np


def perceptron_learn(perceptron, examples, alpha, max_iterations):

    for i in range(max_iterations):
        delta_w = np.zeros_like(perceptron.weights)
        for x, y in examples:
            if y == 1 and perceptron(x) == 0: # przykład należy do funkcji AND
                delta_w += alpha * np.array(x)
            elif y == 0 and perceptron(x) == 1: # przykład należy do funkcji NOT
                delta_w += -alpha * np.array(x)
        perceptron.weights += delta_w
        if not np.any(delta_w):
            print(f"Algorytm nauczania zakończony po {i} iteracjach.")
            break
    return perceptron


class Perceptron:
    def __init__(self, weights):
        self.weights = weights

    def __call__(self, x):
        return np.dot(x, self.weights) > 0


and_examples = [((0, 0), 0), ((0, 1), 0), ((1, 0), 0), ((1, 1), 1)]
not_examples = [((0,), 1), ((1,), 0)]

and_perceptron = Perceptron(np.zeros(2))
and_perceptron = perceptron_learn(and_perceptron, and_examples, 0.1,100)
print("AND perceptron weights:", and_perceptron.weights)

not_perceptron = Perceptron(np.zeros(1))
not_perceptron = perceptron_learn(not_perceptron, not_examples, 0.1,100)
print("NOT perceptron weights:", not_perceptron.weights)
