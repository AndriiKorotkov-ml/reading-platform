from .base import Recommendation
class Trend(Recommendation):
    def __init__(self):
        self.trending_data = {
            "The Hobbit": 95,
            "Harry Potter": 98,
            "Dune": 97,
            "Foundation": 85,
            "Pride and Prejudice": 80,
            "Me Before You": 88
                }
    def suggest(self):
        best = max(self.trending_data, key=self.trending_data.get)
        return {"trending": best}