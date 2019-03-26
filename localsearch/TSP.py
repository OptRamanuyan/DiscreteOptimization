# https://towardsdatascience.com/evolution-of-a-salesman-a-complete-genetic-algorithm-tutorial-for-python-6fe5d2b3ca35

# 遗传算法解TSP问题
# 创建一个city class ，并计算距离
'''

Gene: a city (represented as (x, y) coordinates)
Individual (aka “chromosome”): a single route satisfying the conditions above
Population: a collection of possible routes (i.e., collection of individuals)
Parents: two routes that are combined to create a new route
Mating pool: a collection of parents that are used to create our next population (thus creating the next generation of routes)
Fitness: a function that tells us how good each route is (in our case, how short the distance is)
Mutation: a way to introduce variation in our population by randomly swapping two cities in a route
Elitism: a way to carry the best individuals into the next generation
'''

'''
1. Create the population

2. Determine fitness

3. Select the mating pool

4. Breed

5. Mutate

6. Repeat
'''


import numpy as np


def geneticAlgorithm(population, popSize, eliteSize, mutationRate, generation):

    pop = initialPopulation()


# create the initial population
def initialPopulation(popSize,cityList):
    population = []

    for i in range (popSize):
        population.append(createRoute(cityList))

    return population


#create route 生成路线
def createRoute(cityList):


class Fitness:
    def













class City:
    def _init_(self, x, y):
        self.x = x
        self.y =y

    def distance(self, city):
        xDis = abs(self.x - city.x)
        yDis = abs(self.y - city.y)
        distance = np.sqrt((xDis ** 2) + (yDis ** 2))
        return distance

    def __repr__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"



