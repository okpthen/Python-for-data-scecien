import numpy as np


def slice_me(family: list, start: int, end: int):
    if type(family) is not list:
        raise ValueError("Family must be a list")
    family = np.array(family)
    print("My shape is ", family.shape)
    family = family[start:end]
    print("My nwe shape is ", family.shape)
    return family.tolist()
