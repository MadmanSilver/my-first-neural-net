import numpy as np

def sig(x):
    """ Shorthand function for sigmoid math. """
    return 1 / (1 + np.exp(-x))

def ltow(inputs, weights):
    """ Averages letter values to create a word value. """
    total = 0.0
    for i in range(len(inputs)):
        total += inputs[i] * weights[i]
    return sig(total)

def wtoc(inputs, weights):
    """ Applies the previous word and the next word as a weight to the value. """
    value = inputs[0] * weights[0]
    biases = [inputs[i] * weights[i] for i in range(1, len(inputs))]
    bias = 0.0

    for i in range(len(biases)):
        bias += biases[i]

    bias = bias / float(len(biases))

    return sig(sig(value) * bias)