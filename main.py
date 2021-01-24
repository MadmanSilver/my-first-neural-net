from perset import PerSet
from random import uniform

filename = "training.txt"
max_words = 0
max_letters = 0

for line in open(filename, "r").read().split('\n'):
    if len(line.split('/')[0].split()) > max_words:
        max_words = len(line.split('/')[0].split())
    for word in line.split('/')[0].split():
        if len(word) > max_letters:
            max_letters = len(word)

set1 = PerSet({l: uniform(0.0, 1.0) for l in "abcdefghijklmnopqrstuvwxyz"}, [[uniform(-4.0, 4.0) for l in range(max_letters)] for w in range(max_words)], [[uniform(-4.0, 4.0) for j in range(3)] for i in range(max_words)])

set1.train(filename)
print(set1.err)