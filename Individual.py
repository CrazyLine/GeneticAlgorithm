import random

class Individual:
    def updateFitness(self):
        #TODO implement fitness function
        sumfitness = 0
        for i in range(len(self.map.states)):
            for j in range(len(self.map.borders)):
                if self.map.borders[j].index1 == i:
                    if self.statescolor[i] != self.statescolor[self.map.borders[j].index2]:
                        sumfitness += 1
        self.fitness = sumfitness

    def __init__(self,map):
        self.map=map
        self.fitness=0
        self.color=[0,1,2,3]
        self.statescolor=[]
        for i in range(len(map.states)):
            r=random.randint(0,3)
            self.statescolor.append(self.color[r])
        #TODO implement random generation of an individual
        self.updateFitness()

    def reproduce(self,x, y):
        child1 = Individual(x.map)
        # TODO reproduce child from individuals x and y
        r = random.uniform(0,len(x.statescolor))
        for i in range(len(x.statescolor)):
            if i < r:
                child1.statescolor[i]=x.statescolor[i]
            else:
                child1.statescolor[i]=y.statescolor[i]
        child1.updateFitness()
        child2 = Individual(x.map)
        for i in range(len(x.statescolor)):
            if i > r:
                child2.statescolor[i]=x.statescolor[i]
            else:
                child2.statescolor[i]=y.statescolor[i]
        child2.updateFitness()
        if child1.fitness>child2.fitness:
            return child1
        else:
            return child2

    def mutate(self):
        # TODO implement random mutation of the individual
        r = random.randint(0,len(self.statescolor)-1)
        c = random.randint(0,3)
        self.statescolor[r] = c
        self.updateFitness()

    def isGoal(self):
        print("fitness: " , self.fitness , " goalfitness: " , len(self.map.borders))
        return self.fitness == len(self.map.borders)

    def print(self):
        print("fitness: " , self.fitness)
        for i in range(len(self.statescolor)):
            print(self.map.states[i] , ": " , self.statescolor[i])
        print("0, 1, 2, and 3 represent 4 colors respectively.")