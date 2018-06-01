from gui.main_frame_wx_form_builder import MainFrame
import wx
from sys import maxsize
from threading import Thread
from server.server_network_manager import \
    ServerNetworkManager, get_local_ip_address
from server.server_matrix import ServerMatrix
from server.computer import Computer
from server.simulation import SessionMain
from client.client_network_manager import ClientNetworkManager
from client.simulation_c import SessionClient
from threading import Lock, Event
from server.coding import encode, decode
from ipaddress import ip_address

UPDATE_MATRIX_COORDINATES_MESSAGE = "({0}, {1})"
COMPUTER_NUMBER_MESSAGE = "computer number: {0}"


def evt_connect(win, func, evt_id):
    """Define Result Event."""
    win.Connect(-1, -1, evt_id, func)


def evt_disconnect(win, func, evt_id):
    win.Disconnect(-1, -1, evt_id, func)


class ResultEvent(wx.PyEvent):
    """Simple event to carry arbitrary result data."""
    def __init__(self, data, evt_id):
        """Init Result Event."""
        wx.PyEvent.__init__(self)
        self.SetEventType(evt_id)
        self.data = data


class ProgramFrame(MainFrame):

    def __init__(self, *args, **kwargs):
        MainFrame.__init__(self, *args, **kwargs)

        self.__server_netwrok_manager = None
        self.__client_netwrok_manager = None
        self.pc_matrix = None
        self._session_main = None
        self._session_client = None
        self.__connecting_new_clients_thread = None
        self._server_pc_coordinates = None

        # self.computers_list_ctrl_matrix.InsertColumn(0, "computer number",
        #                                              width=150)
        # self.computers_list_ctrl_matrix.InsertColumn(1, "coordinates",
        #                                              width=100)

        self.computers_list_ctrl.InsertColumn(
            0, "pc number", width=150)
        self.computers_list_ctrl.InsertColumn(
            1, "address", width=150)
        self._address_number_dictionary = {}
        # self.computers_list_ctrl.InsertColumn(
        #     2, "coordinates", wx.LIST_FORMAT_LEFT,
        #     width=100)

        self.__new_connection_evt_id = wx.NewId()
        self.__result_event = ResultEvent("", self.__new_connection_evt_id)
        self.__lock = Lock()
        self.confirm_state = Event()

        self._index = 1

    # def update_matrix(self, event):
    #     x_ratio = int(self.x_text_ctrl.GetValue())
    #     y_ratio = int(self.y_text_ctrl.GetValue())
    #     computer_number = int(self.pc_num_list_ctrl.GetValue())
    #     for pc_number in self._address_number_dictionary.keys():
    #         if pc_number == computer_number:
    #             self.pc_matrix.set(
    #                 x_ratio, y_ratio,
    #                 Computer(self._address_number_dictionary[pc_number]))
    #             self.computers_list_ctrl_matrix.SetItem(
    #                 pc_number - 1, 1,
    #                 UPDATE_MATRIX_COORDINATES_MESSAGE.format(x_ratio, y_ratio))
    #             if pc_number == 2:
    #                 self.pc_matrix.set_pointer((x_ratio, y_ratio))
    #     print(x_ratio, y_ratio, computer_number)

    def new_connection_update(self, event):
        self.__lock.acquire()
        pos = self.computers_list_ctrl.InsertItem(
            maxsize, str(self._index))
        ip_msg = event.data
        self.__result_event.data = self._index
        self.computers_list_ctrl.SetItem(pos, 1, str(ip_msg))
        self._address_number_dictionary[self._index] = ip_msg
        print(self._address_number_dictionary)
        self._index += 1
        self.__lock.release()

    def start_new_session_panel(self, event):
        # self.status_bar.SetStatusText("computer number 1", 0)
        # self.join_wxisting_session_panel.Disable()
        # self.join_wxisting_session_panel.Hide()
        self.computers_list_ctrl.DeleteAllItems()
        self.__server_netwrok_manager = ServerNetworkManager()
        # temp_byted_pc_address = str(
        #     (get_local_ip_address(),ab
        #      self.__server_netwrok_manager.port)).encode("utf-8")
        # self.message_list_ctrl.AppendText(b64encode(temp_byted_pc_address))
        addr = ip_address(get_local_ip_address())
        self.message_list_ctrl.AppendText(encode(int(addr)))
        self.__connecting_new_clients_thread = Thread(
            target=self.__server_netwrok_manager.recv_clients_function,
            args=(self, self.__result_event, self.__lock,
                  self.confirm_state))
        self.__connecting_new_clients_thread.daemon = True
        evt_connect(
            self, self.new_connection_update, self.__new_connection_evt_id)
        self.__connecting_new_clients_thread.start()
        self.new_session_panel.Enable()
        self.new_session_panel.Show()
        self.Update()
        self.Layout()

    def join_existing_session_panel(self, event):
        # self.new_session_panel.Disable()
        # self.new_session_panel.Hide()
        self.join_wxisting_session_panel.Enable()
        self.join_wxisting_session_panel.Show()
        self.Update()
        self.Layout()

    def connect_to_session(self, event):
        # change line below
        addr = ip_address(decode(self.enter_ip_text_ctrl.GetValue()))
        ip_value = str(addr)
        self.__client_netwrok_manager = ClientNetworkManager(ip_value)
        self.__client_netwrok_manager.send_message("check")
        computer_number, adrr = self.__client_netwrok_manager.recv_message()
        self.status_bar.SetStatusText(
            COMPUTER_NUMBER_MESSAGE.format(computer_number), 0)
        print(ip_value)
        self._session_client = SessionClient(self.__client_netwrok_manager)

    def start_session(self, event):
        self._session_client.start_session()

    # this is the old form_session version
    # def form_session(self, event):
    #     print("am i here?")
    #     self.confirm_state.set()
    #     evt_dissconnect(self, self.new_connection_update,
    #                     self.__new_connection_evt_id)
    #     pc_num = len(self._address_number_dictionary.keys())
    #     self.pc_matrix = Matrix(pc_num, pc_num)
    #     print(self._address_number_dictionary)
    #     for pc_number in self._address_number_dictionary.keys():
    #         print(pc_number)
    #         self.computers_list_ctrl_matrix.InsertItem(maxsize, str(pc_number))
    #     self.new_session_panel.Disable()
    #     self.new_session_panel.Hide()
    #     self.form_matrix_panel.Enable()
    #     self.form_matrix_panel.Show()
    #     self.Update()
    #     self.Layout()

    def form_session(self, event):
        print("am i here?")
        self.confirm_state.set()
        evt_disconnect(self, self.new_connection_update,
                       self.__new_connection_evt_id)
        pc_num = len(self._address_number_dictionary.keys())
        # from the next line start changing by adding rows and cols to table
        self.table_grid.AppendRows(pc_num)
        self.table_grid.AppendCols(pc_num)
        for i in range(pc_num):
            self.table_grid.SetColLabelValue(i, "")
            self.table_grid.SetRowLabelValue(i, "")
        self.new_session_panel.Disable()
        self.new_session_panel.Hide()
        self.from_table_panel.Enable()
        self.from_table_panel.Show()
        self.Update()
        self.Layout()

    def reset_grid_background_colours(self):
        pc_number = len(self._address_number_dictionary.keys())
        for row in range(pc_number):
            for col in range(pc_number):
                self.table_grid.SetCellBackgroundColour(row, col, wx.WHITE)

    def select_server_computer(self, event):
        self.reset_grid_background_colours()
        self.table_grid.SetCellBackgroundColour(
            event.GetRow(), event.GetCol(), wx.CYAN)
        self.table_grid.ForceRefresh()
        self._server_pc_coordinates = (event.GetRow(), event.GetCol())
        # the switch is because the (row, col) on wxGrid translates to
        # (col, row) on Matrix class

    def form_table(self):
        pc_number = len(self._address_number_dictionary.keys())
        print(pc_number)
        print(range(pc_number))
        try:
            # shouldn't be 0, 0
            self.pc_matrix = ServerMatrix(
                pc_number, pc_number,
                self._server_pc_coordinates[0], self._server_pc_coordinates[1],
                self._server_pc_coordinates[0], self._server_pc_coordinates[1])
        except TypeError:
            return False
        for row in range(pc_number):
            for col in range(pc_number):
                try:
                    temp_pc = Computer(self._address_number_dictionary[
                                int(self.table_grid.GetCellValue(row, col))])
                    self.pc_matrix.set(row, col, temp_pc)
                except ValueError:
                    pass
        return True

    def confirm_table_and_start_session(self, event):
        table_confirm = self.form_table()
        if table_confirm:
            self.end_session_calibration(None)

    def end_session_calibration(self, event):
        print("calibrating")
        for row in range(2):
            for col in range(2):
                print(self.pc_matrix.get(row, col))
        self._session_main = SessionMain(self.__server_netwrok_manager,
                                         self.pc_matrix)
        self._session_main.start_main()

    def quit(self, event):
        if self._session_main:
            self._session_main.stop_session()
        elif self._session_client:
            self._session_client.stop_session()
        self.Close()


def main_():
    a = wx.App()
    frum = ProgramFrame(None)
    frum.Show()
    a.MainLoop()


if __name__ == '__main__':
    main_()



