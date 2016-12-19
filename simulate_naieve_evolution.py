# Eric Kalosa-Kenyon
# Dec 18, 2016
#
#   This script simulates evolution of diploid biological creatures with
#   categorical alleles, one allele per chromosome, and uniform fitness across
#   genotypes. There is no environment. Mutation is 
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
mutation_rate = 0.08 # alleles per individual per generation, see mutate()

## Create fitness rule - in this case each organism is equally fit
def fitness(population):
    result = np.empty(len(population), dtype=np.dtype(float))
    i = 0
    for organism in population:
        fit = 1 # Each allele confers equal fitness regardless of environment
        result[i] = fit
        i = i + 1
    return result

## Create a mating scheme
def mutate(organism, rate):
    # apply mutation to organim uniformly at random across all chromosomes,
    # coppies, and alleles.
    # number of mutations in an organism is Poisson distributed
    # assumes each locus can choose from the same alleles
    num_mutations = np.random.poisson(rate*organism.size)
    if num_mutations > organism.size: num_mutations = organism.size

    # with replacement:
    for _ in range(num_mutations):
        mutation_indices = tuple([np.random.choice(k) for k in organism.shape])
        new_allele = np.random.choice(alleles)
        organism[mutation_indices] = new_allele
    return organism

def mate_organisms(par1, par2):
    assert par1.shape == par2.shape # parents have same number of chromosomes,
                                    # copy numbers, and alleles on a copy
    offspring = np.empty(par1.shape, dtype=np.dtype(str))
    i, k = 0, 0
    for i in range(par1.shape[0]): # for each chromosome
        for k in range(par1.shape[2]): # for each allele
            # extract variants of the k'th allele on the i'th chromosome
            par1_variants = par1[i, :, k]
            par2_variants = par2[i, :, k]
            # select one variant from par1 and one from par2 for the offspring
            offspring[i, :, k] = np.array([
                    np.random.choice(par1_variants, 1)[0],
                    np.random.choice(par2_variants, 1)[0]
                ])
    return offspring

def mate_population(par_pop):
    # offspring produced as crosses of organisms with frequency proportional to
    # their fitness

    par_fit = fitness(par_pop)
    par_fit_prob = par_fit / par_fit.sum()
    new_pop = np.empty(par_pop.shape, dtype=np.dtype(str))

    # make pop_size new babies
    for i in range(pop_size):
        # note that there is no crossover between copies of chromosomes
        parent_1, parent_2 = par_pop[
                    np.random.choice(
                        a = range(len(par_pop)),
                        size = 2,
                        replace = False,
                        p = par_fit_prob
                    )
                ]
        new_pop[i] = mutate(
                organism = mate_organisms(parent_1, parent_2),
                rate = mutation_rate
            )

    return new_pop

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
        dtype = np.dtype(str)
    )
whole_pop[0] = init_pop
# whole_pop[generation][organism][chromosome][copy][allele]

## Simulate evolution
for i in range(1, generations):
    parent_pop = whole_pop[i-1]
    new_generation = mate_population(parent_pop)
    whole_pop[i] = new_generation

## Visualize
pdb.set_trace()
# Refactor everything into utilities to clean for readability.
