'''
Author: Dylan8527 vvm8933@gmail.com
Date: 2023-02-17 20:26:54
LastEditors: Dylan8527 vvm8933@gmail.com
LastEditTime: 2023-02-17 20:36:01
FilePath: \Digital-Image-Processing\Methods\Intensity transformation\histogram.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''

import numpy as np
import matplotlib.pyplot as plt

img_path = './Figures/OpenCV/data/blox.jpg'


def histogram(img: np.ndarray) -> np.ndarray:
    # img: gray image, shape: (h, w), dtype: uint8 
    hist = np.zeros((256, 1))
    
    return hist
