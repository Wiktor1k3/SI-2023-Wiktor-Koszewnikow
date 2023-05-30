import itertools

def find_rules(decision_system):
    rules = []

    while decision_system:  # Dopóki system decyzyjny nie jest pusty
        found = False  # Flaga pomocnicza do zakończenia iteracji
        for row in decision_system:
            attributes = range(len(row) - 1)  # Indeksy atrybutów
            for length in range(1, len(attributes) + 1):  # Długość kombinacji atrybutów
                if found:  # Jeżeli znaleziono regułę w bieżącej iteracji
                    break  # Przerwij pętlę
                for combination in itertools.combinations(attributes, length):  # Generowanie kombinacji atrybutów
                    rule = {i: row[i] for i in combination}  # Tworzenie reguły na podstawie kombinacji
                    rule[-1] = row[-1]  # Dodanie wartości decyzji do reguły
                    rules.append(rule)  # Dodanie reguły do listy reguł
                    decision_system = [r for r in decision_system if not all(rule[i] == r[i] for i in rule)]  # Usunięcie wierszy spełniających warunki reguły
                    found = True  # Ustawienie flagi, że znaleziono regułę
                    break

    return rules


decision_system = [
    [1, 1, 1, 1, 3, 1, 1],
    [1, 1, 1, 1, 3, 2, 1],
    [1, 1, 1, 3, 2, 1, 0],
    [1, 1, 1, 3, 3, 2, 1],
    [1, 1, 2, 1, 2, 1, 0],
    [1, 1, 2, 1, 2, 2, 1],
    [1, 1, 2, 2, 3, 1, 0],
    [1, 1, 2, 2, 4, 1, 1]
]

rules = find_rules(decision_system)
print("Reguły:")
for rule in rules:
    print(rule)
