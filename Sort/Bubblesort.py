'''
  Bubblesort.

  This is the Python implementation of the Bubblesort sorting algorithm as it applies to an array of Integer values.

  Running time: ?
  Data movement: ?

  @author James Piggott.

'''

import sys
import timeit

class Bubblesort(object):

    def __init__(self):
        print()

    def bubblesort(self, unsorted):

        endinnerLoop = len(unsorted)
        steps = 0

        for i in range(0, len(unsorted)):
            for j in range(1, endinnerLoop):
                if unsorted[j-1] > unsorted[j]:
                    swap = unsorted[j]
                    unsorted[j] = unsorted[j - 1]
                    unsorted[j - 1] = swap
                steps = steps + 1
                endinnerLoop = endinnerLoop - 1
        return unsorted


def main():
    unsorted = [7, 3, 8, 2, 1, 9, 4, 6, 5, 0]

    bubble = Bubblesort()

    bubble.bubblesort(unsorted)

    print(unsorted)

if __name__ == "__main__":
    print(timeit.timeit("main()", setup="from __main__ import Bubblesort"))

    # main()
