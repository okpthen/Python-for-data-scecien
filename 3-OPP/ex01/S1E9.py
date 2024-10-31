from abc import ABC, abstractmethod


class Character(ABC):
    def __init__(self, firstname: str, is_alive: bool = True):
        """Your docstring for Constructo"""
        self.first_name = firstname
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        pass


class Stark(Character):
    """Your docstring for Class"""
    def die(self):
        """Your docstring for Method"""
        self.is_alive = False
