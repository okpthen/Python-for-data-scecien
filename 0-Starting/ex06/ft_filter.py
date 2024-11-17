def ft_filter(funk, ite):
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    if funk:
        return (item for item in ite if funk(item))
    return (item for item in ite if item)
