from abc import ABC,abstractmethod
class User(ABC):
    @abstractmethod
    def read(self,content):
        pass