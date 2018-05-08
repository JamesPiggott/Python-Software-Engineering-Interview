'''
  Selectionsort.

  This is the Python implementation of the Selectionsort sorting algorithm as it applies to an array of Integer values.

  Running time: ?
  Data movement: ?

  @author James Piggott.

'''

import sys
import timeit

class Selectionsort(object):

    def __init__(self):
        print()

    def selectionsort(self, unsorted):

        for i in range(0, len(unsorted)):
            minvalue = unsorted[i]
            index = None
            for j in range(i+1, len(unsorted)):
                if unsorted[j] < minvalue:
                    minvalue = unsorted[j]
                    index = j
            if index is not None:
                unsorted[index] = unsorted[i]
                unsorted[i] = minvalue

def main():
    unsorted = [7, 3, 8, 2, 1, 9, 4, 6, 5, 0]

    selection = Selectionsort()

    selection.selectionsort(unsorted)

    print(unsorted)

if __name__ == "__main__":
    # print(timeit.timeit("main()", setup="from __main__ import Selectionsort"))

    main()
