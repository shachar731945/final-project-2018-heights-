import wx
import wx.lib.inspection


class NewSessionPanel(wx.Panel):

    def __init__(self, frame_size_x, frame_size_y, parent):
        super(NewSessionPanel, self).__init__(parent)

        self._frame_size_x, self._frame_size_y = frame_size_x, frame_size_y
        self.SetSize((self._frame_size_x, self._frame_size_y))

        # sizer = wx.BoxSizer(wx.HORIZONTAL)

        # self.SetBackgroundColour(wx.Colour(0, 255, 0))

        self.__ip_show_text = wx.StaticText(
            self, wx.ID_ANY, "ip here")
        self.__ip_show_text.Move((self._frame_size_x/2, self._frame_size_y/2))

        # sizer.Add(self.__ip_show_text)
        #
        # self.SetSizer(sizer)

        self.Enable()
        self.Show()










