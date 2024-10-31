from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt


def trim(array, x, y, width, height, depth=3):
    return array[y:y+width, x:x+height, :depth]


def rotate(array):
    return np.asarray(list(list(x) for x in zip(*array))[::-1])


def main():

    try:
        image = ft_load('animal.jpeg')
    except Exception as e:
        print(e)
        exit()

    image = trim(image, 450, 100, 400, 400, 1)

    print(f'The shape of the image is: {image.shape}', end='')
    print(f' or ({image.shape[0]}, {image.shape[1]})')
    print(image)

    image = rotate(image)

    print(f'New shape after Transpose: ({image.shape[0]}, {image.shape[1]})')
    print(image)

if __name__ == "__main__":
    main()
