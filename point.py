class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.label = 1 if x > y else -1
