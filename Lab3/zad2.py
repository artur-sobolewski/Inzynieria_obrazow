import cv2 as cv
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = (18, 10)
matplotlib.use('TkAgg')

image = cv.imread("images/example.jpg")

conv_matrix = [
    [0.393, 0.769, 0.189],
    [0.349, 0.689, 0.168],
    [0.272, 0.534, 0.131]
]

image = np.array(image, dtype='f')
image_copy = image.copy()
image_copy[:, :, :] = image_copy[:, :, :]/256.
image_copy = cv.cvtColor(image_copy, cv.COLOR_BGR2RGB)

x_res, y_res, z = image_copy.shape

conv_matrix = np.asmatrix(conv_matrix)

for y in range(y_res):
    for x in range(x_res):
        c = conv_matrix * [[image_copy[x, y, 0]],
                           [image_copy[x, y, 1]],
                           [image_copy[x, y, 2]]]
        if (c[0] > 1.0):
            image_copy[x, y, 0] = 1.0
        else:
            image_copy[x, y, 0] = c[0]
        if (c[1] > 1.0):
            image_copy[x, y, 1] = 1.0
        else:
            image_copy[x, y, 1] = c[1]
        if (c[2] > 1.0):
            image_copy[x, y, 2] = 1.0
        else:
            image_copy[x, y, 2] = c[2]
plt.imshow(image_copy)
plt.show();
