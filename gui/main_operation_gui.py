import wx
from gui.main_frame import MainFrame


def main():
    app = wx.App()
    frame = MainFrame(
        None,
        style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))
    app.MainLoop()


if __name__ == '__main__':
    main()





