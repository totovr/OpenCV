import numpy
import cv2
#from matplotlib import pyplot as plt
import matplotlib.pyplot as plt

def main():
    
    
    # upload Image and save it in a variable called img
    
    img= cv2.imread("Image/mx5.jpg")
    
    #Read image in gray scale with cv2.IMREAD_GRAYSCALE
    img= cv2.imread("Image/mx5.jpg",cv2.IMREAD_GRAYSCALE)
    
    #Save a new image with the function cv2.imwrite
    cv2.imwrite('Image/mazda.png',img)
    
    
    #Show the image in gray scale, and wait until one key is typed
    cv2.imshow('Window',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    #In Spyder you have to add another waitKey
    cv2.waitKey(1)
        
    
    
    matplotlib()
    
    return

def matplotlib():
    
    img = cv2.imread('Image/mx5.jpg')
    plt.imshow(img)
    plt.xticks([]), plt.yticks([])
    plt.show()
    
    
    return





if __name__ == '__main__':
    main()
