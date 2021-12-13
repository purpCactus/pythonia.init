import cv2

# reading the image
img = cv2.imread('./img/raad.jpg')

# a grayscale converted copy of the image
img_grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# masking the image (cropping the lightning)
t, mask = cv2.threshold(img_grayscale, 195, 255, cv2.THRESH_BINARY)

# colore madde nazar
color = [226, 43, 138]

# painting the lightning colore madde nazar
img[mask == 255] = color

# showing the image
cv2.imshow("image2", img)
cv2.waitKey(0)
