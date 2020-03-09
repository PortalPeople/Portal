from letters import letters
import config

class Canvas:
    def __init__(self, cols, rows):
        self.board = [[0 for i in range(rows)] for j in range(cols)]
        self.cols = cols
        self.rows = rows

    def clear(self):
        self.board = [[0 for i in range(self.rows)] for j in range(self.cols)]


    def alignBottom(self, image, len_x, len_y):
        newImage = [[0 for i in range(len_y)] for j in range(len_x)]

        start_x = len_x - len(image)
        start_y = len_y - len(image[0])

        for x in range(len(image)):
            for y in range(len(image[0])):
                newImage[start_x + x][start_y + y] = image[x][y]
        
        return newImage


    def printImage(self, x, y, image):
        for image_x in range(len(image)):
            for image_y in range(len(image[0])):
                if image[image_x][image_y]:
                    if (x + image_x) < self.cols and (x + image_x) >= 0:
                        self.board[(x + image_x) % self.cols][(y + image_y) % self.rows] = image[image_x][image_y] * 100


    def printImages(self, x, y, images):
        max_x = 0
        max_y = 0
        for image in images:
            if (len(image) > max_x):
                max_x = len(image)
            if (len(image[0]) > max_y):
                max_y = len(image[0])

        for pos in range(len(images)):
            self.printImage(x + pos * (max_x + 1), y, self.alignBottom(images[pos], max_x, max_y))


    def printHorizontallyWrap(self, y, images):
        max_x = 0
        for image in images:
            if (len(image) > max_x):
                max_x = len(image)

        self.printImages(self.cols - (config.frame_num % ((max_x + 1) * len(images) + self.cols)), 1, images)

    def printHorizontallyNoWrap(self, y, images):
        self.printImages(self.cols - config.frame_num, y, images)


    def printMessageHorizontally(self, y, message):
        chars = message.upper()
        images = [0] * len(chars)

        for i in range(len(chars)):
            images[i] = letters[chars[i]]

        self.printHorizontallyWrap(y, images)