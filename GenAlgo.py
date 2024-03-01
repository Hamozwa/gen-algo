#GenAlgo
#Uses genetic algorithm to find values of x y and z that set an expression equal to zero

from numpy import random

def expression(x,y,z):
    exp = 8*x**2 + 3*y**3 - 4*z - 16 #Any expression works
    return exp

def fitness(x,y,z):
    res = expression(x,y,z)
    fit = 1/(abs(res)) #the closer to zero, the higher the fitness
    return fit

nextgen = random.normal(size = (1000,3)) #create random initial generation

for gen in range(10000):
    currentgen = []
    
    #calculate fitness of each specimen
    for specimen in nextgen:
        currentfit = fitness(specimen[0],specimen[1],specimen[2])
        currentgen.append([currentfit,specimen[0],specimen[1],specimen[2]])

    #Find 100 best specimens in generation to act as parents              
    currentgen.sort()
    print("Generation "+str(gen)+" fittest specimen: "+str(currentgen[-1:]))                     
    mostfit = currentgen[-100:]

    nextgen = []
    for i in range(1000):
        newborn = []
        randparent = random.randint(0,100)
        #This next line is key - mutates child of parent less the more fit the parent - arbitrary expression used to this end
        currentscale = 2.72**(-0.01*mostfit[randparent][0])
        randmutator = random.normal(loc = 1, scale = currentscale)
        #miracle of childbirth
        newborn = [mostfit[randparent][1]*randmutator,mostfit[randparent][2]*randmutator,mostfit[randparent][3]*randmutator]
        nextgen.append(newborn)
    
    

