# https://towardsdatascience.com/evolution-of-a-salesman-a-complete-genetic-algorithm-tutorial-for-python-6fe5d2b3ca35

# 遗传算法解TSP问题
# 创建一个city class ，并计算距离
'''

Gene: a city (represented as (x, y) coordinates)
Individual (chromosome): a single route satisfying the conditions above
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
import  random


def geneticAlgorithm(population, popSize, eliteSize, mutationRate, generation):
    # Create the initial population[a collection of possible routes]
    pop = initialPopulation()      # many possible routes
    sortedPop = rankFitness(pop)   # rank the routes
    # roulette select the mating pool





# 2. Determine fitness  use the inverse of the lenth of the route as the fitness
# maxmize the fitness
# rank the fitness of the population
def rankFitness(population):
    fit = [0]*len(population)
    for i in range(len(population)):
        fit[i]= fitness(population[i])
    rankfit =  sorted(population,key=fitness, reverse=True)
    return rankfit


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


# create the initial population, popSize of possible routes
def initialPopulation(popSize,cityList):
    population = []

    for i in range (popSize):
        population.append(createRoute(cityList))

    return population



#create one possible route
def createRoute(cityList):
    route = random.sample(cityList, len(cityList))  # choose len(citylist) of element from cityList and return
    return  route

# roulette input the population, calculate the fitness of every route，
# then use the random pick to return a route

# too many for cycle
def rouletteSelect(population):
    selectResults=[]
    fitall = 0
    fit = [0] * len(population)
    fitrate = [0] * len(population)
    for i in range(len(population)):
        fit[i] = fitness(population[i])
    fitall = sum(fit)
    for i in range(len(population)):
        for j in range(i+1):
            sum[i] +=fit[j]
        fitrate[i] = sum[i]/fitall

    for i in range(20):
        pick = random.random()
        for i in range (len(population)):
            if(fitrate[i]<pick<fitrate[i+1]):
                selectResults.append(population[i])
    return selectResults   # return 20 parents


def crossOver():

def mutation():


class City:
    def __init__(self, x, y):
        self.x = x
        self.y =y

    def distance(self, city):
        xDis = abs(self.x - city.x)
        yDis = abs(self.y - city.y)
        distance = np.sqrt((xDis ** 2) + (yDis ** 2))
        return distance

    def __repr__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"



if __name__ == '__main__':
    cityList =[]
    for i in range(5):
        cityList.append(City(x=int(random.random() * 200), y=int(random.random() * 200)))
    population = initialPopulation(4, cityList)
    ra = rankFitness(population)

    print(ra)

