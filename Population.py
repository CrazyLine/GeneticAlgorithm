#Class representing a population of individuals
import random

from Individual import Individual

class Population:
    def __init__(self,map,initialSize):
        self.vector=[]
        for i in range(initialSize):
            self.vector.append(Individual(map))

    def randomSelection(self):
        # TODO implement random selection
        # an individual should be selected with a probability
        # proportional to its fitness
        sumfiness=0
        for i in range(len(self.vector)):
            sumfiness+=self.vector[i].fitness
        fitness_list=[]
        for i in range(len(self.vector)):
            fitness_list.append(float(self.vector[i].fitness)/float(sumfiness))
        r=random.choices(self.vector,weights=fitness_list,k=2)
        while r[0]==r[1] :
            r = random.choices(self.vector, weights=fitness_list, k=2)
        return r[0],r[1]