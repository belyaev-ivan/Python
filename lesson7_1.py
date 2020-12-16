import numpy as np
class Matrix:
    def __init__(self, list1,):
        self.matrix = np.array(list1)


    def __str__(self):
        return  f"Матрица  \n{self.matrix}"

    def __add__(self, other):
        for i in range(len(self.matrix)):
            for x in range(len(other.matrix[i])):
                self.matrix[i][x] = self.matrix[i][x] + other.matrix[i][x]
        return Matrix.__str__(self)

    # def __add__(self, other):
    #    return Matrix(self.matrix + other.matrix)
    # Вариант 2






one_matrix = [[31, 22], [37, 43], [51, 86], [37, 43]]
two_matrix = [[32, 21], [36, 44], [50, 87], [50, 87]]

x1 = Matrix(one_matrix)
x2 = Matrix(two_matrix)
print(x1 + x2)