import matplotlib.pyplot as plt
import numpy as np
import cv2

img = cv2.imread('../../img/sky.jpg', 0)
dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)

magnitude_spectrum = 20 * np.log(cv2.magnitude(dft_shift[:,:,0], dft_shift[:,:,1]))

rows, cols = img.shape
crow,ccol = round(rows/2), round(cols/2)

mask = np.zeros((rows,cols,2),np.uint8)
mask[crow-30:crow+30,ccol-30:ccol+30] = 1

fshift = dft_shift*mask
f_ishift = np.fft.ifftshift(fshift)
img_back = cv2.idft(f_ishift)
img_back = cv2.magnitude(img_back[:,:,0],img_back[:,:,1])

plt.subplot(121)
plt.imshow(img, cmap='gray')
plt.title("Input Image")
plt.axis('off')

plt.subplot(122)
plt.imshow(magnitude_spectrum, cmap='gray')
plt.title("Magnitude Spectrum")
plt.axis('off')

plt.figure(figsize=(8,5))
plt.subplot(121)
plt.imshow(img,cmap='gray')
plt.title("Input Image")
plt.axis('off')

plt.subplot(122)
plt.imshow(img_back,cmap='gray')
plt.title("Magnitude Spectrum")
plt.axis('off')

plt.show()