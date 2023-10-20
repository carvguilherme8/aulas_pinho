class Animal:
    """
    This is the base class for all animals
    """
    def __init__(self, name, species):
        """
        Constructor to initialize an animal object

        Args:
            name (str): The name of the animal
            species (str): The sécies of the animal
        """

        self.name = name
        self.species = species

    def speak(self):
        """
        Make the animal speak.

        Returns:
            str: A message representing the animal's speech
        """
        return f"{self.name} says Hi!"
    
    def __str__(self):
        """
        String representation of the animal

        Returns:
            str: A string with the animal's name and species
        """
        return f"{self.name} {self.species}"
    
    #se você não define sua classe str, o python terá uma padrão

    # def __repr__(self):
    #     pass


class Dog(Animal):
    """
    A class representing a Dog, interiting from the animal class
    """
    def __init__(self, name, breed):
        """
        Constructor to initialize a Dog object.

        Args:
            name (str): The name of the animal.
            breed (str): The breed of the dog
        """
        super().__init__(name, species="Dog") #puxa da classe mãe
        self.breed = breed


    def speak(self):
        """"
            Make the Dog bark

        Retuns
        ------
            str: A message representing the dog's bark.
        """
        return f"{self.name} barks. Woof!"
    
    def wag_tail(self):
        """
            Make the Dog wags its tail.

        Returns
        -------
            str: A message representing the dog wagging its tail.
        """
        return f"{self.name} wags its tail."

class Cat(Animal):
    """
    A class representing a Cat, interiting from the animal class
    """
    def __init__(self, name, color):
        """
        Constructor to initialize a Cat object.

        Args:
            name (str): The name of the animal.
            color (str): The color of the cat
        """
        super().__init__(name, species="Cat") #puxa da classe mãe
        self.color = color


    def speak(self):
        """"
            Make the Dog meows

        Retuns
        ------
            str: A message representing the cat's meow.
        """
        return f"{self.name} meows"
    
    def purr(self):
        """
            Make the Cat purr.

        Returns
        -------
            str: A message representing the cat purring.
        """
        return f"{self.name} purrs"
    
#Create instances of Dog and Cat classes
my_dog = Dog("Nick", "Vira-lata")
my_cat = Cat("Milk", "Black")

#Call methods to demonstrate functionality
print(my_dog.speak())
print(my_dog.wag_tail())
print(my_cat.speak())
print(my_cat.purr())

#Display information about the animals
print(my_dog)
print(my_cat)