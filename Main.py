import random

from Border import Border
from Individual import Individual
from Map import Map
from Population import Population
import networkx as nx
import matplotlib.pyplot as plt

def initMap(map):
    # map.states.append("North Carolina")
    # map.states.append("South Carolina")
    # map.states.append("Virginia")
    # map.states.append("Tennessee")
    # map.states.append("Kentucky")
    # map.states.append("West Virginia")
    # map.states.append("Georgia")
    # map.states.append("Alabama")
    # map.states.append("Mississippi")
    # map.states.append("Florida")
    #
    # map.borders.append(Border(0, 1))
    # map.borders.append(Border(0, 2))
    # map.borders.append(Border(0, 3))
    # map.borders.append(Border(0, 6))
    # map.borders.append(Border(1, 6))
    # map.borders.append(Border(2, 3))
    # map.borders.append(Border(2, 4))
    # map.borders.append(Border(2, 5))
    # map.borders.append(Border(3, 4))
    # map.borders.append(Border(3, 6))
    # map.borders.append(Border(3, 7))
    # map.borders.append(Border(3, 8))
    # map.borders.append(Border(4, 5))
    # map.borders.append(Border(6, 7))
    # map.borders.append(Border(6, 9))
    # map.borders.append(Border(7, 8))
    # map.borders.append(Border(7, 9))
    ##################################################51 states#########################################
    map.states.append("AK")  # 0
    map.borders.append(Border(0, 1))
    map.states.append("WA")  # 1
    map.borders.append(Border(1, 2))
    map.borders.append(Border(1, 3))
    map.states.append("ID")  # 2
    map.borders.append(Border(2, 4))
    map.borders.append(Border(2, 5))
    map.borders.append(Border(2, 6))
    map.borders.append(Border(2, 7))
    map.borders.append(Border(2, 3))
    map.states.append("OR")  # 3
    map.borders.append(Border(3, 7))
    map.borders.append(Border(3, 8))
    map.states.append("MT")  # 4
    map.borders.append(Border(4, 9))
    map.borders.append(Border(4, 10))
    map.borders.append(Border(4, 5))
    map.states.append("WY")  # 5
    map.borders.append(Border(5, 10))
    map.borders.append(Border(5, 11))
    map.borders.append(Border(5, 12))
    map.borders.append(Border(5, 6))
    map.states.append("UT")  # 6
    map.borders.append(Border(6, 12))
    map.borders.append(Border(6, 13))
    map.borders.append(Border(6, 14))
    map.borders.append(Border(6, 7))
    map.states.append("NV")  # 7
    map.borders.append(Border(7, 14))
    map.borders.append(Border(7, 8))
    map.states.append("CA")  # 8
    map.borders.append(Border(8, 14))
    map.borders.append(Border(8, 15))
    map.states.append("ND")  # 9
    map.borders.append(Border(9, 16))
    map.borders.append(Border(9, 10))
    map.states.append("SD")  # 10
    map.borders.append(Border(10, 16))
    map.borders.append(Border(10, 17))
    map.borders.append(Border(10, 11))
    map.states.append("NE")  # 11
    map.borders.append(Border(11, 17))
    map.borders.append(Border(11, 19))
    map.borders.append(Border(11, 18))
    map.borders.append(Border(11, 12))
    map.states.append("CO")  # 12
    map.borders.append(Border(12, 19))
    map.borders.append(Border(12, 20))
    map.borders.append(Border(12, 13))
    map.borders.append(Border(12, 14))
    map.states.append("NM")  # 13
    map.borders.append(Border(13, 20))
    map.borders.append(Border(13, 21))
    map.borders.append(Border(13, 14))
    map.states.append("AZ")  # 14

    map.states.append("HI")  # 15

    map.states.append("MN")  # 16
    map.borders.append(Border(16, 22))
    map.borders.append(Border(16, 17))
    map.states.append("IA")  # 17
    map.borders.append(Border(17, 22))
    map.borders.append(Border(17, 23))
    map.borders.append(Border(17, 18))
    map.states.append("MO")  # 18
    map.borders.append(Border(18, 23))
    map.borders.append(Border(18, 24))
    map.borders.append(Border(18, 25))
    map.borders.append(Border(18, 20))
    map.borders.append(Border(18, 19))
    map.states.append("KS")  # 19
    map.borders.append(Border(19, 20))
    map.states.append("OK")  # 20
    map.borders.append(Border(20, 26))
    map.borders.append(Border(20, 21))
    map.states.append("TX")  # 21
    map.borders.append(Border(21, 26))
    map.borders.append(Border(21, 27))
    map.states.append("WI")  # 22
    map.borders.append(Border(22, 28))
    map.borders.append(Border(22, 23))
    map.states.append("IL")  # 23
    map.borders.append(Border(23, 29))
    map.borders.append(Border(23, 24))
    map.states.append("KY")  # 24
    map.borders.append(Border(24, 30))
    map.borders.append(Border(24, 31))
    map.borders.append(Border(24, 32))
    map.borders.append(Border(24, 25))
    map.borders.append(Border(24, 29))
    map.states.append("TN")  # 25
    map.borders.append(Border(25, 32))
    map.borders.append(Border(25, 33))
    map.borders.append(Border(25, 33))
    map.borders.append(Border(25, 34))
    map.borders.append(Border(25, 35))
    map.borders.append(Border(25, 36))
    map.borders.append(Border(25, 26))
    map.states.append("AR")  # 26
    map.borders.append(Border(26, 36))
    map.borders.append(Border(26, 27))
    map.states.append("LA")  # 27
    map.borders.append(Border(27, 36))
    map.states.append("MI")  # 28
    map.borders.append(Border(28, 30))
    map.borders.append(Border(28, 29))
    map.states.append("IN")  # 29
    map.borders.append(Border(29, 30))
    map.states.append("OH")  # 30
    map.borders.append(Border(30, 37))
    map.borders.append(Border(30, 31))
    map.states.append("WV")  # 31
    map.borders.append(Border(31, 37))
    map.borders.append(Border(31, 38))
    map.borders.append(Border(31, 32))
    map.states.append("VA")  # 32
    map.borders.append(Border(32, 38))
    map.borders.append(Border(32, 39))
    map.borders.append(Border(32, 33))
    map.states.append("NC")  # 33
    map.borders.append(Border(33, 40))
    map.borders.append(Border(33, 34))
    map.states.append("GA")  # 34
    map.borders.append(Border(34, 40))
    map.borders.append(Border(34, 41))
    map.borders.append(Border(34, 35))
    map.states.append("AL")  # 35
    map.borders.append(Border(35, 41))
    map.borders.append(Border(35, 36))
    map.states.append("MS")  # 36

    map.states.append("PA")  # 37
    map.borders.append(Border(37, 42))
    map.borders.append(Border(37, 44))
    map.borders.append(Border(37, 43))
    map.borders.append(Border(37, 38))
    map.states.append("MD")  # 38
    map.borders.append(Border(38, 44))
    map.borders.append(Border(38, 39))
    map.states.append("DC")  # 39

    map.states.append("SC")  # 40

    map.states.append("FL")  # 41

    map.states.append("NY")  # 42
    map.borders.append(Border(42, 45))
    map.borders.append(Border(42, 46))
    map.borders.append(Border(42, 47))
    map.borders.append(Border(42, 43))
    map.states.append("NJ")  # 43
    map.borders.append(Border(43, 47))
    map.borders.append(Border(43, 44))
    map.states.append("DE")  # 44

    map.states.append("VT")  # 45
    map.borders.append(Border(45, 48))
    map.borders.append(Border(45, 46))
    map.states.append("MA")  # 46
    map.borders.append(Border(46, 48))
    map.borders.append(Border(46, 47))
    map.borders.append(Border(46, 49))
    map.states.append("CT")  # 47
    map.borders.append(Border(47, 49))
    map.states.append("NH")  # 48
    map.borders.append(Border(48, 50))
    map.states.append("RI")  # 49
    map.states.append("ME")  # 50 

if __name__ == '__main__':
    map = Map()
    initMap(map)
    populationSize = 100 # TODO find reasonable value
    population = Population(map, populationSize)

    maxIterations = 500 # TODO find reasonable value
    currentIteration = 0
    goalFound = False
    bestIndividual = Individual(map) # to hold the individual representing the goal, if any
    mark = 0
    while currentIteration < maxIterations and goalFound==False:
        newPopulation = Population(map,0)
        bestparent=Individual(map)
        worstchild=Individual(map)
        for i in range(populationSize):
            x,y= population.randomSelection()
            if x.fitness>y.fitness :
                if bestparent.fitness<x.fitness:
                    bestparent=x
            else:
                if bestparent.fitness < y.fitness:
                    bestparent = y
            child = Individual.reproduce(x, x, y)
            pmutate=random.random()
            if pmutate < 0.3 :# TODO use small probability instead
                child.mutate()
            if child.isGoal():
                goalFound = True
                bestIndividual = child
                mark=1
                break
            newPopulation.vector.append(child)
        currentIteration += 1
        if mark == 1:
            break

        worstmark=0
        for i in range(len(newPopulation.vector)):
            if newPopulation.vector[i].fitness<worstchild.fitness:
                worstchild=newPopulation.vector[i]
                worstmark=i
        newPopulation.vector[worstmark]=bestparent
        population = newPopulation


    if goalFound :
        print("Found a solution after ",currentIteration," iterations" )
        bestIndividual.print()
        G = nx.Graph()
        labels={}
        for i in range(len(map.states)):
            G.add_node(i)
            labels[i]=map.states[i]
        for i in range(len(map.borders)):
            G.add_edge(map.borders[i].index1,map.borders[i].index2)
        pos = nx.spring_layout(G)
        colors = bestIndividual.statescolor
        nx.draw_networkx_nodes(G, pos, node_color=colors)
        nx.draw_networkx_labels(G,pos,labels)
        nx.draw_networkx_edges(G, pos)
        plt.axis('off')
        plt.show()
    else:
        print("Did not find a solution after ",currentIteration," iterations")
        print("Please run it again...")