from load_image import ft_load
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


def transpose(img_array):
    rotated_img = []
    for x in range(img_array.shape[1]):  # iterate over the columns

        row = []
        for y in range(img_array.shape[0]):  # iterate over the rows
            row.append(img_array[y][x][0])
        rotated_img.append(row)

    return np.array(rotated_img)


def main():
    try:
        image = ft_load('../animal.jpeg')
    except Exception as e:
        print(e)
        exit()

    # image = trim(image, 450, 100, 400, 400, 1)

    image = Image.fromarray(image)
    image = image.crop((450, 100, 850, 500))
    # image.show()
    array = np.array(image)
    array = array[:, :, :1]

    print(f'The shape of image is: {array.shape}', end='')
    print(f' or ({array.shape[0]}, {array.shape[1]})')
    print(array)

    new = array.squeeze()
    print("New shape after Transpose: ", new.shape)
    print(new)
    array = transpose(array)
    plt.imshow(array, "gray")
    plt.savefig('picture/output_image.png')


if __name__ == "__main__":
    main()
