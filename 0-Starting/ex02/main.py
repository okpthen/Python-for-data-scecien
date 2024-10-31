import find_ft_type

ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}
find_ft_type.all_thing_is_obj(ft_list)
find_ft_type.all_thing_is_obj(ft_tuple)
find_ft_type.all_thing_is_obj(ft_set)
find_ft_type.all_thing_is_obj(ft_dict)
find_ft_type.all_thing_is_obj("Brian")
find_ft_type.all_thing_is_obj("Toto")
print(find_ft_type.all_thing_is_obj(10))