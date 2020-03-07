# from __future__ import print_function
# import time

import time
import curses

scr = curses.initscr()
color = curses.start_color()

# print("Hello world amazing <3")


num_lights = 8
lights = [False] * num_lights


def clearLights():
    global lights
    lights = [False] * num_lights


def printOnSameLine(s):
    # print('\x1b[2K\r',)
    # print(s)
    # print(s, end="\r")
    # print(u'{0}\r'.format(s),)
    scr.addstr(0, 0, s)
    scr.refresh()


def displayLights():
    printOnSameLine(
        "".join(map(lambda l: u"\u25A0" if l else u"\u25A1", lights)))
    # print("".join(map(lambda l: u"\u25A0" if l else u"\u25A1", lights)))


def turnOn(start, count):
    for i in range(start, start+count):
        lights[i % num_lights] = True


def snake(x):
    for i in range(x):
        clearLights()
        turnOn(i, 3)
        displayLights()
        time.sleep(0.1)


curses.endwin()


# -------------------------------------------------------------------------------
# Land of dead code
# -------------------------------------------------------------------------------

# print("Got here")

# snake(20)

# print("asdf\r",)
# time.sleep(.5)
# print("dsaf\r",)
# for x in range(10):
#     time.sleep(.5)
#     print('{0}\r'.format(x),)
# print

# for x in range(10):
#     print("Progress {:2.1%}".format(x / 10), end="\r2")

# scr.addstr(0, 0, "Current Time:")
# scr.addstr(2, 0, "Hello World!")
# while True:
#     scr.addstr(0, 20, time.ctime())
#     scr.refresh()
#     time.sleep(1)


# curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)

# scr.addstr(0, 0, "Pretty text", curses.color_pair(1))
# scr.refresh()

# time.sleep(2)
