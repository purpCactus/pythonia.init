import cv2
import numpy as np

img = cv2.imread("./img/raad.jpg")

# RESIZE
# size = (img.shape[1]//2, img.shape[0]//2)
# img = cv2.resize(img, size)


# print(img)
# print(img.dtype)

# print(img.size)
# print(img.shape)

# img = img.astype('float64')
#
# img = img * 1.5
# img = np.minimum(255, img)
# img = np.maximum(0, img)

# img = img.astype('uint8')

# img = img[100:500,700:1000,:]
# img[100:500:4,700:1000,:] += 50

# img[:,:,0] = 0  # B
# img[:,:,1] = 0  # G
# img[:,:,2] = 0  # R
# img[:, :, 0], img[:,:,1] = img[:,:,1], img[:,:,0 ]

# print(cv2.__version__)
# grayscale
# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

t, bw = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
print(bw.shape)
# print(type(res))
# print(res)

# otsu's thresholding
# t, bw = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# bw = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,2)

# cv2.imshow("my image", img)
# cv2.waitKey(0)
