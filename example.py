from ppmCnv import ppm
import cv2


#initialize reader
image = ppm('test.ppm')
#covert image
CVimg = image.openImg()
#show result
cv2.imwrite('coverted.jpg', img=CVimg)
