from matrix import Matrix
import math


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


class NeuralNetwork:

    def __init__(self, input_nodes, hidden_nodes, output_nodes):
        self.input_nodes = input_nodes
        self.hidden_nodes = hidden_nodes
        self.output_nodes = output_nodes

        self.weights_ih = Matrix(self.hidden_nodes, self.input_nodes)
        self.weights_ho = Matrix(self.output_nodes, self.hidden_nodes)
        self.weights_ih.randomize()
        self.weights_ho.randomize()

        self.bias_h = Matrix(self.hidden_nodes, 1)
        self.bias_o = Matrix(self.output_nodes, 1)
        self.bias_h.randomize()
        self.bias_o.randomize()

    def feedforward(self, input_array):

        # Generating the hidden outputs
        input = Matrix.FromArray(input_array)
        hidden = Matrix.Multiply(self.weights_ih, input)
        hidden.addElementWise(self.bias_h)

        # Activation here
        hidden.map(sigmoid)

        # Generating the output outputs
        output = Matrix.Multiply(self.weights_ho, hidden)
        output.addElementWise(self.bias_o)
        output.map(sigmoid)

        return output.toArray()
