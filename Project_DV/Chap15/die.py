from random import randint

class Die():
    """A Class represt single die"""
    def __init__(self, num_sides=6):
        """Assume 6 side die """
        self.num_sides= num_sides

    def roll(self):
        """Reuturn random number from 1 to num_sides"""
        return randint(1, self.num_sides)
