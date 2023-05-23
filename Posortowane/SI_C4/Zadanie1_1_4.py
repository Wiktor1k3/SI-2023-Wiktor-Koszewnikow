import pandas as pd
import numpy as np

def calculate_reduct(C, D):
    num_attributes = C.shape[1]
    reduct = set(range(num_attributes))
    reduct_copy = reduct.copy()
    changed = True

    while changed:
        changed = False

        for attr in reduct_copy:
            reduct.remove(attr)
            if is_reduct(C, D, reduct):
                changed = True
            else:
                reduct.add(attr)

        reduct_copy = reduct.copy()

    return list(reduct)


def is_reduct(C, D, reduct):
    for i in range(C.shape[0]):
        for j in range(i+1, C.shape[0]):
            if np.array_equal(C[i, list(reduct)], C[j, list(reduct)]) and D[i] != D[j]:
                return False

    return True


fig1 = pd.DataFrame({
    'b': [2, 2, 0, 1],
    'c': [1, 2, 2, 1],
    'd': [0, 1, 1, 1],
    'dec': [0, 1, 2, 1]
})

fig2 = pd.DataFrame({
    'a1': ['wysoka', 'wysoka', 'wysoka', 'więcej niż średnia', 'więcej niż średnia', 'więcej niż średnia', 'wysoka', 'więcej niż średnia', 'więcej niż średnia'],
    'a2': ['bliski', 'bliski', 'bliski', 'daleki', 'daleki', 'daleki', 'bliski', 'daleki', 'daleki'],
    'a3': ['średni', 'średni', 'średni', 'silny', 'silny', 'lekki', 'średni', 'lekki', 'lekki'],
    'dec': ['tak', 'tak', 'tak', 'nie pewne', 'nie', 'nie', 'tak', 'nie', 'tak']
})

reduct2 = calculate_reduct(fig2.iloc[:, :-1].values, fig2.iloc[:, -1].values.flatten())

print("Zadanie 1.4: Redukt decyzyjny dla Fig2:", reduct2)
