# Eric Kalosa-Kenyon
# Dec 18, 2016
#       This script simulates evolution of biological creatures. It wants to be
#       a full fledged package simulating interactions between artificial and
#       naturally observed organisms, their environments, and economic
#       pressures (like consumption, shipping, anthropogenic climate change).
#       Could be used to show potential ramifications of different energy,
#       consumption, etc. policies.
#       Could be used to generate different stories of life on earth under
#       different geoclimactic conditions.
#       Originally just for seeing how plants will rediversify as extinction
#       events pass, useful for looking at economy as an evolutionary force
#       acting on climate and agricultural genetics and crop productivity.
#
#       Currently, functionality includes:
#       1. simulate_pop()
#           Finds Hardy-Weinberg equilibrium with a genetic algorithm
# Sources:
#   http://cooplab.github.io/popgen-notes/#the-coalescent-and-patterns-of-neutral-diversity


import numpy as np

alleles = 5
pop_size = 10
generations = 200
ploidy = 2

## Make initial population for propagation
# uniform prior over alleles
init_pop = np.random.choice(
        alleles,
        pop_size * ploidy,
        replace = True,
        p = np.repeat(1.0/alleles, alleles)
    ).reshape([pop_size, ploidy])
# init_pop[0] is an individual with numeric categorical alleles
whole_pop = np.empty([generations, pop_size, ploidy])
whole_pop[0] = init_pop

### TODO
## Mate individuals and produce offspring
## Apply fitness function
# Allow for multiple generation life spans, fitness based probabilistic life
#   spans
# Allow for variable population size dependent on climate state
#   (e.g. true polynomial range over x domain proportional to sustainable
#   population size - if the range gets too small, world e.g. gets too hot and
#   nothing survives)
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
# Allow for input from better climate models, crop models, economic models.
