class Dog:
    """This class provide Dog actions"""
    def __init__(self, name, age):
        """Initize name and age of dog """
        self.name = name
        self.age = age

    def sit(self):
        """Action when dog sit """
        print(self.name.titile() + " is sitting down")

    def roll_over(self):
        """This function provide when dog rollover """
        print(self.name.title() + " is rolled over")

my_dog = Dog("tommy", 8)        
print("My dog name is " + my_dog.name.title())
print("My dog age is " + str(my_dog.age))