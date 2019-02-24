# The Function adds gaussian , salt-pepper , poisson and speckle noise in an image

# Parameters
#----------
# image : ndarray
#  Input image data. Will be converted to float.
# mode : str
#    One of the following strings, selecting the type of noise to add:

#   'gauss'     Gaussian-distributed additive noise.
#   'poisson'   Poisson-distributed noise generated from the data.
#   's&p'       Replaces random pixels with 0 or 1.
#   'speckle'   Multiplicative noise using out = image + n*image,where
#               n is uniform noise with specified mean & variance.


import numpy as np
import os
import cv2
def noisy(noise_typ,image):
   if noise_typ == "gauss":
      row,col,ch= image.shape
      mean = 0
      var = 10
      sigma = var**0.5
      gauss = np.random.normal(mean,sigma,(row,col,ch))
      gauss = gauss.reshape(row,col,ch)
      noisy = image + gauss
      return noisy

