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


# Przykładowy system decyzyjny
C = np.array([
    [1, 0, 0, 1, 1],
    [0, 1, 0, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [1, 1, 1, 0, 0]
])

D = np.array([
    [1],
    [0],
    [1],
    [0],
    [1],
    [1]
])

reduct = calculate_reduct(C, D)
print("Minimalny redukt:", reduct)
