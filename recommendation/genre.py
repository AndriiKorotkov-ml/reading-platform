from .base import Recommendation
import random
from typing import Dict,Any
class Genre(Recommendation):
    def __init__(self):
        self.__data = {
            "fantasy": ["The Hobbit", "Harry Potter"],
            "sci-fi": ["Dune", "Foundation"],
            "romance": ["Pride and Prejudice", "Me Before You"]
        }

    def suggest(self):
        genre = random.choice(list(self.__data.keys()))
        recommend = random.choice(self.__data[genre])
        return {"genre":genre,"recommendation":recommend}