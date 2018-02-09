import pythoncom
import pyHook


def on_keyboard_press(event):
    print chr(event.KeyID)
    return True


def on_keyboard_release(event):
    print chr(event.KeyID)
    return True


def on_mouse_event(event):
    # print event.Position
    print event.Wheel
    return True


def left_click(event):
    print "left_click"
    return True


def right_click(event):
    print "right_click"
    return True


def middle_click(event):
    print "middle click"
    return True


hm = pyHook.HookManager()
hm.HookKeyboard()
hm.HookMouse()
hm.KeyDown = on_keyboard_press
hm.KeyUp = on_keyboard_release
hm.MouseAll = on_mouse_event
# dont forget to include up
hm.SubscribeMouseLeftDown(left_click)
hm.SubscribeMouseRightDown(right_click)
hm.SubscribeMouseRightUp(right_click)
hm.SubscribeMouseMiddleDown(middle_click)
pythoncom.PumpMessages()
