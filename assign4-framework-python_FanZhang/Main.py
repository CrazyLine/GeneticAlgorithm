import random

from Border import Border
from Individual import Individual
from Map import Map
from Population import Population

# Author Fan Zhang
def initMap(map):
    map.states.append("North Carolina")
    map.states.append("South Carolina")
    map.states.append("Virginia")
    map.states.append("Tennessee")
    map.states.append("Kentucky")
    map.states.append("West Virginia")
    map.states.append("Georgia")
    map.states.append("Alabama")
    map.states.append("Mississippi")
    map.states.append("Florida")

    map.borders.append(Border(0, 1))
    map.borders.append(Border(0, 2))
    map.borders.append(Border(0, 3))
    map.borders.append(Border(0, 6))
    map.borders.append(Border(1, 6))
    map.borders.append(Border(2, 3))
    map.borders.append(Border(2, 4))
    map.borders.append(Border(2, 5))
    map.borders.append(Border(3, 4))
    map.borders.append(Border(3, 6))
    map.borders.append(Border(3, 7))
    map.borders.append(Border(3, 8))
    map.borders.append(Border(4, 5))
    map.borders.append(Border(6, 7))
    map.borders.append(Border(6, 9))
    map.borders.append(Border(7, 8))
    map.borders.append(Border(7, 9))

if __name__ == '__main__':
    map = Map()
    initMap(map)
    populationSize = 0 # TODO find reasonable value
    population = Population(map, populationSize)

    maxIterations = 0 # TODO find reasonable value
    currentIteration = 0
    goalFound = False
    bestIndividual = Individual(map) # to hold the individual representing the goal, if any
    while currentIteration < maxIterations and goalFound==False:
        newPopulation = Population(map,0)
        for i in range(populationSize):
            x= population.randomSelection()
            y = population.randomSelection()
            child = Individual.reproduce(x, x, y)
            if False :# TODO use small probability instead
                child.mutate()
            if child.isGoal():
                goalFound = True
                bestIndividual = child
            newPopulation.vector.append(child)
        currentIteration += 1
        population = newPopulation


    if goalFound :
        print("Found a solution after ",currentIteration," iterations" )
        bestIndividual.printresult()
    else:
        print("Did not find a solution after ",currentIteration," iterations")