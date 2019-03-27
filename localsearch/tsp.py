# https://towardsdatascience.com/evolution-of-a-salesman-a-complete-genetic-algorithm-tutorial-for-python-6fe5d2b3ca35
# modify to pull
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

首先生成100条线路的池子，
第一次迭代
轮盘赌生成20条线路（可能有重复），
crossover 生成10条孩子
变异其中几条孩子
结束此次迭代
记录距离及线路

进行下一次迭代



'''



import numpy as np
import  random
import matplotlib.pyplot as plt

def geneticAlgorithm(cityList, popSize, eliteSize, mutationRate, generation):
    # Create the initial population[a collection of possible routes]
    progress = []
    pop = initialPopulation(popSize, cityList)      # many possible routes
    routeDistance = 1/fitness(rankFitness(pop)[0])
    bestRoute  = rankFitness(pop)[0]
    progress.append(routeDistance)

    for i in range (generation):
        pop = nextGeneration(pop, eliteSize, mutationRate)
        rankedPop = rankFitness(pop)
        if (1 / fitness(rankedPop[0]) < routeDistance):
            routeDistance = 1 / fitness(rankedPop[0])
            bestRoute= rankedPop[0]
        progress.append(routeDistance)

    print(bestRoute)
    print('------------------------')
    print(routeDistance)

    plt.plot(progress)
    plt.ylabel('Distance')
    plt.xlabel('Generation')
    plt.show()



def nextGeneration(currentGen,eliteSize,  mutationRate):
    # now have a generation, it's a population
    # rouletteSelect
    # corssover
    # mutation
    selectPop = rouletteSelect(currentGen, eliteSize)
    children = offSpring(selectPop)
    mutPop =mutation(children, mutationRate)

    return mutPop

# 2. Determine fitness  use the inverse of the lenth of the route as the fitness
# maxmize the fitness
# rank the fitness of the population
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
def rouletteSelect(population,eliteSize):
    selectResults=[]
    fit = [0] * len(population)
    fitrate = [0] * len(population)
    sumfitrate=[0]* len(population)

    for i in range(len(population)):
        fit[i] = fitness(population[i])
    fitall = sum(fit)

    for i in range(len(population)):
        for j in range(i+1):
            sumfitrate[i] +=fit[j]
        fitrate[i] = sumfitrate[i]/fitall

    for i in range(eliteSize):
        pick = random.random()
        for i in range (len(population)):
            if(fitrate[i]<pick<fitrate[i+1]):
                selectResults.append(population[i])
    return selectResults


# ordered crossover
# choose a subset of parent1,give it to parent2,then the remainder was placed in order
# two parents crossover and have one child
def crossOver(parent1, parent2):
    child =[]
    childP1=[]
    childP2=[]
    childP3=[]
    childP4 = []

    genA = int(random.random()*len(parent1))
    genB = int(random.random() * len(parent1))

    startGen = min(genA, genB)
    endGen = max(genA, genB)

    for i in range(startGen, endGen):
        childP1.append(parent1[i])
    childP2 = [item for item in parent2 if item not in childP1]
    for i in range(startGen):
        childP3.append(childP2[i])
    childP4 = [item for item in childP2 if item not in childP3]

    child = childP3+childP1+childP4

    return  child

# 输入选择出来的population,用crossover

def offSpring(selectResults):
    children = []
    pool = random.sample(selectResults, len(selectResults)) #打乱顺序 个数不变

    for i in range (len(selectResults)):
        child = crossOver(pool[i], pool[len(selectResults)-i-1])
        children.append(child)

    return children



#  mutation operation , swap two cities of a route
def mutation(individual, mutationRate):
    for swapped in range(len(individual)):
        if(random.random()< mutationRate):  # swap
            swapWith = int(random.random()*len(individual))
            city1 = individual[swapped]
            city2= individual[swapWith]


            individual[swapped]= city2
            individual[swapWith]=city1

    return  individual

# mutation for the population, 对一整个population都实施这个操作，不一定所有route都会变异
def mutPop(population, mutationRate):
    mutPop=[]

    for ind in range(0, len(population)):
        mutated = mutation(population[ind], mutationRate)
        mutPop.append(mutated)

    return mutPop

# 实例化 city（x,y）
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
    for i in range(25):
        cityList.append(City(x=int(random.random() * 200), y=int(random.random() * 200)))
    geneticAlgorithm(cityList, 100, eliteSize =50, mutationRate=0.01, generation=500)


