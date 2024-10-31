from load_image import ft_load
from PIL import Image
from pimp_image import ft_invert, ft_red, ft_blue, ft_green, ft_grey


def ft_print_image(array, str):
    image = Image.fromarray(array)
    file_name = "pictures/" + str + ".png"
    image.save(file_name)


array = ft_load("landscape.jpg")
ft_print_image(array, "original")
ft_print_image(ft_invert(array), "invet")
ft_print_image(ft_red(array), "red")
ft_print_image(ft_blue(array), "blue")
ft_print_image(ft_green(array), "green")
ft_print_image(ft_grey(array), "grey")
