from PIL import Image, ImageFilter
import numpy as np
import cv2
from ImageNoise import noisy

# Create a gray image 127
img = np.zeros((1000,1000,1), np.uint16)
# cv2.add(img, 127)
img += 127

# print(img)
# im = Image.open('Defect_4_Class_1_Internal.tiff')
# im.show()

#for j in range(14):
#    for i in range(14):
#        img = cv2.rectangle(img, (67 * (j + 1), 67 * (i + 1)), ( (67+30) * (j + 1) , (67+30) * (i + 1)), 250, -1)

img = cv2.rectangle(img, (67, 67), ((67+30),(67+30)), 250, -1)
img = cv2.rectangle(img, (67+3, 67+3), ((67+30-3),(67+30-3)), 64, -1)

# for i in range(14):
#   img = cv2.rectangle(img, (67+30*((i+1)*2), 67), ((67+30+30*((i+1)*2)),(67+30)), 250, -1)
#    img = cv2.rectangle(img, (67+30*((i+1)*2)+3, 67+3), ((67+30+30*((i+1)*2)-3),(67+30-3)), 63, -1)


i=0
j=1
for i in range(14):
    for j in range(14):
        img = cv2.rectangle(img, (67+30*((i )*2), 67+30*((j)*2)), ((67+30+30*((i)*2)),(67+30+30*((j)*2))), 250, -1)
        img = cv2.rectangle(img, (67+30*((i )*2)+3, 67+30*((j)*2)+3), ((67+30+30*((i)*2)-3),(67+30+30*((j)*2)-3)), 63, -1)


# img = cv2.circle(img,(67,67*2), 17, 250, -1)
# img = cv2.circle(img,(67,67*2), 15, 200, -1)

# img = cv2.circle(img,(67,67*3, 17, 250, -1)
# img = cv2.circle(img,(67,67*3), 15, 200, -1)

# img = cv2.circle(img,(67,67*4), 17, 250, -1)
# img = cv2.circle(img,(67,67*4), 15, 200, -1)

# img = cv2.circle(img,(67,67*4), 17, 250, -1)
# img = cv2.circle(img,(67,67*4), 15, 200, -1)

# print(type(img))
noise_img = noisy("gauss", img)
# print(type(noise_img))

kernel = np.ones((5, 5), np.float32) / 25
dst = cv2.filter2D(noise_img,-1,kernel)

# cv2.imshow("noise_image",img)

k= cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('Defect_1_Class_1_Internal.tiff',noise_img)
    cv2.destroyAllWindows()

cv2.imwrite('Rectangle_Defect_1_Class_1_Internal.tiff',noise_img)
