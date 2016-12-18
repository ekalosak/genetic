# Eric Kalosa-Kenyon
# Dec 18, 2016
#
#   This script simulates evolution of biological creatures.
#
# Sources:
#   http://cooplab.github.io/popgen-notes/#the-coalescent-and-patterns-of-neutral-diversity


import numpy as np
import pdb
import utilities as ut

## Configure simulation
generations = 200
pop_size = 10 # K, number of organisms in population
chromosomes = 1 # N, so if e.g. N = 4 then 2N=8
ploidy = 2 # P, ploidy
alleles_per_chromosome = 1
alleles = ['A', 'B', 'C', 'D', 'E']

## Create fitness rule - in this case each organism is equally fit
fitness = lambda org: 1

## Make initial population for propagation
# init_pop is a np.matrix (J*P*N*K)
#   J = pop size by P*N = chromosomes by K = alleles per chromosome
#   init_pop[0] a np.matrix size P*N by K representing a single organism
init_pop = ut.make_init_pop(pop_size=pop_size, chromosomes=chromosomes,
        ploidy=ploidy, alleles_per_chromosome=alleles_per_chromosome,
        alleles=alleles, method='uniform_categorical')

# whole_pop is an np.matrix size G*J*P*N*K
#   G generations, J organisms, ploidy P, P*N chromosomes, K alleles
whole_pop = np.empty(
        [generations, pop_size, chromosomes, ploidy, alleles_per_chromosome],
        dtype = np.float32
    )
pdb.set_trace()
whole_pop[0] = init_pop

### TODO
for i in range(1, generations):
    ## Apply fitness function to current generation
    parent_fitness = fitness(whole_pop[i-1])
    ## Mate individuals proportional to their fitness
    pdb.set_trace()
    ## Assign the most fit offspring to the next part of history
    whole_pop[i] = new_generation

# Refactor everything into utilities to clean for readability.

### IDEAS
# Give each allele or combination morphological meaning
#   e.g. first, just higher number is higher fitness. Trivial but functional.
#       second, LES, drought tollerance, etc. all parameterized
#       ecophysiologically.
#       third, tolerance to pests, diseases, and eaters who all have their own
#       evolutionary path.
#       fourth, maybe find a way to grow new adaptive morphological traits
#       rather than just strategies of movement, reproduction, and potentially
#       social order (fish swim in schools) and trait parameterization.
#
# Allow for input from better climate models, crop models, economic models.
# It wants to be a full fledged package simulating interactions between
# artificial and naturally observed organisms, their environments, and economic
# pressures (like consumption, shipping, anthropogenic climate change). Could be
# used to show potential ramifications of different energy, consumption, etc.
# policies. Could be used to generate different stories of life on earth under
# different geoclimactic conditions. Originally just for seeing how plants will
# rediversify as extinction events pass, useful for looking at economy as an
# evolutionary force acting on climate and agricultural genetics and crop
# productivity.
#
# Allow for multiple generation life spans, fitness based probabilistic life
#   spans
# Allow for variable population size dependent on climate state
#   (e.g. true polynomial range over x domain proportional to sustainable
#   population size - if the range gets too small, world e.g. gets too hot and
#   nothing survives)
