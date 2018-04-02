import wx
from form_new_session_panel import NewSessionPanel

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

        # self._starting_panel = StartingPanel()

        self.SetTitle("View Teamer")
        self.Show()

    def bla(self, e):
        print("asd")

    def start_session_panel_activate(self, e):
        new_session_panel = NewSessionPanel(FRAME_SIZE_X, FRAME_SIZE_Y, self)
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


