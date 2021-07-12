import matplotlib.pyplot as plt
import numpy as np
import cv2

img = cv2.imread('../img/sky.jpg', 0)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20 * np.log(np.abs(fshift))

plt.subplot(121)
plt.imshow(img, cmap='gray')
plt.title("Input Image")
plt.axis('off')
plt.subplot(122)
plt.imshow(magnitude_spectrum, cmap='gray')
plt.title("Magnitude Spectrum")
plt.axis('off')
plt.show()