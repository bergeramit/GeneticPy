import random
import string

# target = the word the algorithm searches
# sizeSTR = size of target
sizeSTR = 5
target = "hello"

#the basic gene struct
class ga_struct:
    def __init__(self):
        self.str =""
        for i in xrange(0,sizeSTR):
            a= random.choice(string.ascii_letters).lower()
            self.str = self.str + a
        self.fitness=0

#calculate and update fitness 
def updateFitness(ga_str):
    fitness = 5
    for i in xrange(0,sizeSTR):
        if ga_str[i] == target[i]:
            fitness = fitness-1
    return fitness

def calcFitness(ga_list):
    for ga_st in ga_list:
        ga_st.fitness = updateFitness(ga_st.str)

def compareFit(ga_st):
    return ga_st.fitness

#mutate gene by randomly selecting a place to insert randome letter at 
def mutate(ga_str):
    num = random.randint(0, sizeSTR-1)
    a = random.choice(string.ascii_letters).lower()
    l = list(ga_str.str)
    l[num] = a
    ga_str.str = ''.join(l)

#mate two genes using One Point Crossover
def mate(ga_list):
    for i in range(20,len(ga_list)):
        num = random.randint(0, sizeSTR-1)
        gene1 = random.randint(0, len(ga_list)-1)
        gene2 = random.randint(0, len(ga_list)-1)
        l = list(ga_list[i].str)
        for j in range(0,num):
           l[j] = ga_list[gene1].str[j]
        for j in range(num,sizeSTR):
           l[j] = ga_list[gene2].str[j]
        ga_list[i].str = ''.join(l)
        if random.randint(0, sizeSTR-1) == 2:
            mutate(ga_list[i])

#main area TODO: add def main():
ga_list = []
for i in range(1,2000):
    a = ga_struct()
    ga_list.append(a)

for iter in range(1,200):
    calcFitness(ga_list)
    ga_list.sort(key=compareFit,reverse=False)
    print('Best',iter,': ',ga_list[0].str," with fitness: ",ga_list[0].fitness)
    if ga_list[0].fitness == 0:
        break
    mate(ga_list)




