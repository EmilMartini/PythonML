from neuralnetwork import NeuralNetwork
from matrix import Matrix

inputs = [1, 0]
targets = [1, 0]

nn = NeuralNetwork(1, 2, 2, 0.1)
nn.train(inputs, targets)
