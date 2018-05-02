'''
  Quicksort.

  This is the Python implementation of the Quicksort sorting algorithm as it applies to an array of Integer values.

  Running time: ?
  Data movement: ?

  @author James Piggott.

'''

import sys

class Quicksort(object):

    def __init__(self):
        print()

    def quicksort(self, unsorted, low, high):
        if low < high:
            p = self.partition(unsorted, low, high)
            self.quicksort(unsorted, low, p - 1)
            self.quicksort(unsorted, p + 1, high)
        return unsorted

    def partition(self, unsorted, low, high):
        pivot = unsorted[high]
        i = low - 1

        for j in range(low, high+1):
            if unsorted[j] <= pivot:
                i = i + 1
                if i != j:
                    swap = unsorted[i]
                    unsorted[i] = unsorted[j]
                    unsorted[j] = swap
        return i

def main():
    unsorted = [7, 3, 8, 2, 1, 9, 4, 6, 5, 0]

    quick = Quicksort()

    quick.quicksort(unsorted, 0, 9)

    print(unsorted)

if __name__ == "__main__":
    main()
