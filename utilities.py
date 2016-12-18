# Eric Kalosa-Kenyon
# Dec 18, 2016


import numpy as np
import pdb

class evolution:
    # tracks population over time
    def __init__(self):
        raise NotImplemented

class population:
    # tracks population over time
    def __init__(self):
        raise NotImplemented

class organism:
    # organism.num_alleles (> 0) :: Int
    # organism.ploidy (> 0) :: Int
    def __init__(self, num_alleles, ploidy):
        raise NotImplemented

    def __eq__(self, other):
        raise NotImplemented
    def __ne__(self, other):
        raise NotImplemented
    def __str__(self):
        raise NotImplemented

class allele:
    # allele.val :: Int
    # a1 == a2 iff a1.val == a2.val

    def __init__(self, val):
        assert type(val) == type(3)
        self.val = val

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.val == other.val
        return False
    def __ne__(self, other):
        return not self.__eq__(other)
    def __str__(self):
        return str(self.val)

def make_poly(deg, coefLow, coefHigh):
    #   Makes a random polynomial represented by a list of floats.
    # deg :: Int
    # coefLow :: Float
    # coefHigh :: Float
    # return :: (Float a) => [a | coefLow < a < coefHigh]
    #   where len(return) == deg
    return [coefLow + random.random() * (coefHigh - coefLow)
        for _ in range(deg)]

def mate(p, q, cross = 0.6, method='random'):
    # Mates two organisms
    # cross :: (0 < cross < 1) => Float
    # method :: String
    #   'elemwise' -> each allele potentially contributes to offspring
    #   'single' -> offspring is crossover of each copy of an allele
    pdb.set_trace()
    assert len(p) == len(q)
    assert (0 < cross) & (cross < 1)
    assert method in ['elemwise', 'single']
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

def poly_fitness(p, tp, x_range = [-10,10], n_samp=200):
    # Apply OLS fitness to polynomial organisms p and tp
    #   p :: [Float]
    #   tp :: [Float]
    pdb.set_trace()
    x_sampled = np.linspace(*x_range, n_samp)
    organism_fitness = sum(np.square(
            np.subtract(
                np.polyval(p, x_sampled),
                truePolEval
            )))
