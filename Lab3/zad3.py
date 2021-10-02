import cv2 as cv
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

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

x_res, y_res, z = image.shape

for y in range(y_res):
    for x in range(x_res):
        c = conv_matrix * [[image[x, y, 0]],
                           [image[x, y, 1]],
                           [image[x, y, 2]]
                           ]
        c = c + [
            [0],
            [128],
            [128]
        ]
        if (c[0] > 255):
            image[x, y, 0] = 255
        else:
            image[x, y, 0] = c[0].astype(np.uint8)
        if (c[1] > 255):
            image[x, y, 1] = 255
        else:
            image[x, y, 1] = c[1].astype(np.uint8)
        if (c[2] > 255):
            image[x, y, 2] = 255
        else:
            image[x, y, 2] = c[2].astype(np.uint8)
plt.imshow(image)
plt.show();
