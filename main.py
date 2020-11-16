from perceptron import Perceptron
from random import uniform
import activations

while True:
    inputs = str(input()).lower().split() # Takes input from the terminal and splits it into words
    values = {l: uniform(0.0, 1.0) for l in 'abcdefghijklmnopqrstuvwxyz'} # Assign values to letters (will be calculated instead of random in future)

    # Creates and activates first layer of perceptrons
    lps = []
    for i in range(len(inputs)):
        lps.append(Perceptron(len(inputs[i]), activations.ltow))
        lps[i].inputs = [values[j] for j in inputs[i]]
        lps[i].activate()

    # Creates and activates second layer of perceptrons
    wps = []
    for i in range(len(inputs)):
        wpin = [lps[i].output] # Adds current word
        if i != 0:
            wpin.append(lps[i - 1].output) # Adds previous word
        if i != len(lps) - 1:
            wpin.append(lps[i + 1].output) # Adds next word
        wps.append(Perceptron(len(wpin), activations.wtoc))
        wps[i].inputs = wpin
        wps[i].activate()

    # Prints values for testing purposes
    for i in range(len(inputs)):
        print('{}: {:.2f}, {:.2f}'.format(inputs[i], lps[i].output, wps[i].output))