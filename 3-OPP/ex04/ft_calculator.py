class calculator:
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        print("Dot product is:", sum(x * y for x, y in zip(V1, V2)))

    def add_vec(V1: list[float], V2: list[float]) -> None:
        # result =  [float(x + y) for x, y in zip(V1, V2)]
        print("Add Vector is :", [float(x + y) for x, y in zip(V1, V2)])

    def sous_vec(V1: list[float], V2: list[float]) -> None:
        # result = [float(x - y) for x, y in zip(V1, V2)]
        print("Sous Vector is:", [float(x - y) for x, y in zip(V1, V2)])
