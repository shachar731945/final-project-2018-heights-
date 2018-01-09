import pyHook
import pythoncom


class InputTracker:

    def __init__(self, confirm, input_hub):
        self._hm = pyHook.HookManager()
        self._hm.HookKeyboard()
        self._hm.HookMouse()
        self.confirm_state = confirm
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
        self._input_hub.send_input("kp|" + event.KeyID)
        return self.confirm_state

    def keyboard_release(self, event):
        self._input_hub.send_input("kr|" + event.KeyID)
        return self.confirm_state

    def mouse_event(self, event):
        self._input_hub.send_input("mmove|" + event.Position)
        self._input_hub.send_input("mwheel|" + event.Wheel)
        return self.confirm_state

    def mouse_left_down(self, event):
        self._input_hub.send_input("mld")
        return self.confirm_state

    def mouse_left_up(self, event):
        self._input_hub.send_input("mlu")
        return self.confirm_state

    def mouse_middle_down(self, event):
        self._input_hub.send_input("mmd")
        return self.confirm_state

    def mouse_middle_up(self, event):
        self._input_hub.send_input("mmu")
        return self.confirm_state

    def mouse_right_down(self, event):
        self._input_hub.send_input("mrd")
        return self.confirm_state

    def mouse_right_up(self, event):
        self._input_hub.send_input("mru")
        return self.confirm_state
