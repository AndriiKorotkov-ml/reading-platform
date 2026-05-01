from .base import User

class PremiumUser(User):
    def read(self, content):
        return f"Premium: {content.display()}"