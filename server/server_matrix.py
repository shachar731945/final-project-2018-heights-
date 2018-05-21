from server.matrix import Matrix
from server.pointer import Pointer


class ServerMatrix(Matrix):

    def __init__(self, row, col,
                 row_pointer=0, col_pointer=0,
                 server_row_pointer=0, server_col_pointer=0):
        super(ServerMatrix, self).__init__(row, col, row_pointer, col_pointer)
        self.server_pointer = Pointer(server_row_pointer, server_col_pointer)

    def get_server_pointer(self):
        return self.server_pointer.get_tuple()


