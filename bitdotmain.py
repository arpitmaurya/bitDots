import cv2
import numpy as np
from PIL import Image as im
import sys
#
# oimage = cv2.imread("sample2.jpg",cv2.IMREAD_COLOR)
# greyimage = cv2.cvtColor(oimage, cv2.COLOR_BGR2GRAY)
# (thresh, blackimage) = cv2.threshold(greyimage,127,255,cv2.THRESH_BINARY)
# # #cv2.imshow("original", oimage)
# # #cv2.imshow("grey", greyimage)
# # cv2.imshow("bw",blackimage)
# #
# matrix = [blackimage]
# #
# # print(matrix)
# #
# # cv2.waitKey(0)
# # cv2.destroyAllWindows()
#
# #array = np.arange(0,25,1,np.uint8)
# array = np.reshape(matrix, (400,400))
# np.set_printoptions(threshold=np.inf)
# print(array)
# data = im.fromarray(array)
# data.save("output.png")
#

import sys
from PIL import Image

# pass the image as command line argument
#image_path = sys.argv[1]
img = Image.open("s9.jpeg")

# resize the image
width, height = img.size
aspect_ratio = height/width
new_width = 40
new_height = aspect_ratio * new_width * 0.40
img = img.resize((new_width, int(new_height)))
# new size of image
# print(img.size)

# converts my imagu to greyscale format
img = img.convert('L')
pixels = img.getdata()

# replace each 'pixel' with a 'character' from array
#chars = ["B","S","#","&","@","$","%",".","!",":"," "]
chars = ["B","S","#","&","@","$","%",".","!",":","."]

new_pixels = [chars[pixel//25] for pixel in pixels]
new_pixels = ''.join(new_pixels)

# split string of chars into multiple strings of length equal to new width and create a list
new_pixels_count = len(new_pixels)
ascii_image = [new_pixels[index:index + new_width] for index in range(0, new_pixels_count, new_width)]
ascii_image = "\n".join(ascii_image)
print(ascii_image)

# write to a text file.
with open("output.txt", "w") as f:
 f.write(ascii_image)

