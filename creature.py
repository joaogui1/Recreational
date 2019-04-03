import numpy as np
np.random.seed()

def crossover(cr1, cr2):
    pass

class Creature(object):
    """docstring for ."""
    def __init__(self, board, genome=None):
        if genome is None:
            self.genome = np.random.randint(0, 2, size=10)

        self.reach = 1 + self.genome[0]
        self.speed = 1 + self.genome[1]
        self.senses = 1 + self.genome[2]
        self.health = 5*(1 + self.genome[3])
        self.stamina = 12*(1 + self.genome[4])
        self.strenght = 1 + self.genome[5]
        self.aggression = 1 + self.genome[6]
        self.attractivness = 1 + self.genome[7]

        self.strategy = 2*self.genome[8] + self.genome[9]

        self.pos = np.random.randint(0, 7, size=2)

        board.place(self)

    def eat(self, food, board):
        self.stamina += 2
        board.remove(food.pos)

    def mate(self, other, board):
        new_creature =  Creature(board, crossover(self, other))


    def feel(self, board):
        neighbors = board.neigbors(self.pos)
