from abc import ABC,abstractmethod
class AbstractClass:
    @abstractmethod
    def add(self):
        pass

class inheritorofAbstractClass(AbstractClass):
    def add(self,a,b):
       return a+b