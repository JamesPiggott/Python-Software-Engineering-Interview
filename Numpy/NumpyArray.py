'''
  Numpy

  A simpleNumpy tutorial

  @author James Piggott.

  Date: May 22 2018

'''
import numpy as np
import matplotlib.pyplot as plt


def simplePythonArrays():

    # one-dimensional array with 7 elements
    x = [1, 2, 5, 10, 30, 42, 86]

    # first element is indexed at 0 and last element at 6
    print("Values in array x at position 0 and 6 are: ", x[0], " and: ", x[6])

    # You can also count backwards, index -1 and -2 will return the last and next to last elements
    print("Values in array x at position -1 and -2 are: ", x[-1], " and: ", x[-2])

    # And returning ranges are also possible, use the semi colon
    print("First range: ", x[2:])     # This returns a sub-array from element 2 onwards

    print("Second range: ", x[1:6])   # This returns a sub-array from element 1 to but not including element 6

    # Finally we can also select the increment used choose elements
    print("Third range: ", x[0:5:2])  # Increment 2 skips the second and fourth elements

def simpleNumpy():

    # Same one-dimensional array as above
    y = np.array([1, 2, 5.5, 10, 30, 42, 86])

    # Numpy treats all the element as floating point numbers because one is defined as such
    print(y)

    # You can easily count the mean with mean()
    print("Mean of array y is:", np.mean(y))

    # Or the maximum and minimum values with max() and min()
    print("The max value is: ", np.max(y), " and the min is: ", np.min(y))

    # It is also possible to already reserve a new array in Numpy
    t = np.empty(10)    # This creates an array of 10 elements in memory.
    print("The empty array contains: ", t)  # The values displayed are whatever happens to be at that location in memory

    zeros = np.zeros(6)
    print("Array with just zeros:", zeros)    # Now we have created an array with just zero values

    ones = np.ones(8)
    print("Array with just ones:", ones)    # And now with ones

    # Finally we can create an array within a range and define how many elements should be defined
    # Numpy will try to divide the range into equal part to get right number of elements
    print("Linspace array:", np.linspace(0, 3, 8))

def linearAlgebraWithNumpy():
    print()
    # shape

    # reshape

    #


def advancedNumpy():
    print()
    # ndarray

    # argmax


def plottingNumpyArrays():
    plt.plot(np.linspace(0, 3, 8))  # This should be a straight line defined by 8 elements ranging from 0 to 3
    plt.show()



if __name__ == "__main__":

    simplePythonArrays()
    simpleNumpy()
    plottingNumpyArrays()