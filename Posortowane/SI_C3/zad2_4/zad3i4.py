import numpy as np


# Funkcja aktywacji
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


# Wejścia sieci
inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])

# Oczekiwane wyniki
targets = np.array([[0], [1], [1], [0]])

# Wagi warstwy ukrytej
hidden_weights = np.random.uniform(size=(2, 2))

# Wagi warstwy wyjściowej
output_weights = np.random.uniform(size=(2, 1))

# Współczynnik uczenia
learning_rate = 0.1

# Liczba epok
epochs = 10000

# Trenowanie sieci
for i in range(epochs):
    # Propagacja w przód
    hidden_layer_activation = sigmoid(np.dot(inputs, hidden_weights))
    output_layer_activation = sigmoid(np.dot(hidden_layer_activation, output_weights))

    # Obliczanie błędów
    output_layer_error = targets - output_layer_activation
    hidden_layer_error = np.dot(output_layer_error, output_weights.T) * hidden_layer_activation * (
                1 - hidden_layer_activation)

    # Propagacja wsteczna
    output_weights += learning_rate * np.dot(hidden_layer_activation.T, output_layer_error)
    hidden_weights += learning_rate * np.dot(inputs.T, hidden_layer_error)

# Testowanie sieci
print("Dane:  Wynik:")
test_inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
for i in range(len(test_inputs)):
    hidden_layer_activation = sigmoid(np.dot(test_inputs[i], hidden_weights))
    output_layer_activation = np.round(sigmoid(np.dot(hidden_layer_activation, output_weights)),0)
    inter = int(output_layer_activation)
    print(test_inputs[i],"  ",inter)


