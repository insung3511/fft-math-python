import matplotlib.pyplot as plt
import numpy as np
import cv2

img = cv2.imread('../img/sky.jpg', 0)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20 * np.log(np.abs(fshift))

rows, cols = img.shape
crow, ccol = round(rows/2), round(cols/2)

fshift[crow-30:crow+60, ccol-30:ccol+30] = 0
f_ishift = np.fft.ifftshift(fshift)
img_back = np.fft.ifft2(f_ishift)
img_back = np.abs(img_back)

plt.figure(figsize=(12, 8))
plt.subplot(131)
plt.imshow(img, cmap='gray')
plt.title("Input Image")
plt.axis('off')

plt.subplot(132)
plt.imshow(img_back, cmap='gray')
plt.title("Image after ")
plt.axis('off')

plt.subplot(133)
plt.imshow(img_back)
plt.title("Input Image")
plt.axis('off')

plt.show()