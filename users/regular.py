from .base import User
class Regular(User):
    def read(self,content):
        return f"{content.display()}"