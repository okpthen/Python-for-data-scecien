from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""
    def __init__(self, firstname, is_alive=True):
        super().__init__(firstname, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self):
        self.is_alive = False

    def __str__(self):
        return f"Vevtor: ({self.family_name}, {self.eyes}, {self.hairs})"

    def __repr__(self):
        return self.__str__()


class Lannister(Character):
    def __init__(self, first_name: str, is_alive=True):
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def die(self):
        self.is_alive = False

    def create_lannister(first_name, is_alive=True):
        return Lannister(first_name, is_alive)

    def __str__(self) -> str:
        return f'Vector: ({self.family_name}, {self.eyes}, {self.hairs})'

    def __repr__(self):
        return self.__str__()
