import win32api
import win32con


def move_mouse(position):
    win32api.SetCursorPos(position)


def click_mouse(click_state):
    button_dictionary = {'lu': win32con.MOUSEEVENTF_LEFTUP,
                         'ld': win32con.MOUSEEVENTF_LEFTDOWN,
                         'md': win32con.MOUSEEVENTF_MIDDLEDOWN,
                         'mu': win32con.MOUSEEVENTF_MIDDLEUP,
                         'ru': win32con.MOUSEEVENTF_RIGHTUP,
                         'rd': win32con.MOUSEEVENTF_RIGHTDOWN}
    win32api.mouse_event(button_dictionary[click_state], 0, 0)


def wheel_mouse(wheel_state):
    wheel_dictionary = {'u': 1, 'd': -1}
    win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, 0,
                         wheel_dictionary[wheel_state], 0)

# testing
from win32api import GetSystemMetrics
print GetSystemMetrics(1)




