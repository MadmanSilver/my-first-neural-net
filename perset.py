from perceptron import Perceptron
from random import uniform
import activations

class PerSet:
    """ A neural net state used for easy comparisons. """

    def __init__(self, alpha, lps_v, wps_v):
        """ Creates a perceptron set with given values. """
        self.alpha_values = alpha.copy()

        # Creates first layer of perceptrons
        self.lps = []
        for i in range(len(lps_v)):
            self.lps.append(Perceptron(lps_v[i], activations.ltow))

        self.lps_values = [l.copy() for l in lps_v]

        # Creates second layer of perceptrons
        self.wps = []
        for i in range(len(wps_v)):
            self.wps.append(Perceptron(wps_v[i], activations.wtoc))

        self.wps_values = wps_v.copy()

    def process(self, input):
        """ Processes an input through the nuernet. """
        input = input.lower().split()

        # Activates first layer of perceptrons
        for i in range(len(input)):
            self.lps[i].activate([self.alpha_values[l] for l in input[i]])

        # Activates second layer of perceptrons
        for i in range(len(self.wps)):
            wpin = [self.lps[i].output] # Adds current word
            if i != 0:
                wpin.append(self.lps[i - 1].output) # Adds previous word
            if i != len(self.lps) - 1:
                wpin.append(self.lps[i + 1].output) # Adds next word
            self.wps[i].activate(wpin)

        return [self.wps[i].output for i in range(len(input))]

    def train(self, file):
        """ Loads training dataset from a file and calculates average error. """
        file = open(file, "r").read().split('\n')

        self.err = 0
        for line in file:
            input = line.split('/')[0]
            vals = line.split('/')[1].split()

            out = self.process(input)

            diff = 0
            for i in range(len(vals)):
                diff += abs(float(vals[i]) - out[i])
            self.err += diff / len(vals)

        self.err = self.err / len(file)
