class Dog: 
    kennel = 0 
    def __init__(self, breed): 
        self.breed = breed 
        Dog.kennel += 1 
    def __str__(self): 
    return self.breed + " says: Woof!" 


class SheepDog(Dog): 
    def __str__(self): 
        return super().__str__() + " Don't run away, Little Lamb!" 

    
class GuardDog(Dog): 
    def __str__(self): 
    return super().__str__() + " Stay where you are, Mister Intruder!"


class LowlandDog(SheepDog):
    def __str__(self):
        return Dog.__str__(self) + " I don't like mountains!" 

if __name__ == "__main__":
    rocky = SheepDog("Collie") 
    luna = GuardDog("Dobermann") 

    print(rocky) # Collie says: Woof! Don't run away, Little Lamb!
    print(luna) # Dobermann says: Woof! Stay where you are, Mister Intruder!

    print(issubclass(SheepDog, Dog), issubclass(SheepDog, GuardDog)) # True False
    print(isinstance(rocky, GuardDog), isinstance(luna, GuardDog)) # False True

    print(luna is luna, rocky is luna) # True False
    print(rocky.kennel) # 2
