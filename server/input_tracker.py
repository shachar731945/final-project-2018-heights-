import pyHook
import pythoncom
from win32api import SetCursorPos, GetSystemMetrics


class InputTracker:

    def __init__(self, communication_handle):
        self._hm = pyHook.HookManager()
        self._hm.HookKeyboard()
        self._hm.HookMouse()
        self._communication_handle = communication_handle
        self._static_position = (
            int(GetSystemMetrics(0)/2), int(GetSystemMetrics(1)/2))
        self._hm.MouseAll = self.mouse_event
        self._hm.SubscribeMouseLeftDown(self.mouse_left_down)
        self._hm.SubscribeMouseMiddleDown(self.mouse_middle_down)
        self._hm.SubscribeMouseRightDown(self.mouse_right_down)
        self._hm.SubscribeMouseLeftUp(self.mouse_left_up)
        self._hm.SubscribeMouseMiddleUp(self.mouse_middle_up)
        self._hm.SubscribeMouseRightUp(self.mouse_right_up)
        self._hm.KeyDown = self.keyboard_press
        self._hm.KeyUp = self.keyboard_release
        SetCursorPos(self._static_position)
        # previous line shouldnt be here
        pythoncom.PumpMessages()

    def keyboard_press(self, event):
        self._communication_handle.send("k|p|" + str(event.KeyID))
        return event.Injected

    def keyboard_release(self, event):
        self._communication_handle.send("k|r|" + str(event.KeyID))
        return event.Injected

    def mouse_event(self, event):
        if event.MessageName == "mouse wheel":
            # print("wheel " + str(event.Wheel))
            self._communication_handle.send("m|w|" + str(event.Wheel))
        elif event.MessageName == "mouse move":
            position = event.Position
            movement = (position[0] - self._static_position[0],
                        position[1] - self._static_position[1])
            # print("static position " + str(self._static_position))
            # print("new position " + str(event.Position))
            # print("movement " + str(movement))
            self._communication_handle.send("m|m|" + str(movement))
        return event.Injected

    def mouse_left_down(self, event):
        self._communication_handle.send("m|c|l|d")
        return event.Injected

    def mouse_left_up(self, event):
        self._communication_handle.send("m|c|l|u")
        return event.Injected

    def mouse_middle_down(self, event):
        self._communication_handle.send("m|c|m|d")
        return event.Injected

    def mouse_middle_up(self, event):
        self._communication_handle.send("m|c|m|u")
        return event.Injected

    def mouse_right_down(self, event):
        self._communication_handle.send("m|c|r|d")
        return event.Injected

    def mouse_right_up(self, event):
        self._communication_handle.send("m|c|r|u")
        return event.Injected

# # just for check
# SetCursorPos((960, 540))
# InputTracker(5)






