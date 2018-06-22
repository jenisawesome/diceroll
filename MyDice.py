import random

class MyDice:

    def roll(self, sides):
        return random.randint(1,sides)

    def multidice(self, num,sides):
        """Returns a list of dice rolls when given the number of dice and the number of sides"""
        rolls = []
        for x in range(num):
            rolls.append(random.randint(1, sides))
        return rolls