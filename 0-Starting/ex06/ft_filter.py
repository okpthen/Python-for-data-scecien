def ft_filter(funk, ite):
    if funk:
        return (item for item in ite if funk(item))
    return (item for item in ite if item)
