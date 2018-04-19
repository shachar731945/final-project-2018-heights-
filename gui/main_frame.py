import wx
from gui.form_new_session_panel import NewSessionPanel
from server.server_network_manager import ServerNetworkManager

FRAME_SIZE_X, FRAME_SIZE_Y = 1500, 1000


class MainFrame(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(MainFrame, self).__init__(*args, **kwargs)

        self.SetSize((FRAME_SIZE_X, FRAME_SIZE_Y))

        menu_bar = wx.MenuBar()

        session_menu = wx.Menu()
        start_new_session_item = session_menu.Append(
            wx.ID_ANY, "start new session")
        self.Bind(wx.EVT_MENU, self.start_session_panel_activate,
                  start_new_session_item)
        join_existing_session_item = session_menu.Append(
            wx.ID_ANY, "join an establishing session")
        self.Bind(wx.EVT_MENU, self.join_existing_session_activate,
                  join_existing_session_item)

        options_menu = wx.Menu()
        quit_item = options_menu.Append(wx.ID_ANY, "Quit")
        self.Bind(wx.EVT_MENU, self.quit, quit_item)

        menu_bar.Append(session_menu, "Session")
        menu_bar.Append(options_menu, "Options")

        self.SetMenuBar(menu_bar)
        self.status_bar = self.CreateStatusBar(1,
                                               0 | wx.CLIP_CHILDREN |
                                               wx.NO_BORDER,
                                               wx.ID_ANY)

        # self._starting_panel = StartingPanel()

        self.SetTitle("View Teamer")
        self.Show()

    def bla(self, e):
        print("asd")

    def start_session_panel_activate(self, e):
        server_netwrok_manager = ServerNetworkManager()
        new_session_panel = NewSessionPanel(FRAME_SIZE_X, FRAME_SIZE_Y, self,
                                            server_netwrok_manager)
        new_session_panel.Enable()
        new_session_panel.Show()
        self.Update()
        self.Layout()
        # from time import sleep
        # sleep(10)

    def join_existing_session_activate(self, e):
        print("bla")

    def quit(self, e):
        self.Close()


