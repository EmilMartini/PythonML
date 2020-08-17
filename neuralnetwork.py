from matrix import Matrix
import math


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


def derivsigmoid(x):
    return x * (1 - x)


class NeuralNetwork:

    def __init__(self, input_nodes, hidden_nodes, output_nodes, learningRate):
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

        self.learningrate = learningRate

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

    def train(self, inputs, targets):
        # Generating the hidden outputs
        inputs = Matrix.FromArray(inputs)
        hidden = Matrix.Multiply(self.weights_ih, inputs)
        hidden.addElementWise(self.bias_h)

        # Activation here
        hidden.map(sigmoid)

        # Generating the output outputs
        outputs = Matrix.Multiply(self.weights_ho, hidden)
        outputs.addElementWise(self.bias_o)
        outputs.map(sigmoid)

        # Converting array to new Matrix objects
        targets = Matrix.FromArray(targets)

        # Calculating the errors
        output_errors = Matrix.Subtract(targets, outputs)

        # Calculate gradient
        gradients = Matrix.Map(outputs, derivsigmoid)
        gradients.multiplyElementWise(output_errors)
        gradients.multiply(self.learningrate)

        # Calculate deltas
        hidden_t = Matrix.Transpose(hidden)
        weights_ho_deltas = Matrix.Multiply(gradients, hidden_t)

        # Adjust Hidden -> Output weights
        self.weights_ho.addElementWise(weights_ho_deltas)

        # Transposing the hidden-output weights and calculating those errors
        weights_ho_t = Matrix.Transpose(self.weights_ho)
        hidden_errors = Matrix.Multiply(weights_ho_t, output_errors)

        # Caluclate hidden gradient
        hidden_gradient = Matrix.Map(hidden, derivsigmoid)
        hidden_gradient.multiplyElementWise(hidden_errors)
        hidden_gradient.multiply(self.learningrate)

        # Calculate hidden deltas
        inputs_t = Matrix.Transpose(inputs)
        weights_ih_deltas = Matrix.Multiply(hidden_gradient, inputs_t)

        # Adjust Input -> Hidden weights
        self.weights_ih.addElementWise(weights_ih_deltas)
