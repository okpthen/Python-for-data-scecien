import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float]):
    if len(height) != len(weight):
        raise ValueError("Error: element must be same length")
    if type(height) is not list or type(weight) is not list:
        raise ValueError('Height and weight must be lists')
    a = np.array(height)
    b = np.array(weight)
    for h, w in zip(height, weight):
        if not isinstance(h, (float, int)) or not isinstance(w, (float, int)):
            raise TypeError("Height and weight must be integers or floats.")
        if h <= 0 or w <= 0:
            raise ValueError("Height and weight values must be positive.")
    ans = b / (a * a)
    return ans.tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    return [x > limit for x in bmi]
