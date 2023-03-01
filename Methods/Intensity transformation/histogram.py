'''
Author: Dylan8527 vvm8933@gmail.com
Date: 2023-02-17 20:26:54
LastEditors: Dylan8527 vvm8933@gmail.com
LastEditTime: 2023-03-01 23:47:25
FilePath: \Digital-Image-Processing\Methods\Intensity transformation\histogram.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''

import numpy as np
import matplotlib.pyplot as plt
import cv2 
from PIL import Image

img_path = './Figures/OpenCV/data/blox.jpg'


def histogram(img: np.ndarray) -> np.ndarray:
    # img: gray image, shape: (h, w), dtype: uint8 
    hist = np.zeros((256, 1), dtype=np.uint32)
    normalize_image = (img - img.min()) / (img.max() - img.min()) * 255
    normalize_image = normalize_image.astype(np.uint8)
    H, W = img.shape[:2]
    for i in range(H):
        for j in range(W):
            hist[normalize_image[i, j]] += 1
    return hist

def normalized_histogram(img: np.ndarray) -> np.ndarray:
    hist = histogram(img).astype(np.float32)
    H, W = img.shape[:2]
    hist = hist / (H * W)
    return hist

def simple_hist(path: str):
    img = Image.open(path).convert("L")
    img = np.array(img)
    hist = histogram(img)
    normalized_hist = normalized_histogram(img)

    plt.figure()
    plt.subplot(1, 2, 1)
    plt.plot(hist)
    plt.subplot(1, 2, 2)
    plt.plot(normalized_hist)
    plt.show()


if __name__ == '__main__':
    simple_hist(img_path)