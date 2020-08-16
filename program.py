from neuralnetwork import NeuralNetwork
from matrix import Matrix

input = [1, 0]

nn = NeuralNetwork(2, 2, 1)
result = nn.feedforward(input)
print(result)
