from neuralnetwork import NeuralNetwork
from matrix import Matrix
from training_data_obj import Training_Data
import os
def clear(): return os.system('cls')


# Init training data, should probably be inside a json file
training_data = []
training_data.append(Training_Data([1, 0], [1]))
training_data.append(Training_Data([0, 1], [1]))
training_data.append(Training_Data([1, 1], [0]))
training_data.append(Training_Data([0, 0], [0]))

nn = NeuralNetwork(2, 2, 1, 0.5)

for i in range(10000):
    # Train without logging, faster
    # nn.train(training_data[0].inputs, training_data[0].targets)
    # nn.train(training_data[1].inputs, training_data[1].targets)
    # nn.train(training_data[2].inputs, training_data[2].targets)
    # nn.train(training_data[3].inputs, training_data[3].targets)

    # Train with loggin, much slower
    clear()
    nn.train(training_data[0].inputs, training_data[0].targets).log()
    nn.train(training_data[1].inputs, training_data[1].targets).log()
    nn.train(training_data[2].inputs, training_data[2].targets).log()
    nn.train(training_data[3].inputs, training_data[3].targets).log()
    print("Iteration: " + str(i))

print(str(nn.feedforward([1, 0])))
print(str(nn.feedforward([0, 1])))
print(str(nn.feedforward([1, 1])))
print(str(nn.feedforward([0, 0])))
