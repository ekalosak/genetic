# Eric Kalosa-Kenyon
# Dec 18, 2016

def make_poly(deg, coefLow, coefHigh):
    #   Makes a random polynomial represented by a list of floats.
    # deg :: Int
    # coefLow :: Float
    # coefHigh :: Float
    # return :: (Float a) => [a | coefLow < a < coefHigh]
    #   where len(return) == deg
    return [coefLow + random.random() * (coefHigh - coefLow)
        for _ in range(deg)]

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

def fitness(p, tp, x_range = [-10,10], n_samp=200):
    # Apply OLS fitness to polynomial organisms p and tp
    #   p :: [Float]
    #   tp :: [Float]
    x_sampled = np.linspace(*x_range, n_samp)
    organism_fitness = sum(np.square(
            np.subtract(
                np.polyval(p, x_sampled),
                truePolEval
            )))
