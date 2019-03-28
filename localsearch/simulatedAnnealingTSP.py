'''
Use the simulated Annealing Algorithm to solve the TSP problem
http://www.blog.pyoung.net/2013/07/26/visualizing-the-traveling-salesman-problem-using-matplotlib-in-python/
https://github.com/chncyhn/simulated-annealing-tsp

http://codecapsule.com/2010/04/06/simulated-annealing-traveling-salesman/

'''

'''
1,Create the initial list of cities
2,At every iteration, two cities are swapped in the list. The cost value is the distance traveled by the salesman for the whole tour.
3,If the new distance, computed after the change, is shorter than the current distance, it is kept.
4,If the new distance is longer than the current one, it is kept with a certain probability.
5,We update the temperature at every iteration by slowly cooling down.
'''

import numpy as np
import random
import math
import matplotlib.pyplot as plt
import localsearch.visual_tsp as visual

def annealSimulate(cityList):
    Tem = 500
    stopping_tem = 1e-8
    iteration =0
    alpha = 0.995
    progress=[]

    # initial route
    route = createRoute( cityList)
    bestRoute = route
    bestDis = 1/fitness(bestRoute)
    progress.append(bestDis)



    while Tem > stopping_tem and iteration < 10000:
        route = accept(swap(route),route,Tem)

        if(1/fitness(route)< 1/fitness(bestRoute)):
            bestRoute = route
            bestDis = 1/fitness(route)
        Tem = Tem * alpha
        iteration += 1
        progress.append(bestDis)
        # print(route)
    visual.plotTSP(bestRoute, num_iters=1)
    print(bestRoute)
    print('------------------------')
    print(bestDis)

    # plt.plot(progress)
    # plt.ylabel('Distance')
    # plt.xlabel('Generation')
    # plt.show()



# swap
def swap(route):
    a = int(random.random()*len(route))
    route[a:a+2] = reversed(route[a:a+2])

    return route

# Accept with probability 1 if candidate is better than current.
# Accept with probabilty p_accept(..) if candidate is worse.
def accept(newRoute, curRoute, Tem):
    if(fitness(newRoute) > fitness(curRoute)):
        curRoute = newRoute
    else:
        if(random.random()< p_accept(fitness(curRoute), fitness(newRoute), Tem)):
            curRoute = newRoute

    return curRoute


def p_accept(cur_fitness, candidate_fitness, Tem):
    """
    Probability of accepting if the candidate is worse than current.
    Depends on the current temperature and difference between candidate and current.
    """
    return math.exp(-abs(candidate_fitness - cur_fitness) / Tem)


#initial route
def createRoute(cityList):
    route = random.sample(cityList, len(cityList))  # choose len(citylist) of element from cityList and return
    return  route

def rankFitness(population):
    fit = [0]*len(population)
    for i in range(len(population)):
        fit[i]= fitness(population[i])
    rankedPop =  sorted(population,key=fitness, reverse=False)

    return rankedPop


# input route list
def fitness(route):
    pathDistance = 0
    for i in range (len(route)):
        if i+1<len(route):
            pathDistance+=City.distance(route[i], route[i+1])
        else:
            pathDistance+=City.distance(route[i],route[0])

    fiteness = 1/pathDistance

    return fiteness


class City:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def distance(self, city):
        xDis = abs(self.x - city.x)
        yDis = abs(self.y - city.y)
        distance = np.sqrt((xDis ** 2) + (yDis ** 2))
        return distance

    def __repr__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"


if __name__ == '__main__':
    cityList =[]
    for i in range(25):
        cityList.append(City(x=int(random.random() * 200), y=int(random.random() * 200)))
    annealSimulate(cityList)
