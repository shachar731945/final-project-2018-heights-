import pyHook
import pythoncom
from win32gui import GetCursorPos


class InputTracker:

    def __init__(self, confirm, input_hub):
        self._hm = pyHook.HookManager()
        self._hm.HookKeyboard()
        self._hm.HookMouse()
        self._confirm_state = confirm
        self._input_hub = input_hub
        self._hm.KeyDown = self.keyboard_press
        self._hm.KeyUp = self.keyboard_release
        self._hm_MouseAll = self.mouse_event
        self._hm.SubscribeMouseLeftDown(self.mouse_left_down)
        self._hm.SubscribeMouseMiddleDown(self.mouse_middle_down)
        self._hm.SubscribeMouseRightDown(self.mouse_right_down)
        self._hm.SubscribeMouseLeftUp(self.mouse_left_up)
        self._hm.SubscribeMouseMiddleUp(self.mouse_middle_up)
        self._hm.SubscribeMouseRightUp(self.mouse_right_up)
        pythoncom.PumpMessages()

    def keyboard_press(self, event):
        self._input_hub.send_input("k|p|" + str(event.KeyID))
        return self._confirm_state

    def keyboard_release(self, event):
        self._input_hub.send_input("k|r|" + str(event.KeyID))
        return self._confirm_state

    def mouse_event(self, event):
        position = GetCursorPos()
        requested_position = (position[0] - event.Position[0],
                              position[1] - event.Position[1])
        self._input_hub.send_input("m|m|" + requested_position)
        self._input_hub.send_input("m|w|" + str(event.Wheel))
        return self._confirm_state

    def mouse_left_down(self, event):
        self._input_hub.send_input("m|c|l|d")
        return self._confirm_state

    def mouse_left_up(self, event):
        self._input_hub.send_input("m|c|l|u")
        return self._confirm_state

    def mouse_middle_down(self, event):
        self._input_hub.send_input("m|c|m|d")
        return self._confirm_state

    def mouse_middle_up(self, event):
        self._input_hub.send_input("m|c|m|u")
        return self._confirm_state

    def mouse_right_down(self, event):
        self._input_hub.send_input("m|c|r|d")
        return self._confirm_state

    def mouse_right_up(self, event):
        self._input_hub.send_input("m|c|r|u")
        return self._confirm_state



