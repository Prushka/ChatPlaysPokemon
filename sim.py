# USAGE
# python compare.py

# import the necessary packages
import numpy
from skimage import metrics
import numpy as np
import cv2


def mse(imageA, imageB):
    # the 'Mean Squared Error' between the two images is the
    # sum of the squared difference between the two images;
    # NOTE: the two images must have the same dimension
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])

    # return the MSE, the lower the error, the more "similar"
    # the two images are
    return err


def similarity(path1, imageB):
    # compute the mean squared error and structural similarity
    # index for the images
    imageA = cv2.cvtColor(cv2.resize(cv2.imread(path1), (64, 64)),
                          cv2.COLOR_BGR2GRAY)
    imageB = cv2.cvtColor(cv2.resize(numpy.array(imageB), (64, 64)),
                          cv2.COLOR_BGR2GRAY)
    s = metrics.structural_similarity(imageA, imageB)
    return s


def similarity_numpy(numpyA, numpyB):
    # compute the mean squared error and structural similarity
    # index for the images
    imageA = cv2.cvtColor(cv2.resize(numpyA, (64, 64)),
                          cv2.COLOR_BGR2GRAY)
    imageB = cv2.cvtColor(cv2.resize(numpyB, (64, 64)),
                          cv2.COLOR_BGR2GRAY)
    s = metrics.structural_similarity(imageA, imageB)
    return s
