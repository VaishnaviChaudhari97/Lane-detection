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

def display_lines(img,lines):
    line_image = np.zeros_like(img)
    if lines is not None:
        for line in lines:
            for x1, y1, x2, y2 in line:
                cv2.line(line_image,(x1,y1),(x2,y2),(255,0,0),10)
    return line_image

image = cv2.imread('C:/Users/vaish/OneDrive/Documents/AI Project/test_image.jpg')
lane_image = np.copy(image)
#gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
#blur = cv2.GaussianBlur(gray,(5,5),0)
#canny = cv2.Canny(gray, 50, 150)
canny = canny(lane_image)
cropped_image = region_of_interest(canny)
lines = cv2.HoughLinesP(cropped_image, 2, np.pi/180, 100, np.array([]), minLineLength=40, maxLineGap=5)
lines_image = display_lines(lane_image, lines)
combo_image = cv2.addWeighted(lane_image, 0.8, lines_image, 1,1)
cv2.imshow("result", combo_image)
cv2.waitKey(0)