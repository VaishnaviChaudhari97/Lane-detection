import numpy as np
import cv2

def canny(img):
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    kernel = 5
    blur = cv2.GaussianBlur(gray,(kernel, kernel),0)
    canny = cv2.Canny(gray, 50, 150)
    return canny

def region_of_interest(canny):
    height = canny.shape[0]
    polygons = np.array([
        [(200, height), (1100, height), (550, 250)]
    ])
    mask = np.zeros_like(canny)
    cv2.fillPoly(mask, polygons, 255)
    masked_image = cv2.bitwise_and(canny, mask)
    return masked_image

image = cv2.imread('C:/Users/vaish/OneDrive/Documents/AI Project/test_image.jpg')
lane_image = np.copy(image)
#gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
#blur = cv2.GaussianBlur(gray,(5,5),0)
#canny = cv2.Canny(gray, 50, 150)
canny = canny(lane_image)
cropped_image = region_of_interest(canny)
cv2.imshow("result", cropped_image)
cv2.waitKey(0)