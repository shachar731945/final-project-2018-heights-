class Computer:

    def __init__(self, addr):
        self.address = addr

    def __eq__(self, other):
        return other.address == self.address



