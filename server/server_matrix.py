from server.matrix import Matrix
from server.pointer import Pointer


class ServerMatrix(Matrix):
    """
    the ServerMatrix class contains  a2 dimensional matrix according to it
    inheriting the Matrix class and in addition to the default pointer it has
    a server pointer (Pointer class) in order to allow more usability
    """

    def __init__(self, row, col,
                 row_pointer=0, col_pointer=0,
                 server_row_pointer=0, server_col_pointer=0):
        """
        the function calls the __init__ function of the inherited class and
        creates the additional pointer
        :param row: the number of rows in the 2 dimensional matrix
        :param col: the number of cols in the 2 dimensional matrix
        :param row_pointer: the row component of the Matrix class pointer
        :param col_pointer: the col component of the Matrix class pointer
        :param server_row_pointer: the row component of the ServerMatrix class
        pointer
        :param server_col_pointer: the col component of the ServerMatrix class
        pointer
        """
        super(ServerMatrix, self).__init__(row, col, row_pointer, col_pointer)
        self.server_pointer = Pointer(server_row_pointer, server_col_pointer)

    def get_server_pointer(self):
        """
        :return: this function returns the server_pointer
        """
        return self.server_pointer.get_tuple()


