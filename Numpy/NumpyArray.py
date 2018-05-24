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

    a = np.array([1, 2, 5, 10, 30, 42])
    b = np.array([[1, 2, 5.5, 10], [30, 42, 86]])

    # With shape the size of an Numpy array can be retrieved
    print("Array a has size: ", a.shape)  # A has 7 elements so shape is 7
    print("Array b has size: ", b.shape)  # B has 2 elements (2 arrays) so shape is 2

    # With reshape the shape of array can be changed without affecting the data (such as the transpose)
    c = np.reshape(a, (3, 2))
    print("Now a is a 3 by 2 matrix", c)

    # If we are not certain about the shape we can use a placeholder value '-1'
    d = np.reshape(a, (3, -1))
    print("Now a is a 3 by 2 matrix", d)


def advancedNumpy():

    # With ndarray we can fully customize an Numpy array. Lets see what a Christmas tree implementation looks like
    example = np.ndarray(shape=(3, 2), dtype=float, order='F')
    print(example)

    # argmax


def plottingNumpyArrays():
    plt.plot(np.linspace(0, 3, 8))  # This should be a straight line defined by 8 elements ranging from 0 to 3
    plt.show()


if __name__ == "__main__":

    simplePythonArrays()
    simpleNumpy()
    # plottingNumpyArrays()
    linearAlgebraWithNumpy()
    advancedNumpy()