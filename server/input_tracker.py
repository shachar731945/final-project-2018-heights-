import pyHook
import pythoncom
from win32api import SetCursorPos, GetSystemMetrics


class InputTracker:

    def __init__(self, confirm, communication_handle):
        self._hm = pyHook.HookManager()
        self._hm.HookKeyboard()
        self._hm.HookMouse()
        self._confirm_state = confirm
        self._communication_handle = communication_handle
        self._static_position = (GetSystemMetrics()[0], GetSystemMetrics()[1])
        self._hm.KeyDown = self.keyboard_press
        self._hm.KeyUp = self.keyboard_release
        self._hm.MouseAll = self.mouse_event
        self._hm.SubscribeMouseLeftDown(self.mouse_left_down)
        self._hm.SubscribeMouseMiddleDown(self.mouse_middle_down)
        self._hm.SubscribeMouseRightDown(self.mouse_right_down)
        self._hm.SubscribeMouseLeftUp(self.mouse_left_up)
        self._hm.SubscribeMouseMiddleUp(self.mouse_middle_up)
        self._hm.SubscribeMouseRightUp(self.mouse_right_up)
        pythoncom.PumpMessages()

    def keyboard_press(self, event):
        self._communication_handle.send("k|p|" + str(event.KeyID))
        return self._confirm_state

    def keyboard_release(self, event):
        self._communication_handle.send("k|r|" + str(event.KeyID))
        return self._confirm_state

    def mouse_event(self, event):
        if event.MessageName == "mouse wheel":
            print("wheel " + str(event.Wheel))
            self._communication_handle.send("m|w|" + str(event.Wheel))
            # how is the scroll how is it
        elif event.MessageName == "mouse move":
            position = event.Position
            movement = (position[0] - self._static_position[0], position[1] - self._static_position[1])
            print("move " + str(event.Position))
            print("movement " + str(movement))
            self._communication_handle.send("m|m|" + str(movement))
        if event.Injected:
            return True
        return False

    def mouse_left_down(self, event):
        self._communication_handle.send("m|c|l|d")
        return self._confirm_state

    def mouse_left_up(self, event):
        self._communication_handle.send("m|c|l|u")
        return self._confirm_state

    def mouse_middle_down(self, event):
        self._communication_handle.send("m|c|m|d")
        return self._confirm_state

    def mouse_middle_up(self, event):
        self._communication_handle.send("m|c|m|u")
        return self._confirm_state

    def mouse_right_down(self, event):
        self._communication_handle.send("m|c|r|d")
        return self._confirm_state

    def mouse_right_up(self, event):
        self._communication_handle.send("m|c|r|u")
        return self._confirm_state

# just for check
SetCursorPos((960, 540))
InputTracker(False, 5)






