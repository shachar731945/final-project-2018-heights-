import pyHook
import pythoncom
from threading import Thread
from win32gui import GetCursorPos
# from multiprocessing import Process
# from mimik_keyboard import press_key, release_key
# from mimik_mouse import move_mouse, click_mouse, wheel_mouse


class InputTracker:

    def __init__(self, communication_handle, update_pointer_pipe,
                 pc_server_pointed=False):
        """
        this is the initializing function of the tracking process. this process
        uses pyhook to "subscribe" certain io inputs to functions that will
        ultimately send then through pipe to the process which sends input to
        the client/controlled pc. the "pc_server_pointed" attribute is used
        to know if the controlled pc is the one currently running the
        session-manager server side component in order to know if to confirm
        ot reject the io input, will it be executed or not.another thread that
        runs while this process is running is the thread that changes the
        pc_server_pointed attribute through a pipe that connects this process
        to the process which receives matrix update from the clients.
        :param communication_handle: the pipe that io input information is sent
        through in order to send it to the controlled pc
        :param update_pointer_pipe: the pipe that is receiving updated
        "pc_server_pointed" attribute in order to change input direction
        :param pc_server_pointed: the pointer which is used to confirm or
        reject the io input and send it to the client
        """
        self._pc_server_pointed = pc_server_pointed
        self._hm = pyHook.HookManager()
        self._hm.HookKeyboard()
        self._hm.HookMouse()
        self._communication_handle = communication_handle
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
                self._pc_server_pointed = eval(data_recv)

    def keyboard_press(self, event):
        if not self._pc_server_pointed:
            self._communication_handle.send("k|p|" + str(event.KeyID))
        return self._pc_server_pointed

    def keyboard_release(self, event):
        if not self._pc_server_pointed:
            self._communication_handle.send("k|r|" + str(event.KeyID))
        return self._pc_server_pointed

    def mouse_event(self, event):
        # print(self._pc_server_pointed)
        if not self._pc_server_pointed:
            if event.MessageName == "mouse move":
                new_position = event.Position
                old_position = GetCursorPos()
                # print(event.Injected, " injected")
                movement = (new_position[0] - old_position[0],
                            new_position[1] - old_position[1])
                self._communication_handle.send("m|m|" + str(movement))
            elif event.MessageName == "mouse wheel":
                self._communication_handle.send("m|w|" + str(event.Wheel))
        return self._pc_server_pointed

    def mouse_left_down(self, event):
        if not self._pc_server_pointed:
            self._communication_handle.send("m|c|l|d")
        return self._pc_server_pointed

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
