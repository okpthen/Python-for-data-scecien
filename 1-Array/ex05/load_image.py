from PIL import Image
import numpy as np


def ft_load(path: str):
    img = Image.open(path)
    img = np.array(img)
    print("My shape of image is ", img.shape)
    return img
