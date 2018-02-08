class Matrix:

    def __init__(self, row, col):
        self._matrix = []
        for r in row:
            self._matrix.append([])
            for c in col:
                self._matrix[r].append(object)

    def get(self, row, col):
        return self._matrix[row][col]

    def set(self, row, col, item):
        self._matrix[row][col] = item
