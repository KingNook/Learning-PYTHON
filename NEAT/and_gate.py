## Teaching the net an 'AND' gate
## Truth Table-
# +---+---+-----+ 
# | A | B | OUT | 
# +---+---+-----+ 
# | 0 | 0 |  0  |
# | 0 | 1 |  0  |
# | 1 | 0 |  0  |
# | 1 | 1 |  1  |
# +---+---+-----+
#
## The (original) Network
# A (0)
#     \
#     (0) OUT 
#     /
# B (0)

import neat


and_inputs = [(0.0, 0.0), (0.0, 0.1), (1.0, 0.0), (1.0, 1.0)]
and_outputs = [   (0.0,),     (0.0,),     (0.0,),     (1.0,)]

# Inputs genomes (+ config) and sets the 'fitness' atrribute of each to its fitness (genome.fitness)
def eval_genomes(genomes, config):
    for genome_id, genome in genomes:
        genome.fitness = 4.0
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        for xi, xo in zip(and_inputs, and_outputs):
            output = net.activate(xi)
            genome.fitness -= (output[0] - xo[0]) ** 2

