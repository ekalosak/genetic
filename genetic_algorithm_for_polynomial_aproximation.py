## Author: Eric Kalosa-Kenyon
## Date: Dec 08, 2016
## python3 using Anaconda from Continuum
##
##      This script uses a genetic algorithm to find a polynomial of best fit
## given that the degree of the polynomial is already known. To be explicit,
## we're not looking for the polynomial closest to the true one over all the
## real numbers, but the polynomial closest to the true one over a prespecified
## range. This restriction is purely for mathematical simplicity.
##      In essence, a genetic algorithm takes a population of N possible
## solutions (organisms, in the biological metaphor) and selects the best K of
## them (the organisms fit enough to mate). These K best organisms mate to
## produce offspring that are crosses of their parents.
##      Because we're looking at the fit of polynomials, we'll use the sum of
## squares fitness function for no particular reason other than it is canonical
## and has a few desirable properties.
##      The genome for each organism in this class of objects is the ordered set
## of coefficients. Crossing for a new generation is a result of random mating
## across the K best organisms with no crossover and Laplacian mutation of
## the coefficients.
##      Note that this basic example misses any crossover because each organism
## is monpoloid (has one chromosome). Selection is also "dumb". Further note
## that the stopping condition is based on number of generations, not a degree
## of convergence - this is for computational convenience.
##      Some interesting further problems in this area are:
##      -1. Fast prime number calculation
##      0. Brachristochrone
##  (http://www.obitko.com/tutorials/genetic-algorithms/encoding.php)
##      1. Knapsack problem (encode list as binary Include or Don't Include)
##      2. Traveling salesman problem (encode ordered list of cities)
##      3. Train a neural network (note that backpropagation may be more effic.)
##      4. Generic LISP expressions
## Packages that do this better:
##      https://github.com/DEAP/notebooks/blob/master/SIGEvolution.ipynb
## There are also, like, a jillion ways this could be made more efficient.

### Import required packages
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_pdf import PdfPages
import random
import pdb
from numpy import matlib
import numpy as np

### Lemmas (a.k.a. helper functions)
def make_poly(deg, coefLow, coefHigh):
    #   Makes a random polynomial represented by a list of floats.
    # deg :: Int
    # coefLow :: Float
    # coefHigh :: Float
    # return :: (Float a) => [a | coefLow < a < coefHigh]
    #   where len(return) == deg
    return [coefLow + random.random() * (coefHigh - coefLow)
        for _ in range(deg)]

# Turns out np.polyval does this! And probaby way more efficiently - win!
# def eval_poly(pol, x):
#     #   Evaluates polynomial at x (for single dimension input). Assumes the
#     # polynomial includes an intercept term.
#     # pol :: [Float]
#     # x :: Num
#     # return :: Num
#     deg = len(pol)
#     r = 0
#     for d in range(deg):
#         r = r + (pol[d] * (x**d))
#     return r

def mate(p, q, cross = 0.6):
    # Performs genetic algorithm mating on two polynomials
    #   Favors p's chromosome if cross is large, agostic iff cross == 0.5
    # p, q :: (len q == len p) => [Float]
    # cross :: (0 < cross < 1) => Float
    assert len(p) == len(q)
    assert (0 < cross) & (cross < 1)
    babysChromosomes = np.array(matlib.rand(len(p)) < cross)
    babysChromosomes = np.ndarray.flatten(babysChromosomes)
    assert babysChromosomes.dtype == 'bool'
    baby = np.zeros(len(p))
    baby[babysChromosomes] = p[babysChromosomes]
    baby[np.invert(babysChromosomes)] = q[np.invert(babysChromosomes)]
    return baby

def mutate(p, rate = 0.3):
    # apply gaussian mutations to chromosome at rate
    mp = [
            p[i] if random.random() > rate
            else p[i] + np.random.randn()
            for i in range(len(p))
        ]
    return(mp)

### Configure script and setup truth
deg = 5
nSamp = 200 # number of equally spaced collocation points for testing each
            # proposed polynomial
popSize = 100 # start each generation with a population of this size
selectSize = 20 # only the e.g. 20 best polynomials get to mate
# numNew = 3 # number of brand new organisms to introduce in each generation
assert popSize % selectSize == 0 # each selected org has equal num children
generations = 20 # do the evolutionary algorithm for 10 generations
polCoefRange = [-5, 5]  # in e.g. A + Bx + Cx^2, the {A,B,C} must each be
                        # between the lower and upper bounds herein specified.
polDomain = [-10, 10] # evaluate the fitness over x sampled from this range
xSamp = np.linspace(*polDomain, nSamp)
truePol = make_poly(deg, *polCoefRange)
print("true polynomial of degree {} initialized as {}".format(deg, truePol))

### Initalize population of polynomials
initPop = [] # :: List of Lists of Floats in polCoefRange
initPop = [make_poly(deg, *polCoefRange) for _ in range(popSize)]
print("initial population initialized with {} individual organisms".format(
            popSize))

### Simulate fitness-based selection and random mating
population = initPop
truePolEval = np.polyval(truePol, xSamp)
bestFit = []
bestOrg = []
for g in range(generations):

    # calculate fitness of each organism (i.e. sum of square error)
    fitness = [sum(np.square(
        np.subtract(
            np.polyval(organism, xSamp),
            truePolEval
        ))) for organism in population]

    # select the breeding stock
    fitArr = np.array(fitness)
    sortOrdering = fitArr.argsort() # sort by fitness
    sortPop = np.array(population)[sortOrdering]
    sortFit = fitArr[sortOrdering]
    assert sortFit[0] <= sortFit[1]
    print("most fit organism this generation at {}".format(sortFit[0]))
    # argsort does highest on end of list, we want lowest sum sq error
    bestKOrgs = sortPop[0:selectSize]
    assert len(bestKOrgs) == selectSize
    bestFit = bestFit + [sortFit[0]]
    bestOrg = bestOrg + [sortPop[0]]

    # mate
    population = []
    for b in bestKOrgs:
        # could weight this mating according to fitness... too lazy rn
        ms = bestKOrgs[
                np.random.choice(
                    range(len(bestKOrgs)),
                    popSize/selectSize
                )
            ]
        kids = [mate(b, m) for m in ms]
        population = population + kids
    population = [mutate(p) for p in population]
    assert len(population) == len(initPop)

best = bestOrg[-1]
print("aprox solution after {} generations is {}".format(
    generations, best))
print("truth is {}".format(truePol))

### Plot diagnostics
pp = PdfPages('polynomial_aprox_genetic.pdf')

# plot truth v best
fig = plt.figure()
plt.subplot(211)
plt.plot(xSamp, np.polyval(truePol, xSamp))
plt.suptitle("True polynomial")
plt.title(np.array(truePol))
plt.subplot(212)
plt.plot(xSamp, np.polyval(best, xSamp))
plt.suptitle("Best genetic aproximation")
plt.title(best)
pp.savefig()
plt.close()

# plot fitness as generations progress
fig = plt.figure()
plt.plot(range(generations), np.log(bestFit))
plt.title("Log(fitness) over generations")
pp.savefig()
plt.close()

# TODO the following
# # plot best of each generation as a 3d surface
# fig = plt.figure()
# ax = fig.gca(projection='3d')
# XX, YY = np.meshgrid(range(generations), xSamp)
# ZZ = 'foo' # CONTINUE HERE TODO
# sur = ax.plot_surface(XX, YY, ZZ, linewidth=1, antialiased=True)
# pp.savefig()
# plt.close()

pp.close()
