'''
  Insertionsort.

  This is the Python implementation of the Insertionsort sorting algorithm as it applies to an array of Integer values.

  Running time: ?
  Data movement: ?

  @author James Piggott.

'''

import sys
import timeit

class Insertionsort(object):

    def __init__(self):
        print()

    def insertionsort(self, unsorted):
        for i in range(0, len(unsorted)):
            for j in range(unsorted[i], 0, -1):
                if unsorted[j] < unsorted[j - 1]:
                    swap = unsorted[j - 1]
                    unsorted[j - 1] = unsorted[j]
                    unsorted[j] = swap

def main():
    unsorted = [7, 3, 8, 2, 1, 9, 4, 6, 5, 0]

    insert = Insertionsort()

    insert.insertionsort(unsorted)

    print(unsorted)

if __name__ == "__main__":
    # print(timeit.timeit("main()", setup="from __main__ import Insertionsort"))

    main()
