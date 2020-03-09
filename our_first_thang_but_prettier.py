from p5 import *
import time
import random
from letters import letters
import config
from canvas import *

square_size = 20
padding = 10

frames_to_change_hue = 10

canvas = Canvas(30, 10)

def getRandomPrettyColor():
    return Color(random_uniform(255), 200, 200)


def turnOn(count):
    # r = if config.frame_dir == 1 else range(0, -count)
    for i in range(count):
        x = (config.frame_num + i) % cols
        y = ((config.frame_num + i) // cols) % rows
        lights[x][y] = 100 * (i + 1 if config.frame_dir == 1 else count - i) / count


def update(canvas):
    canvas.clear()
    canvas.printMessageHorizontally(1, "hello handsome")
    # turnOn(3)
    time.sleep(0.05)


def setup():
    size(960, 360)
    no_stroke()
    color_mode('HSB', 360, 100, 100)
    background(0, 0, 0)


def draw():
    # Clear screen
    background(0, 0, 0)
    board = canvas.board

    # TODO: Draw current state of lights
    for x in range(canvas.cols):
        for y in range(canvas.rows):
            if board[x][y]:
                # fill(123, 19, 49, 43 + 5 * x + 5 * y)
                # fill(getRandomPrettyColor())
                fill(config.current_hue, 80, board[x][y])
                circle(((square_size + padding) * (x + 1),
                        (square_size + padding) * (y + 1)), square_size)

    # TODO: Update lights
    update(canvas)
    config.frame_num += config.frame_dir

    # if random_uniform(100) < 3:
    #     config.target_hue = random.randint(0, 360)
    #     config.hue_shift_per_frame = abs(
    #         config.current_hue - config.target_hue) / frames_to_change_hue
    #     config.frame_dir *= -1

    if (abs(config.current_hue - config.target_hue) < config.hue_shift_per_frame):
        config.current_hue = config.target_hue
    elif (config.current_hue > config.target_hue):
        config.current_hue -= config.hue_shift_per_frame
    elif (config.current_hue < config.target_hue):
        config.current_hue += config.hue_shift_per_frame


def key_pressed(event):
    background(0, 0, 0)


config.init()
run()
