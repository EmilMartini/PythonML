import random
import texttable as tt


class Matrix:

    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.data = [[0 for x in range(columns)]
                     for y in range(rows)]

    def randomize(self):
        for i in range(self.rows):
            for j in range(self.columns):
                self.data[i][j] = random.random() * 2 - 1

    def log(self):
        tab = tt.Texttable()
        for row in zip(self.data):
            tab.add_row(row)
        print(tab.draw())

    def add(self, num):
        for i in range(self.rows):
            for j in range(self.columns):
                self.data[i][j] = self.data[i][j] + num

    def addElementWise(self, num):
        for i in range(self.rows):
            for j in range(self.columns):
                self.data[i][j] + num.data[i][j]

    def toArray(self):
        arr = []
        for i in range(self.rows):
            for j in range(self.columns):
                arr.append(self.data[i][j])
        return arr

    def map(self, func):
        for i in range(self.rows):
            for j in range(self.columns):
                val = self.data[i][j]
                self.data[i][j] = func(val)

    # Memberfunction to multiply all elements inside this matrix with a given num
    def multiply(self, num):
        for i in range(self.rows):
            for j in range(self.columns):
                self.data[i][j] = self.data[i][j] * num

    def FromArray(input_array):
        m = Matrix(len(input_array), 1)
        for i in range(len(input_array)):
            m.data[i][0] = input_array[i]
        return m

    # Static function to transpose a e,g 3x2 matrix to a 2x3 matrix and return the result
    def Transpose(m1):
        if(m1.rows > m1.columns):
            print("Invalid format of input matrix")
            return

        result = Matrix(m1.columns, m1.rows)
        for i in range(m1.rows):
            for j in range(m1.columns):
                result.data[j][i] = m1.data[i][j]
        return result

    # Static function to multiply two matrices together and return a matrix with the result
    def Multiply(m1, m2):
        result = Matrix(m1.rows, m2.columns)
        for i in range(result.rows):
            for j in range(result.columns):
                sum = 0
                for k in range(m1.columns):
                    sum += m1.data[i][k] * m2.data[k][j]
                result.data[i][j] = sum
        return result


Matrix.Multiply = staticmethod(Matrix.Multiply)
Matrix.Transpose = staticmethod(Matrix.Transpose)
Matrix.FromArray = staticmethod(Matrix.FromArray)
