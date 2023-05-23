import math

def all_same_class(data, target_attribute):
    """
    Sprawdza, czy wszystkie przykłady w zbiorze danych mają tę samą wartość dla atrybutu docelowego.
    """
    class_value = data[0][target_attribute]
    for example in data:
        if example[target_attribute] != class_value:
            return False
    return True


def majority_class(data, target_attribute):
    """
    Zwraca najczęściej występującą klasę w zbiorze danych.
    """
    class_counts = {}
    for example in data:
        class_value = example[target_attribute]
        if class_value in class_counts:
            class_counts[class_value] += 1
        else:
            class_counts[class_value] = 1
    return max(class_counts, key=class_counts.get)


def entropy(data, target_attribute):
    """
    Oblicza entropię zbioru danych.
    """
    class_counts = {}
    for example in data:
        class_value = example[target_attribute]
        if class_value in class_counts:
            class_counts[class_value] += 1
        else:
            class_counts[class_value] = 1

    entropy_value = 0
    total_examples = len(data)
    for count in class_counts.values():
        probability = count / total_examples
        entropy_value -= probability * math.log2(probability)

    return entropy_value


def information_gain(data, attribute, target_attribute):
    """
    Oblicza przyrost informacji dla podziału zbioru danych na podstawie danego atrybutu.
    """
    attribute_values = set(example[attribute] for example in data)
    total_examples = len(data)
    remainder = 0

    for value in attribute_values:
        subset = [example for example in data if example[attribute] == value]
        subset_entropy = entropy(subset, target_attribute)
        subset_probability = len(subset) / total_examples
        remainder += subset_entropy * subset_probability

    return entropy(data, target_attribute) - remainder


def choose_best_attribute(data, attributes, target_attribute):
    """
    Wybiera atrybut o najwyższym przyroście informacji.
    """
    best_attribute = None
    best_gain = -1

    for attribute in attributes:
        gain = information_gain(data, attribute, target_attribute)
        if gain > best_gain:
            best_gain = gain
            best_attribute = attribute

    return best_attribute


def partition_data(data, attribute):
    """
    Dzieli zbiór danych na podstawie wartości danego atrybutu.
    """
    partitions = {}
    for example in data:
        value = example[attribute]
        if value in partitions:
            partitions[value].append(example)
        else:
            partitions[value] = [example]
    return partitions


def decision_tree_learning(data, attributes, target_attribute, default_decision=None):
    """
    Algorytm Decision-Tree-Learning do nauki drzewa decyzyjnego.
    """
    # Sprawdź warunek zatrzymania
    if len(data) == 0:
        # Brak danych, zwróć domyślną decyzję
        return default_decision
    elif all_same_class(data, target_attribute):
        # Wszystkie przykłady mają tę samą klasę, zwróć tę klasę
        return data[0][target_attribute]
    elif len(attributes) == 0:
        # Brak atrybutów do podziału, zwróć najczęściej występującą klasę
        return majority_class(data, target_attribute)
    else:
        # Wybierz atrybut do podziału
        best_attribute = choose_best_attribute(data, attributes, target_attribute)

        # Utwórz nowe poddrzewo decyzyjne
        tree = {best_attribute: {}}

        # Podziel dane na podstawie wybranego atrybutu
        partitions = partition_data(data, best_attribute)

        # Rekurencyjnie wywołaj algorytm dla każdej partycji
        for value, partition in partitions.items():
            subtree = decision_tree_learning(partition, attributes - {best_attribute}, target_attribute,
                                             default_decision)
            tree[best_attribute][value] = subtree

        return tree


# Dane wejściowe
data = [
    {'a1': 1, 'a2': 0, 'a3': 0, 'dec': 0},
    {'a1': 1, 'a2': 0, 'a3': 1, 'dec': 0},
    {'a1': 0, 'a2': 1, 'a3': 0, 'dec': 0},
    {'a1': 1, 'a2': 1, 'a3': 1, 'dec': 1},
    {'a1': 1, 'a2': 1, 'a3': 0, 'dec': 1}
]

# Lista atrybutów
attributes = {'a1', 'a2', 'a3'}

# Atrybut decyzyjny
target_attribute = 'dec'

# Utwórz drzewo decyzyjne
decision_tree = decision_tree_learning(data, attributes, target_attribute)

# Wyświetl drzewo decyzyjne
print(decision_tree)
