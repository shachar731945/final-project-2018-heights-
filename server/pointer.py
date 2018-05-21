class Pointer:

    def __init__(self, row, col):
        print("poi", row, col)
        self.row = row
        self.col = col

    def get_tuple(self):
        return self.row, self.col

    def __eq__(self, other):
        return self.row == other.row and self.col == other.col


