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

def alignBottom(image, len_x, len_y):
    newImage = [[0 for i in range(len_y)] for j in range(len_x)]

    start_x = len_x - len(image)
    start_y = len_y - len(image[0])

    for x in range(len(image)):
        for y in range(len(image[0])):
            newImage[start_x + x][start_y + y] = image[x][y]
    
    return newImage

def printImage(x, y, image):
    for image_x in range(len(image)):
        for image_y in range(len(image[0])):
            if image[image_x][image_y]:
                if (x + image_x) < cols and (x + image_x) >= 0:
                    lights[(x + image_x) % cols][(y + image_y) % rows] = image[image_x][image_y] * 100

def printImages(x, y, images):
    max_x = 0
    max_y = 0
    for image in images:
        if (len(image) > max_x):
            max_x = len(image)
        if (len(image[0]) > max_y):
            max_y = len(image[0])

    for pos in range(len(images)):
        printImage(x + pos * (max_x + 1), y, alignBottom(images[pos], max_x, max_y))

def printHorizontallyWrap(y, images):
    max_x = 0
    for image in images:
        if (len(image) > max_x):
            max_x = len(image)

    printImages(cols - (frame_num % ((max_x + 1) * len(images) + cols)), 1, images)

def printHorizontallyNoWrap(y, images):
    printImages(cols - frame_num, y, images)


def printMessageHorizontally(y, message):
    chars = message.upper()
    images = [0] * len(chars)


    for i in range(len(chars)):
        images[i] = letters[chars[i]]

    printHorizontallyWrap(y, images)


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
    printMessageHorizontally(1, "hello handsome")
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


def key_pressed(event):
    background(0, 0, 0)


run()
