#Trừu tượng trong Python
from abc import ABC, abstractmethod
class animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class dog(animal):
    def sound(self):
        return "GÂU"
    
class cat(animal):
    def sound(self):
        return "MÈO MÉO MEO MÈO MEO"
    
cat = cat()
dog = dog()

print(cat.sound())
print(dog.sound())