from p5 import *
import time
import random
from letters import letters

square_size = 20
padding = 10

rows = 10
cols = 30
lights = [[0 for i in range(rows)] for j in range(cols)]

current_hue = 120
target_hue = 120
hue_shift_per_frame = 3
frames_to_change_hue = 10

frame_num = 0
frame_dir = 1

def printChar(start_x, start_y, char):
    for char_x in range(len(char)):
        for char_y in range(len(char[0])):
            if char[char_x][char_y]:
                if (start_x + char_x) < cols and (start_x + char_x) >= 0:
                    lights[(start_x + char_x) % cols][(start_y + char_y) % rows] = 100

def printCharHorizontally(i, y, char):
    printChar(cols - (i % cols), 1, char)

def printMessage(start_x, start_y, message):
    chars = list(message.upper())
    for pos in (range(len(chars))):
        printChar(start_x + pos * 6, start_y, letters[chars[pos]])

def printMessageHorizontally(i, y, message):
    printMessage(cols - (i % (len(message) * 10)), y, message)


def getRandomPrettyColor():
    return Color(random_uniform(255), 200, 200)


def clearLights():
    global lights
    lights = [[0 for i in range(rows)] for j in range(cols)]


def displayLights():
    printOnSameLine(
        "".join(map(lambda l: u"\u25A0" if l else u"\u25A1", lights)))
    # print("".join(map(lambda l: u"\u25A0" if l else u"\u25A1", lights)))


def turnOn(start, count, frame_dir):
    # r = if frame_dir == 1 else range(0, -count, frame_dir)
    for i in range(count):
        x = (start + i) % cols
        y = ((start + i) // cols) % rows
        lights[x][y] = 100 * (i + 1 if frame_dir == 1 else count - i) / count


def update(i, frame_dir):
    clearLights()
    # printCharHorizontally(i, 1, letters["A"])
    printMessageHorizontally(i, 1, "hello handsome")
    # turnOn(i, 3, frame_dir)
    time.sleep(0.05)


def setup():
    size(960, 360)
    no_stroke()
    color_mode('HSB', 360, 100, 100)
    background(0, 0, 0)


def draw():
    global frame_num, frame_dir, current_hue, target_hue, hue_shift_per_frame

    # Clear screen
    background(0, 0, 0)

    # TODO: Draw current state of lights
    for x in range(cols):
        for y in range(rows):
            if lights[x][y]:
                # fill(123, 19, 49, 43 + 5 * x + 5 * y)
                # fill(getRandomPrettyColor())
                fill(current_hue, 80, lights[x][y])
                circle(((square_size + padding) * (x + 1),
                        (square_size + padding) * (y + 1)), square_size)

    # TODO: Update lights
    update(frame_num, frame_dir)
    frame_num += frame_dir

    # if random_uniform(100) < 3:
    #     target_hue = random.randint(0, 360)
    #     hue_shift_per_frame = abs(
    #         current_hue - target_hue) / frames_to_change_hue
    #     frame_dir *= -1

    if (abs(current_hue - target_hue) < hue_shift_per_frame):
        current_hue = target_hue
    elif (current_hue > target_hue):
        current_hue -= hue_shift_per_frame
    elif (current_hue < target_hue):
        current_hue += hue_shift_per_frame

    # if mouse_is_pressed:
    #     fill(random_uniform(255), random_uniform(127), random_uniform(51), 127)
    # else:
    #     fill(255, 15)

    # circle_size = random_uniform(low=10, high=80)

    # circle((mouse_x, mouse_y), circle_size)


def key_pressed(event):
    background(0, 0, 0)


run()
