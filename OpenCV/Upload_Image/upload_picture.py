import numpy
import cv2

# Save Image in a variable called imagen

imagen= cv2.imread("Image/mx5.jpg")

# With imshow function we can show a window with the image that we upload
# This function acept two parameters, name of the window and name of the
# varible that we will show, in this case "image"

cv2.imshow("Ventana de imagen", imagen)

# Wait for a key to be press, if you put a number inside of the () it will
# display a frame of "x" ms

cv2.waitKey(0)

# Close all the windows

cv2.destroyAllWindows()

#Mac as one bug so I added an extra waitKey

cv2.waitKey(1)
