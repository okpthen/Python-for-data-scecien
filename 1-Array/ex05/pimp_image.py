import numpy as np

def ft_invert(array):
    return 255 - array


def ft_red(array):
    red_array = array.copy()
    red_array[..., 1] = 0
    red_array[..., 2] = 0
    return red_array
def ft_green(array):
    green_array = array.copy()
    green_array[..., 0] = 0
    green_array[..., 2] = 0
    return green_array
def ft_blue(array):
    blue_array = array.copy()
    blue_array[..., 0] = 0
    blue_array[..., 1] = 0
    return blue_array

def ft_grey(array):
    grey_array = array.copy()
    weights = np.array([0.2989, 0.5870, 0.1140])
    grey = np.dot(array[..., :3], weights)
    grey_array[..., 0] = grey
    grey_array[..., 1] = grey
    grey_array[..., 2] = grey
    return grey_array