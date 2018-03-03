class Matrix:

    def __init__(self, row, col):
        self._matrix = []
        self._pointer = 0, 0
        self._matrix = [[object for c in range(col)] for r in range(row)]
        # A bad way of creating this 2d array
        # for r in row:
        #     self._matrix.append([])
        #     for c in col:
        #         self._matrix[r].append(object)

    def get(self, row, col):
        return self._matrix[row][col]

    def set(self, row, col, item):
        self._matrix[row][col] = item

    def get_pointer_value(self):
        return self._matrix[self._pointer[0]][self._pointer[1]]

    def set_pointer_value(self, value):
        self._matrix[self._pointer[0]][self._pointer[1]] = value

    def set_pointer(self, coordinates):
        self._pointer = coordinates

    def get_pointer(self):
        return self._pointer

    def pointer_up(self):
        self._pointer[1] += 1

    def check_up(self):
        return self._matrix[self._pointer[0]][self._pointer[1]+1]

    def pointer_down(self):
        self._pointer[1] -= 1

    def check_down(self):
        return self._matrix[self._pointer[0]][self._pointer[1] - 1]

    def pointer_right(self):
        self._pointer[0] += 1

    def check_right(self):
        return self._matrix[self._pointer[0] + 1][self._pointer[1] + 1]

    def pointer_left(self):
        self._pointer[0] -= 1

    def check_left(self):
        return self._matrix[self._pointer[0] - 1][self._pointer[1] + 1]




