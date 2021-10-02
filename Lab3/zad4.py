import cv2 as cv
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import math

# Ustawienie rozmarów wyświetlanych obrazów
plt.rcParams["figure.figsize"] = (18, 10)
matplotlib.use('TkAgg')

image = cv.imread("images/example.jpg")

conv_matrix = [
    [0.229, 0.587, 0.114],
    [0.500, -0.418, -0.082],
    [-0.168, -0.331, 0.500]
]

conv_matrix = np.asmatrix(conv_matrix)
image = cv.cvtColor(image, cv.COLOR_BGR2RGB)

image_copy = image.copy()

x_res, y_res, z = image_copy.shape
cr_matrix = np.zeros((int(x_res/2), int(y_res/2)))
cb_matrix = np.zeros((int(x_res/2), int(y_res/2)))

for y in range(y_res):
    for x in range(x_res):
        c = conv_matrix * [[image_copy[x, y, 0]],
                           [image_copy[x, y, 1]],
                           [image_copy[x, y, 2]]
                           ]
        c = c + [
            [0],
            [128],
            [128]
        ]
        if (c[0] > 255):
            image_copy[x, y, 0] = 255
        else:
            image_copy[x, y, 0] = c[0].astype(np.uint8)
        if (c[1] > 255):
            image_copy[x, y, 1] = 255
        else:
            image_copy[x, y, 1] = c[1].astype(np.uint8)
        if (c[2] > 255):
            image_copy[x, y, 2] = 255
        else:
            image_copy[x, y, 2] = c[2].astype(np.uint8)

for y in range(0, y_res, 2):
    for x in range(0, x_res, 2):
        cr_matrix[int(x/2), int(y/2)] = image_copy[x, y, 1]
        cb_matrix[int(x/2), int(y/2)] = image_copy[x, y, 2]

for y in range(0, y_res, 2):
    for x in range(0, x_res, 2):
        image_copy[x, y, 1] = cr_matrix[int(x/2), int(y/2)]
        image_copy[x, y+1, 1] = cr_matrix[int(x/2), int(y/2)]
        image_copy[x+1, y, 1] = cr_matrix[int(x/2), int(y/2)]
        image_copy[x+1, y+1, 1] = cr_matrix[int(x/2), int(y/2)]
        image_copy[x, y, 2] = cb_matrix[int(x/2), int(y/2)]
        image_copy[x, y + 1, 2] = cb_matrix[int(x/2), int(y/2)]
        image_copy[x + 1, y, 2] = cb_matrix[int(x/2), int(y/2)]
        image_copy[x + 1, y + 1, 2] = cb_matrix[int(x/2), int(y/2)]

image_copy = cv.cvtColor(image_copy, cv.COLOR_YCrCb2RGB)
sum = 0
for y in range(y_res):
    for x in range(x_res):
        sum1 = 0
        for i in range(2):
            sum1 = sum1 + pow(int(image[x, y, i]) - int(image_copy[x, y, i]), 2)
        sum = sum + sum1
mse = math.sqrt(sum/(x*y))
print(str(mse) + "%")
plt.imshow(image_copy)
plt.show();
