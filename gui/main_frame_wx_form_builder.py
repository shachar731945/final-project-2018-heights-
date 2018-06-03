# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid


###########################################################################
## Class MainFrame
###########################################################################

class MainFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString,
                          pos=wx.DefaultPosition, size=wx.Size(878, 598),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        vertical_sizer1 = wx.BoxSizer(wx.VERTICAL)

        self.new_session_panel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition,
                                          wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.new_session_panel.Hide()

        vertical_sizer2 = wx.BoxSizer(wx.VERTICAL)

        vertical_sizer2.AddSpacer(50)

        self.message_list_ctrl = wx.TextCtrl(self.new_session_panel, wx.ID_ANY,
                                             u"when connecting to session from other computer, enter this ip for connection: ",
                                             wx.DefaultPosition,
                                             wx.Size(700, 30), wx.TE_MULTILINE)
        self.message_list_ctrl.SetForegroundColour(wx.Colour(0, 0, 0))

        vertical_sizer2.Add(self.message_list_ctrl, 0,
                            wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 0)

        horizontal_sizer1 = wx.BoxSizer(wx.HORIZONTAL)

        horizontal_sizer1.AddSpacer(100)

        self.computers_list_ctrl = wx.ListCtrl(self.new_session_panel,
                                               wx.ID_ANY, wx.DefaultPosition,
                                               wx.Size(300, 300),
                                               wx.LC_ALIGN_LEFT | wx.LC_REPORT | wx.SUNKEN_BORDER)
        horizontal_sizer1.Add(self.computers_list_ctrl, 0,
                              wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)

        horizontal_sizer1.AddSpacer(200)

        self.form_session_button = wx.Button(self.new_session_panel, wx.ID_ANY,
                                             u"start forming table",
                                             wx.DefaultPosition,
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
        self.join_wxisting_session_panel.Hide()

        bSizer4 = wx.BoxSizer(wx.VERTICAL)

        bSizer4.AddSpacer(100)

        self.join_session_static_text = wx.StaticText(
            self.join_wxisting_session_panel, wx.ID_ANY,
            u"enter the code of the session manager", wx.DefaultPosition,
            wx.DefaultSize, 0)
        self.join_session_static_text.Wrap(-1)
        bSizer4.Add(self.join_session_static_text, 0,
                    wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer17 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer17.AddSpacer(100)

        self.enter_ip_text_ctrl = wx.TextCtrl(self.join_wxisting_session_panel,
                                              wx.ID_ANY, wx.EmptyString,
                                              wx.DefaultPosition,
                                              wx.Size(150, -1), 0)
        bSizer17.Add(self.enter_ip_text_ctrl, 0,
                     wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        bSizer17.AddSpacer(100)

        self.connect_to_session_button = wx.Button(
            self.join_wxisting_session_panel, wx.ID_ANY, u"enter code",
            wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer17.Add(self.connect_to_session_button, 0,
                     wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        bSizer17.AddSpacer(100)

        self.m_button6 = wx.Button(self.join_wxisting_session_panel, wx.ID_ANY,
                                   u"start session", wx.DefaultPosition,
                                   wx.DefaultSize, 0)
        bSizer17.Add(self.m_button6, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        bSizer4.Add(bSizer17, 1, wx.EXPAND, 5)

        self.join_wxisting_session_panel.SetSizer(bSizer4)
        self.join_wxisting_session_panel.Layout()
        bSizer4.Fit(self.join_wxisting_session_panel)
        vertical_sizer1.Add(self.join_wxisting_session_panel, 1,
                            wx.EXPAND | wx.ALL, 0)

        self.from_table_panel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition,
                                         wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.from_table_panel.Hide()

        bSizer9 = wx.BoxSizer(wx.VERTICAL)

        bSizer9.AddSpacer(50)

        self.user_message = wx.StaticText(self.from_table_panel, wx.ID_ANY,
                                          u"Fill in the table according to "
                                          u"the physical place of the "
                                          u"computers. If any, right click "
                                          u"the computer of the session "
                                          u"manager",
                                          wx.DefaultPosition, wx.DefaultSize,
                                          0)
        self.user_message.Wrap(-1)
        bSizer9.Add(self.user_message, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL,
                    5)

        bSizer9.AddSpacer(50)

        self.confirm_table_button = wx.Button(self.from_table_panel, wx.ID_ANY,
                                              u"confirm table and start "
                                              u"session",
                                              wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        bSizer9.Add(self.confirm_table_button, 0,
                    wx.ALL | wx.ALIGN_CENTER_VERTICAL |
                    wx.ALIGN_CENTER_HORIZONTAL,
                    0)

        bSizer9.AddSpacer(100)

        self.table_grid = wx.grid.Grid(self.from_table_panel, wx.ID_ANY,
                                       wx.DefaultPosition, wx.DefaultSize, 0)

        # Grid
        self.table_grid.CreateGrid(0, 0)
        self.table_grid.EnableEditing(True)
        self.table_grid.EnableGridLines(True)
        self.table_grid.EnableDragGridSize(False)
        self.table_grid.SetMargins(0, 0)

        # Columns
        self.table_grid.EnableDragColMove(False)
        self.table_grid.EnableDragColSize(True)
        self.table_grid.SetColLabelSize(30)
        self.table_grid.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Rows
        self.table_grid.EnableDragRowSize(True)
        self.table_grid.SetRowLabelSize(80)
        self.table_grid.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Label Appearance

        # Cell Defaults
        self.table_grid.SetDefaultCellAlignment(wx.ALIGN_CENTRE, wx.ALIGN_TOP)
        bSizer9.Add(self.table_grid, 0,
                    wx.ALL | wx.ALIGN_CENTER_VERTICAL |
                    wx.ALIGN_CENTER_HORIZONTAL,
                    0)

        self.from_table_panel.SetSizer(bSizer9)
        self.from_table_panel.Layout()
        bSizer9.Fit(self.from_table_panel)
        vertical_sizer1.Add(self.from_table_panel, 1, wx.EXPAND | wx.ALL, 0)

        self.SetSizer(vertical_sizer1)
        self.Layout()
        self.status_bar = self.CreateStatusBar(1,
                                               0 | wx.CLIP_CHILDREN |
                                               wx.NO_BORDER,
                                               wx.ID_ANY)
        self.menubar = wx.MenuBar(0)
        self.session_item = wx.Menu()
        self.start_new_session_item = wx.MenuItem(self.session_item, wx.ID_ANY,
                                                  u"new session",
                                                  wx.EmptyString,
                                                  wx.ITEM_NORMAL)
        self.session_item.Append(self.start_new_session_item)

        self.session_item.AppendSeparator()

        self.join_session_item = wx.MenuItem(self.session_item, wx.ID_ANY,
                                             u"join session", wx.EmptyString,
                                             wx.ITEM_NORMAL)
        self.session_item.Append(self.join_session_item)

        self.menubar.Append(self.session_item, u"Session")

        self.options_menu = wx.Menu()
        self.quit_menu_item = wx.MenuItem(self.options_menu, wx.ID_ANY,
                                          u"Quit", wx.EmptyString,
                                          wx.ITEM_NORMAL)
        self.options_menu.Append(self.quit_menu_item)

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
        self.confirm_table_button.Bind(wx.EVT_BUTTON,
                                       self.confirm_table_and_start_session)
        self.table_grid.Bind(wx.grid.EVT_GRID_CELL_RIGHT_CLICK,
                             self.select_server_computer)
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

    def confirm_table_and_start_session(self, event):
        event.Skip()

    def select_server_computer(self, event):
        event.Skip()

    def start_new_session_panel(self, event):
        event.Skip()

    def join_existing_session_panel(self, event):
        event.Skip()

    def quit(self, event):
        event.Skip()
