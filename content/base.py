from abc import ABC,abstractmethod
class Content(ABC):
    @abstractmethod
    def display(self):
        pass