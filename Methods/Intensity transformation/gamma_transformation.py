import numpy as np
import matplotlib.pyplot as plt
import cv2 
from PIL import Image

img_path = './Figures/OpenCV/data/blox.jpg'

def normalized_uint8(img: np.ndarray)->np.ndarray:
    # to uint8 0 ~ 255
    normalize_image = (img - img.min()) / (img.max() - img.min()) * 255
    normalize_image = normalize_image.astype(np.uint8)
    return normalize_image

def normalized_float(img: np.ndarray)->np.ndarray:
    # to float 0 ~ 1
    normalize_image = (img - img.min()) / (img.max() - img.min())
    return normalize_image

def gamma_transformation(img: np.ndarray, gamma=2.5) -> np.ndarray:
    normalized_image = normalized_float(img)
    gamma_image = normalized_image ** gamma
    gamma_image = normalized_uint8(gamma_image)
    return gamma_image

def diff_gamma(path: str):
    gammas = [0.04, 0.10, 0.20, 0.40, 1, 1.5, 2.5, 5.0, 10.0, 25.0]
    img = Image.open(path).convert("L")
    img = np.array(img)
    plt.figure()
    for i, gamma in enumerate(gammas):
        gamma_image = gamma_transformation(img, gamma)
        plt.subplot(2, 5, i+1)
        plt.title(f"gamma={gamma}", fontsize=10)
        plt.axis('off') 
        plt.imshow(gamma_image, cmap="gray")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    diff_gamma(img_path)