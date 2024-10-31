def ft_filter(func, it):
    if not func:
        return (item for item in it if item)
    else:
        return (item for item in it if func(item))


def count_in_list(lst: list, s: str):
    return len(list(ft_filter(lambda x: x == s, lst)))
