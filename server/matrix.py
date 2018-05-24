from server.pointer import Pointer


class Matrix:

    def __init__(self, row, col, row_pointer=0, col_pointer=0):
        print(row_pointer, "shushu ", col_pointer)
        self.pointer = Pointer(row_pointer, col_pointer)
        self._matrix = [[object for c in range(col)] for r in range(row)]
        # (row, col)
        # (0, 0) (0, 1)
        # (1, 0) (1, 1)

    def get(self, row, col):
        return self._matrix[row][col]

    def set(self, row, col, item):
        self._matrix[row][col] = item

    def get_pointer_value(self):
        # print("ququ", self.pointer.row, self.pointer.col)
        return self._matrix[self.pointer.row][self.pointer.col]

    def set_pointer_value(self, value):
        self._matrix[self.pointer.row][self.pointer.col] = value

    def set_pointer(self, pointer):
        self.pointer.row = pointer[0]
        self.pointer.col = pointer[1]

    def get_pointer(self):
        return self.pointer.get_tuple()

    def pointer_up(self):
        self.pointer.row -= 1

    def check_up(self):
        return self._matrix[self.pointer.row - 1][self.pointer.col]

    def pointer_down(self):
        self.pointer.row += 1

    def check_down(self):
        return self._matrix[self.pointer.row + 1][self.pointer.col]

    def pointer_right(self):
        print("update right to ")
        self.pointer.col += 1
        print(self.get_pointer(), "new pointer")

    def check_right(self):
        return self._matrix[self.pointer.row][self.pointer.col + 1]

    def pointer_left(self):
        self.pointer.col -= 1

    def check_left(self):
        return self._matrix[self.pointer.row][self.pointer.col - 1]




