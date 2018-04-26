from gui.main_frame_wx_form_builder import MainFrame
import wx
from sys import maxsize
from threading import Thread
from server.server_network_manager import ServerNetworkManager
from server.matrix import Matrix
from server.computer import Computer
from server.simulation import SessionMain
from client.client_network_manager import ClientNetworkManager
from client.simulation_c import SessionClient
from threading import Lock, Event

UPDATE_MATRIX_COORDINATES_MESSAGE = "({0}, {1})"
COMPUTER_NUMBER_MESSAGE = "computer number: {0}"


def evt_connect(win, func, evt_id):
    """Define Result Event."""
    win.Connect(-1, -1, evt_id, func)


def evt_dissconnect(win, func, evt_id):
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

        self.__server_netwrok_manager = ServerNetworkManager()
        self.__client_netwrok_manager = None
        self.pc_matrix = None
        self._session_main = None
        self._session_client = None

        self.computers_list_ctrl_matrix.InsertColumn(0, "computer number",
                                                     width=150)
        self.computers_list_ctrl_matrix.InsertColumn(1, "coordinates",
                                                     width=100)

        self.computers_list_ctrl.InsertColumn(
            0, "computer number", width=50)
        self.computers_list_ctrl.InsertColumn(
            1, "ip", width=150)
        self._address_number_dictionary = {}
        # self.computers_list_ctrl.InsertColumn(
        #     2, "coordinates", wx.LIST_FORMAT_LEFT,
        #     width=100)

        self.__new_connection_evt_id = wx.NewId()
        self.__result_event = ResultEvent("", self.__new_connection_evt_id)
        self.__lock = Lock()
        self.confirm_state = Event()
        self.__connecting_new_clients_thread = Thread(
            target=self.__server_netwrok_manager.recv_clients_function,
            args=(self, self.__result_event, self.__lock,
                  self.confirm_state))
        self.__connecting_new_clients_thread.daemon = True

        self._index = 1

    def update_matrix(self, event):
        x_ratio = int(self.x_text_ctrl.GetValue())
        y_ratio = int(self.y_text_ctrl.GetValue())
        computer_number = int(self.pc_num_list_ctrl.GetValue())
        for pc_number in self._address_number_dictionary.keys():
            if pc_number == computer_number:
                self.pc_matrix.set(
                    x_ratio, y_ratio,
                    Computer(self._address_number_dictionary[pc_number]))
                self.computers_list_ctrl_matrix.SetItem(
                    pc_number - 1, 1,
                    UPDATE_MATRIX_COORDINATES_MESSAGE.format(x_ratio, y_ratio))
                if pc_number == 1:
                    self.pc_matrix.set_pointer((x_ratio, y_ratio))
                # update pc_number-1 or by good pos / not recommended
                # good way is to have numerical order
        print(x_ratio, y_ratio, computer_number)

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
        self.new_session_panel.Enable()
        self.new_session_panel.Show()
        self.Update()
        self.Layout()
        self.computers_list_ctrl.DeleteAllItems()
        evt_connect(
            self, self.new_connection_update, self.__new_connection_evt_id)
        self.__connecting_new_clients_thread.start()

    def join_existing_session_panel(self, event):
        # self.new_session_panel.Disable()
        # self.new_session_panel.Hide()
        self.join_wxisting_session_panel.Enable()
        self.join_wxisting_session_panel.Show()
        self.Update()
        self.Layout()

    def connect_to_session(self, event):
        ip_value, port = eval(self.enter_ip_text_ctrl.GetValue())
        self.__client_netwrok_manager = ClientNetworkManager(ip_value, port)
        self.__client_netwrok_manager.send_message("check")
        computer_number = self.__client_netwrok_manager.recv_message()
        self.status_bar.SetStatusText(
            COMPUTER_NUMBER_MESSAGE.format(computer_number), 0)
        print(ip_value)
        self._session_client = SessionClient(self.__client_netwrok_manager)
        self._session_client.start_session()

    def form_session(self, event):
        print("am i here?")
        self.confirm_state.set()
        evt_dissconnect(self, self.new_connection_update,
                        self.__new_connection_evt_id)
        pc_num = len(self._address_number_dictionary.keys())
        self.pc_matrix = Matrix(pc_num, pc_num)
        print(self._address_number_dictionary)
        for pc_number in self._address_number_dictionary.keys():
            print(pc_number)
            self.computers_list_ctrl_matrix.InsertItem(maxsize, str(pc_number))
        self.new_session_panel.Disable()
        self.new_session_panel.Hide()
        self.form_matrix_panel.Enable()
        self.form_matrix_panel.Show()
        self.Update()
        self.Layout()

    def end_session_calibration(self, event):
        self._session_main = SessionMain(
            self.__server_netwrok_manager, self.pc_matrix)
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



