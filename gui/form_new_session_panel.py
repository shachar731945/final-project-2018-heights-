import wx
import wx.lib.inspection
from sys import maxsize
from server.server_network_manager import get_local_ip_address
from threading import Thread

USER_MESSAGE = "when establishing session through other computers, write " \
               "this ip upon entering: {} "
FONT = 24


def evt_connect(win, func, evt_id):
    """Define Result Event."""
    win.Connect(-1, -1, evt_id, func)


class ResultEvent(wx.PyEvent):
    """Simple event to carry arbitrary result data."""
    def __init__(self, data, evt_id):
        """Init Result Event."""
        wx.PyEvent.__init__(self)
        self.SetEventType(evt_id)
        self.data = data


class NewSessionPanel(wx.Panel):

    def __init__(self, frame_size_x, frame_size_y, parent,
                 server_netwrok_manager):
        super(NewSessionPanel, self).__init__(parent)

        self.frame_size_x, self.frame_size_y = frame_size_x, frame_size_y
        self.SetSize((self.frame_size_x, self.frame_size_y))

        # overall_sizer = wx.Sizer()
        # message_sizer = wx.BoxSizer(wx.HORIZONTAL)

        # self.SetBackgroundColour(wx.Colour(0, 255, 0))

        font = wx.Font(FONT, wx.DEFAULT, wx.ITALIC, wx.NORMAL)
        self.__text_to_show = USER_MESSAGE.format(str(get_local_ip_address()))
        self.__text_ctrl = wx.TextCtrl(
            self,
            size=(self.frame_size_x*3/5, FONT*4),
            style=(wx.TE_READONLY | wx.TE_CENTER | wx.TE_MULTILINE),
            pos=(self.frame_size_x/5, self.frame_size_y/20),
            value=self.__text_to_show)
        self.__text_ctrl.SetFont(font)
        del self.__text_to_show

        self.__connected_computers_list = wx.ListCtrl(
            self, wx.ID_ANY,
            style=wx.LC_REPORT | wx.BORDER_SUNKEN | wx.LC_SORT_ASCENDING,
            size=(self.frame_size_x*3/10, self.frame_size_y*3/5),
            pos=(self.frame_size_x/10, self.frame_size_y*3/10))
        self.__connected_computers_list.InsertColumn(
            0, "computer number", width=self.frame_size_x/10)
        self.__connected_computers_list.InsertColumn(
            1, "ip", width=self.frame_size_x/10)
        self.__connected_computers_list.InsertColumn(
            2, "coordinates", wx.LIST_FORMAT_LEFT,
            width=self.frame_size_x/10)
        self._index = 0

        self.__new_connection_evt_id = wx.NewId()
        evt_connect(
            self, self.new_connection_update, self.__new_connection_evt_id)

        self.__connecting_new_clients_thread = Thread(
            target=server_netwrok_manager.recv_clients_function,
            args=(self, ResultEvent("", self.__new_connection_evt_id)))
        self.__connecting_new_clients_thread.daemon = True
        self.__connecting_new_clients_thread.start()

        self.Enable()
        self.Show()

    # def activate_new_connection_thread(self):
    #     custom_event = ResultEvent(self, self.__new_connection_evt_id)
    #


        # self.btn = wx.Button(self, -1, "click Me")
        # self.btn.Bind(wx.EVT_BUTTON, self.new_connection_update)
        # self.__ip_show_text1 = wx.StaticText(
        #     self, wx.ID_ANY, self.__text_to_show[0:len(self.__text_to_show)/2])
        # # self.__ip_show_text2 = wx.StaticText(
        # #     self, wx.ID_ANY,
        # #     self.__text_to_show[len(self.__text_to_show) / 2:])
        # self.__ip_show_text1.SetFont(font)
        # # self.__ip_show_text2.SetFont(font)
        # self.__ip_show_text1.Move(
        #     (self._frame_size_x/10, self._frame_size_y/5))
        # self.__ip_show_text2.Move(
        #     (self._frame_size_x / 10, self._frame_size_y / 5 + FONT))
        # self.__ip_show_text.SetSize(24)

        # message_sizer.Add(self.__ip_show_text, 1, wx.ALL, 5)
        # overall_sizer.Add(message_sizer, 0, wx.CENTER)
        #
        # self.SetSizer(overall_sizer)
        # overall_sizer.Fit(self)

    def new_connection_update(self, event):
        pos = self.__connected_computers_list.InsertItem(
            maxsize, str(self._index))
        ip_msg = event.data
        self.__connected_computers_list.SetItem(pos, 1, str(ip_msg))
        self._index += 1


        # missions
        # send message to client of computer number
        # store address in matrix
        # add button to start session











