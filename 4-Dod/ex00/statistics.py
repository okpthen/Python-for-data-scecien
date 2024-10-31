from typing import Any


def ft_var(array, ave):
    total = 0.0
    for x in array:
        a = (ave - x) * (ave - x)
        total += a
    return total / len(array)


def quartile(array):
    n = len(array)
    if n % 4 == 0:
        q1 = (array[n // 4 - 1] + array[n // 4]) / 2
    else:
        q1 = array[n // 4]
    if n % 4 == 0:
        q3 = (array[3 * n // 4 - 1] + array[3 * n // 4]) / 2
    else:
        q3 = array[3 * n // 4]
    return [float(q1), float(q3)]


def median(array):
    mid = len(array) // 2
    if len(array) % 2 == 1:
        return array[mid]
    else:
        return (array[mid] + array[mid - 1]) / 2


def ft_statistics(*args: Any, **kwargs: Any):
    if not args:
        for _ in kwargs.items():
            print("ERROR")
        return
    data = list(args)
    data.sort()
    ave = sum(data) / len(data)
    variance = ft_var(data, ave)
    if "mean" in kwargs.values():
        print("mean :", ave)
    if "median" in kwargs.values():
        print("median", median(data))
    if "quartile" in kwargs.values():
        print("quartile :", quartile(data))
    if "std" in kwargs.values():
        print("std :", variance ** 0.5)
    if "var" in kwargs.values():
        print("var :", variance)
