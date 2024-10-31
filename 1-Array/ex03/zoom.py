# from PIL import Image
# import numpy as np
# import scipy as sp
# from load_image import ft_load

# def ft_zoom(path: str, pix: int):
#     img = Image.open(path)
#     # img = img.convert('L').rotate(90)
#     img_array = np.array(img)
#     w, h = img_array.shape[:2]
#     w_start = 450
#     h_start = 100
#     zoom_image = img.crop((w_start, h_start, w_start + pix, h_start + pix))
#     zoom_image = zoom_image.convert('L')
#     # zoom_image = zoom_image.convert('L').rotate(90)
#     # zoom_image = zoom_image.transpose(method=Image.FLIP_TOP_BOTTOM)

#     # zoom_image_array = np.array(zoom_image)
#     zoom_image_array = np.squeeze(zoom_image)

#     zoom_image.save("animal1.jpeg")
#     print("My shape of image is ", zoom_image_array.shape)
#     return zoom_image_array


# def main():
#     ft_load("animal.jpeg")
#     print(ft_zoom("animal.jpeg", 400))

# if __name__ == "__main__":
#     main()
from load_image import ft_load


def trim(array, x, y, width, height, depth=3):
    return array[y:y+width, x:x+height, :depth]


def main():
    try:
        image = ft_load('animal.jpeg')
    except Exception as e:
        print(e)
        exit()

    print(image)

    image = trim(image, 450, 100, 400, 400, 1)

    print(f'New shape after slicing: {image.shape}', end='')
    print(f' or ({image.shape[0]}, {image.shape[1]})')
    print(image)


if __name__ == "__main__":
    main()
