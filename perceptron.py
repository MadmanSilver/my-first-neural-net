from random import uniform

class Perceptron:
    """ Basic outline of a perceptron. Mostly for convenience. """
    
    def __init__(self, weights, activation):
        """ Initialises everything to a default value. These values are not meant to be final. """
        self.weights = weights.copy()
        self.activation = activation
        self.output = 0.0

    def activate(self, input):
        """ Calls the activation function with appropriate arguments. Basically shorthand. """
        self.output = self.activation(input, self.weights)