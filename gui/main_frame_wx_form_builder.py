# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc


###########################################################################
## Class MainFrame
###########################################################################

class MainFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString,
                          pos=wx.DefaultPosition, size=wx.Size(878, 598),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        vertical_sizer1 = wx.BoxSizer(wx.VERTICAL)

        self.new_session_panel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition,
                                          wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.new_session_panel.Hide()

        vertical_sizer2 = wx.BoxSizer(wx.VERTICAL)

        # vertical_sizer2.AddSpacer((0, 50), 0, wx.EXPAND, 0)

        self.message_list_ctrl = wx.TextCtrl(self.new_session_panel, wx.ID_ANY,
                                             u"when connecting to session from other computer, enter this ip for connection: ",
                                             wx.DefaultPosition,
                                             wx.Size(700, 30), wx.TE_MULTILINE)
        self.message_list_ctrl.SetForegroundColour(wx.Colour(0, 0, 0))

        vertical_sizer2.Add(self.message_list_ctrl, 0,
                            wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 0)

        horizontal_sizer1 = wx.BoxSizer(wx.HORIZONTAL)

        # horizontal_sizer1.AddSpacer((100, 0), 0, wx.EXPAND, 0)

        self.computers_list_ctrl = wx.ListCtrl(self.new_session_panel,
                                               wx.ID_ANY, wx.DefaultPosition,
                                               wx.Size(300, 300),
                                               wx.LC_ALIGN_LEFT | wx.LC_REPORT | wx.SUNKEN_BORDER)
        horizontal_sizer1.Add(self.computers_list_ctrl, 0,
                              wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)

        # horizontal_sizer1.AddSpacer((200, 0), 0, wx.EXPAND, 0)

        self.form_session_button = wx.Button(self.new_session_panel, wx.ID_ANY,
                                             u"MyButton", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        horizontal_sizer1.Add(self.form_session_button, 0,
                              wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        vertical_sizer2.Add(horizontal_sizer1, 1, wx.EXPAND, 5)

        self.new_session_panel.SetSizer(vertical_sizer2)
        self.new_session_panel.Layout()
        vertical_sizer2.Fit(self.new_session_panel)
        vertical_sizer1.Add(self.new_session_panel, 1, wx.EXPAND | wx.ALL, 0)

        self.join_wxisting_session_panel = wx.Panel(self, wx.ID_ANY,
                                                    wx.DefaultPosition,
                                                    wx.DefaultSize,
                                                    wx.TAB_TRAVERSAL)
        bSizer4 = wx.BoxSizer(wx.VERTICAL)

        self.join_session_static_text = wx.StaticText(
            self.join_wxisting_session_panel, wx.ID_ANY,
            u"enter the ip of the session manager", wx.DefaultPosition,
            wx.DefaultSize, 0)
        self.join_session_static_text.Wrap(-1)
        bSizer4.Add(self.join_session_static_text, 0,
                    wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer17 = wx.BoxSizer(wx.HORIZONTAL)

        self.enter_ip_text_ctrl = wx.TextCtrl(self.join_wxisting_session_panel,
                                              wx.ID_ANY, wx.EmptyString,
                                              wx.DefaultPosition,
                                              wx.Size(150, -1), 0)
        bSizer17.Add(self.enter_ip_text_ctrl, 0,
                     wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.connect_to_session_button = wx.Button(
            self.join_wxisting_session_panel, wx.ID_ANY, u"enter ip",
            wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer17.Add(self.connect_to_session_button, 0,
                     wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_button6 = wx.Button(self.join_wxisting_session_panel, wx.ID_ANY,
                                   u"MyButton", wx.DefaultPosition,
                                   wx.DefaultSize, 0)
        bSizer17.Add(self.m_button6, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        bSizer4.Add(bSizer17, 1, wx.EXPAND, 5)

        self.join_wxisting_session_panel.SetSizer(bSizer4)
        self.join_wxisting_session_panel.Layout()
        bSizer4.Fit(self.join_wxisting_session_panel)
        vertical_sizer1.Add(self.join_wxisting_session_panel, 1,
                            wx.EXPAND | wx.ALL, 0)

        self.form_matrix_panel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition,
                                          wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.form_matrix_panel.Hide()

        bSizer14 = wx.BoxSizer(wx.VERTICAL)

        horizontal_sizer111 = wx.BoxSizer(wx.HORIZONTAL)

        # horizontal_sizer111.AddSpacer((120, 0), 0, wx.EXPAND, 0)

        self.computers_list_ctrl_matrix = wx.ListCtrl(self.form_matrix_panel,
                                                      wx.ID_ANY,
                                                      wx.DefaultPosition,
                                                      wx.Size(300, 200),
                                                      wx.LC_ALIGN_LEFT | wx.LC_REPORT)
        horizontal_sizer111.Add(self.computers_list_ctrl_matrix, 0,
                                wx.ALL | wx.ALIGN_BOTTOM, 0)

        # horizontal_sizer111.AddSpacer((100, 0), 0, wx.EXPAND, 0)

        bSizer15 = wx.BoxSizer(wx.VERTICAL)

        # bSizer15.AddSpacer((0, 70), 0, wx.EXPAND, 0)

        self.start_session_button = wx.Button(self.form_matrix_panel,
                                              wx.ID_ANY,
                                              u"confirm matrix and start session",
                                              wx.DefaultPosition,
                                              wx.DefaultSize, wx.NO_BORDER)
        bSizer15.Add(self.start_session_button, 0,
                     wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL,
                     0)

        # bSizer15.AddSpacer((0, 70), 0, wx.EXPAND, 0)

        self.updtae_matrix_button = wx.Button(self.form_matrix_panel,
                                              wx.ID_ANY, u"update matrix",
                                              wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        bSizer15.Add(self.updtae_matrix_button, 0,
                     wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 0)

        self.m_button5 = wx.Button(self.form_matrix_panel, wx.ID_ANY,
                                   u"end session", wx.DefaultPosition,
                                   wx.DefaultSize, 0)
        bSizer15.Add(self.m_button5, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        horizontal_sizer111.Add(bSizer15, 1, wx.EXPAND, 5)

        bSizer14.Add(horizontal_sizer111, 1, wx.EXPAND, 5)

        gSizer71 = wx.GridSizer(2, 3, 0, 0)

        self.m_staticText71 = wx.StaticText(self.form_matrix_panel, wx.ID_ANY,
                                            u"X ratio", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText71.Wrap(-1)
        gSizer71.Add(self.m_staticText71, 0,
                     wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL,
                     5)

        self.m_staticText81 = wx.StaticText(self.form_matrix_panel, wx.ID_ANY,
                                            u"Y ratio", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText81.Wrap(-1)
        gSizer71.Add(self.m_staticText81, 0,
                     wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL,
                     5)

        self.m_staticText91 = wx.StaticText(self.form_matrix_panel, wx.ID_ANY,
                                            u"computer number",
                                            wx.DefaultPosition, wx.DefaultSize,
                                            0)
        self.m_staticText91.Wrap(-1)
        gSizer71.Add(self.m_staticText91, 0,
                     wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL,
                     5)

        self.x_text_ctrl = wx.TextCtrl(self.form_matrix_panel, wx.ID_ANY,
                                       wx.EmptyString, wx.DefaultPosition,
                                       wx.DefaultSize, 0)
        gSizer71.Add(self.x_text_ctrl, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL,
                     5)

        self.y_text_ctrl = wx.TextCtrl(self.form_matrix_panel, wx.ID_ANY,
                                       wx.EmptyString, wx.DefaultPosition,
                                       wx.DefaultSize, 0)
        gSizer71.Add(self.y_text_ctrl, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL,
                     5)

        self.pc_num_list_ctrl = wx.TextCtrl(self.form_matrix_panel, wx.ID_ANY,
                                            wx.EmptyString, wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        gSizer71.Add(self.pc_num_list_ctrl, 0,
                     wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer14.Add(gSizer71, 1, wx.EXPAND, 5)

        self.form_matrix_panel.SetSizer(bSizer14)
        self.form_matrix_panel.Layout()
        bSizer14.Fit(self.form_matrix_panel)
        vertical_sizer1.Add(self.form_matrix_panel, 1,
                            wx.EXPAND | wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 0)

        self.SetSizer(vertical_sizer1)
        self.Layout()
        self.status_bar = self.CreateStatusBar(1,
                                               0 | wx.CLIP_CHILDREN | wx.NO_BORDER,
                                               wx.ID_ANY)
        self.menubar = wx.MenuBar(0)
        self.session_item = wx.Menu()
        self.start_new_session_item = wx.MenuItem(self.session_item, wx.ID_ANY,
                                                  u"new session",
                                                  wx.EmptyString,
                                                  wx.ITEM_NORMAL)
        self.session_item.AppendItem(self.start_new_session_item)

        self.session_item.AppendSeparator()

        self.join_session_item = wx.MenuItem(self.session_item, wx.ID_ANY,
                                             u"join session", wx.EmptyString,
                                             wx.ITEM_NORMAL)
        self.session_item.AppendItem(self.join_session_item)

        self.menubar.Append(self.session_item, u"Session")

        self.options_menu = wx.Menu()
        self.quit_menu_item = wx.MenuItem(self.options_menu, wx.ID_ANY,
                                          u"Quit", wx.EmptyString,
                                          wx.ITEM_NORMAL)
        self.options_menu.AppendItem(self.quit_menu_item)

        self.menubar.Append(self.options_menu, u"Options")

        self.SetMenuBar(self.menubar)

        self.Centre(wx.BOTH)

        # Connect Events
        self.computers_list_ctrl.Bind(wx.EVT_LIST_ITEM_ACTIVATED,
                                      self.change_coordinates)
        self.form_session_button.Bind(wx.EVT_BUTTON, self.form_session)
        self.connect_to_session_button.Bind(wx.EVT_BUTTON,
                                            self.connect_to_session)
        self.m_button6.Bind(wx.EVT_BUTTON, self.start_session)
        self.computers_list_ctrl_matrix.Bind(wx.EVT_LIST_ITEM_ACTIVATED,
                                             self.change_coordinates)
        self.start_session_button.Bind(wx.EVT_BUTTON,
                                       self.end_session_calibration)
        self.updtae_matrix_button.Bind(wx.EVT_BUTTON, self.update_matrix)
        self.m_button5.Bind(wx.EVT_BUTTON, self.end_active_session)
        self.Bind(wx.EVT_MENU, self.start_new_session_panel,
                  id=self.start_new_session_item.GetId())
        self.Bind(wx.EVT_MENU, self.join_existing_session_panel,
                  id=self.join_session_item.GetId())
        self.Bind(wx.EVT_MENU, self.quit, id=self.quit_menu_item.GetId())

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def change_coordinates(self, event):
        event.Skip()

    def form_session(self, event):
        event.Skip()

    def connect_to_session(self, event):
        event.Skip()

    def start_session(self, event):
        event.Skip()

    def end_session_calibration(self, event):
        event.Skip()

    def update_matrix(self, event):
        event.Skip()

    def end_active_session(self, event):
        event.Skip()

    def start_new_session_panel(self, event):
        event.Skip()

    def join_existing_session_panel(self, event):
        event.Skip()

    def quit(self, event):
        event.Skip()
