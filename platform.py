from users.base import User
from recommendation.base import Recommendation
class ReadingPlatform:
    def __init__(self, user: User, recommendation: Recommendation):
        self.user = user
        self.recommendation = recommendation
        self.history = []
    def read_content(self, content):
        result = self.user.read(content)
        self.history.append(content)
        return result
    def get_recommendations(self):
        return self.recommendation.suggest()
    def get_history(self):
        return [item.__class__.__name__ for item in self.history]
    def clear_history(self):
        self.history.clear()
    def change_user(self, user: User):
        self.user = user
    def get_statistics(self):
        return {
            "total_read": len(self.history)
        }