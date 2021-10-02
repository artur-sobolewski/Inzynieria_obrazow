import cv2 as cv
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# Ustawienie rozmarów wyświetlanych obrazów
plt.rcParams["figure.figsize"] = (18, 10)
matplotlib.use('TkAgg')

image = cv.imread("images/example.jpg")

kernel = [
    [-1, -1, -1],
    [-1, 8, -1],
    [-1, -1, -1]
]
kernel = np.asarray(kernel)
filtered_image = cv.filter2D(image, -1, kernel=kernel)

plt.imshow(cv.cvtColor(filtered_image, cv.COLOR_BGR2RGB))
plt.show();
