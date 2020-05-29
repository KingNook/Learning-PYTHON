import numpy

class Mandelbrot:

    def __init__(self, x_dim, y_dim = None, iterations = 255, R_S = -1, R_E = 2, I_S = -1, I_E = 2):
        self.x = x_dim
        self.y = y_dim if y_dim else x_dim
        self.MAX_ITER = iterations

        self.real = (R_S, R_E - R_S)
        self.imaginary = (I_S, I_E - I_S)

        self.graph = numpy.zeros((self.x, self.y), int)

        self.update()

    def __str__(self):
        return self.graph.__str__()

    def check_pix(self, x, y):
        # Plot values from real start(R_S) to real end (R_E) and same for imaginaries (I_S tp I_E)
        c = complex(self.real[0] + (x / self.x) * self.real[1],
                    self.imaginary[0] + (y / self.y) * self.imaginary[1])
        n = 1
        z = c
        while n < self.MAX_ITER and abs(z) <= 2:
            z = z * z + c
            n += 1
        
        return n

    def update(self):

        for y_val in range(self.y):
            for x_val in range(self.x):
                self.graph[y_val, x_val] = self.check_pix(x_val, y_val)

        return True