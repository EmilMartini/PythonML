from point import Point
import random

class Perceptron:
    weights = []
    accuracy = 0

    def __init__(self, learnRate):
        self.learningRate = learnRate
        for i in range(2):
            self.weights.append(random.random())


    def Activate(self, n):
        return -1 if n < 0 else 1


    def Guess(self, inputs):
        sum = 0
        for i in range(len(inputs)):
            sum += inputs[i] * self.weights[i]
        
        output = self.Activate(sum)
        return output


    def Train(self, inputs, target):
        guess = self.Guess(inputs)
        error = target - guess

        for i in range(len(self.weights)):
            self.weights[i] += error * inputs[i] * self.learningRate