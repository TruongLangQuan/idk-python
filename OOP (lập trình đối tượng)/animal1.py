#Đa hình trong python
class animal:
    def sound(self):
        return "idk"
    
class cat(animal):
    def sound(self):
        return "Meo"
    
class dog(animal):
    def sound(self):
        return "Gâu"
    
animals = [cat(),dog()]
for animal in animals:
    print(animal.sound())