from neuralnetwork import NeuralNetwork
from matrix import Matrix

inputs = [1, 0]
targets = [1, 0]

nn = NeuralNetwork(2, 2, 1, 0.1)
nn.train(inputs, targets)
