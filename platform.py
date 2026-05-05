
class ReadingPlatform:
    def __init__(self, user, recommendation):
        self.user = user
        self.recommendation = recommendation
        self.history = []

    def read_content(self, content):
        result = self.user.read(content)
        self.history.append(content.__class__.__name__)
        return result

    def get_recommendations(self):
        return self.recommendation.suggest()

    def get_history(self):
        return self.history