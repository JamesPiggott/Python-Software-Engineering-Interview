'''
  Mergesort.

  This is the Python implementation of the Mergesort sorting algorithm as it applies to an array of Integer values.

  Running time: ?
  Data movement: ?

  @author James Piggott.

'''

import sys
import timeit

class Mergesort(object):

    def __init__(self):
        print()

    def mergesort(self, unsorted):
        if len(unsorted) > 1:
            mid = len(unsorted)//2
            leftHalf = unsorted[:mid]
            rightHalf = unsorted[mid:]

            self.mergesort(leftHalf)
            self.mergesort(rightHalf)

            i = 0
            j = 0
            k = 0

            while i < len(leftHalf) and j < len(rightHalf):
                if leftHalf[i] < rightHalf[j]:
                    unsorted[k] = leftHalf[i]
                    i = i + 1
                else:
                    unsorted[k] = rightHalf[j]
                    j = j + 1
                k = k + 1

            # Now deal with the residual parts of the sub-lists, they should already be sorted
            while i < len(leftHalf):
                unsorted[k] = leftHalf[i]
                i = i + 1
                k = k + 1

            while j < len(rightHalf):
                unsorted[k] = rightHalf[j]
                j = j + 1
                k = k + 1

def main():
    unsorted = [7, 3, 8, 2, 1, 9, 4, 6, 5, 0]

    merge = Mergesort()

    merge.mergesort(unsorted)

    print(unsorted)

if __name__ == "__main__":
    #print(timeit.timeit("main()", setup="from __main__ import Mergesort"))

    main()
