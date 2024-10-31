from load_image import ft_load
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def main():
    try:
        image = ft_load('../animal.jpeg')
    except Exception as e:
        print(e)
        exit()

    print(image)
    image = Image.fromarray(image)
    image = image.crop((450, 100, 850, 500))
    array = np.array(image)
    array = array[:, :, :1]

    print(f'New shape after slicing: {array.shape}', end='')
    print(f' or ({array.shape[0]}, {array.shape[1]})')
    print(array)
    plt.imshow(array, "gray")
    plt.savefig('picture/output_image.png')


if __name__ == "__main__":
    main()
