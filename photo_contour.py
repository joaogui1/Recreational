#!/usr/bin/env python3
import imageio
import numpy as np
import matplotlib.pyplot as plt

filename = input("photo name:\t")
image = imageio.imread(filename)

image = image / image.max(axis=(0, 1, 2))

bw_image = (image[:, :, 0] + image[:, :, 1] + image[:, :, 2])/(3.)

grad_image = np.zeros_like(bw_image)
for i in range(1, bw_image.shape[0]-1):
    for j in range(1, bw_image.shape[1]-1):
        grad_image[i, j] = ((bw_image[i+1, j] - bw_image[i-1, j])**2 +
                            (bw_image[i, j+1] - bw_image[i, j-1])**2)**0.5

plt.imshow(grad_image, cmap='gray')
plt.show()
