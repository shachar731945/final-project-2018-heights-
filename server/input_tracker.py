import pyHook
import pythoncom
from threading import Thread
from win32gui import GetCursorPos
# from multiprocessing import Process
# from mimik_keyboard import press_key, release_key
# from mimik_mouse import move_mouse, click_mouse, wheel_mouse


class InputTracker:

    def __init__(self, communication_handle, static_position,
                 update_pointer_pipe, pc_server_pointed=False):

        self._pc_server_pointed = pc_server_pointed
        self._hm = pyHook.HookManager()
        self._hm.HookKeyboard()
        self._hm.HookMouse()
        self._communication_handle = communication_handle
        self._static_position = static_position
        self._hm.MouseAll = self.mouse_event
        self._hm.SubscribeMouseLeftDown(self.mouse_left_down)
        self._hm.SubscribeMouseMiddleDown(self.mouse_middle_down)
        self._hm.SubscribeMouseRightDown(self.mouse_right_down)
        self._hm.SubscribeMouseLeftUp(self.mouse_left_up)
        self._hm.SubscribeMouseMiddleUp(self.mouse_middle_up)
        self._hm.SubscribeMouseRightUp(self.mouse_right_up)
        self._hm.KeyUp = self.keyboard_release
        self._hm.KeyDown = self.keyboard_press
        self._update_pointer_pipe = update_pointer_pipe
        self._update_thread = Thread(target=self.update_pointer)
        self._update_thread.start()
        pythoncom.PumpMessages()

    def update_pointer(self):
        while 1:
            data_recv = self._update_pointer_pipe.recv()
            if data_recv:
                print("hooking was updated ", data_recv)
                self._pc_server_pointed = eval(data_recv)
                print("nibba ", self._pc_server_pointed)
                print("position ", self._static_position, " ", GetCursorPos())

    def keyboard_press(self, event):
        if not self._pc_server_pointed:
            self._communication_handle.send("k|p|" + str(event.KeyID))
        return self._pc_server_pointed
        # print("was it injected ???", event.Injected, bool(event.Injected))
        # return True

    def keyboard_release(self, event):
        if not self._pc_server_pointed:
            self._communication_handle.send("k|r|" + str(event.KeyID))
        return self._pc_server_pointed
        # print("was it injected ???", event.Injected, bool(event.Injected))
        # return True

    def mouse_event(self, event):
        # print(self._pc_server_pointed)
        if not self._pc_server_pointed:
            if event.MessageName == "mouse move":
                position = event.Position
                # print(event.Injected, " injected")
                movement = (position[0] - self._static_position[0],
                            position[1] - self._static_position[1])
                print("movement", movement)
                self._communication_handle.send("m|m|" + str(movement))
            elif event.MessageName == "mouse wheel":
                print(self._pc_server_pointed)
                self._communication_handle.send("m|w|" + str(event.Wheel))
        return self._pc_server_pointed
        # print("kulululululullululu?")
        # print("was it injected ???", event.Injected, bool(event.Injected))
        # return True

    def mouse_left_down(self, event):
        if not self._pc_server_pointed:
            self._communication_handle.send("m|c|l|d")
        return self._pc_server_pointed
        # print("was it injected ???", event.Injected, bool(event.Injected))
        # return True

    def mouse_left_up(self, event):
        if not self._pc_server_pointed:
            self._communication_handle.send("m|c|l|u")
        return self._pc_server_pointed

    def mouse_middle_down(self, event):
        if not self._pc_server_pointed:
            self._communication_handle.send("m|c|m|d")
        return self._pc_server_pointed

    def mouse_middle_up(self, event):
        if not self._pc_server_pointed:
            self._communication_handle.send("m|c|m|u")
        return self._pc_server_pointed

    def mouse_right_down(self, event):
        if not self._pc_server_pointed:
            self._communication_handle.send("m|c|r|d")
        return self._pc_server_pointed

    def mouse_right_up(self, event):
        if not self._pc_server_pointed:
            self._communication_handle.send("m|c|r|u")
        return self._pc_server_pointed

# just for check
# from win32api import SetCursorPos
# SetCursorPos((960, 540))

#
# def press_keys():
#     from time import sleep
#     while 1:
#         wheel_mouse(-1)
#         sleep(0.5)
#
#
# def main():
#     from time import sleep
#     sleep(2)
#     p = Process(target=press_keys)
#     p.start()
#     InputTracker(3, 5)
#
#
# if __name__ == '__main__':
#     main()



