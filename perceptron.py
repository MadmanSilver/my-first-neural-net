from random import uniform

class Perceptron:
    """ Basic outline of a perceptron. Mostly for convenience. """
    
    def __init__(self, inNum, activation):
        """ Initialises everything to a default value. These values are not meant to be final. """
        self.inputs = [0.0] * inNum
        self.weights = [uniform(-4.0, 4.0) for i in range(inNum)]
        self.activation = activation
        self.output = 0.0

    def activate(self):
        """ Calls the activation function with appropriate arguments. Basically shorthand. """
        self.output = self.activation(self.inputs, self.weights)