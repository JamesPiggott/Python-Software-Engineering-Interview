'''
  Heapsort.

  This is the Python implementation of the Heapsort sorting algorithm as it applies to an array of Integer values.

  Running time: ?
  Data movement: ?

  @author James Piggott.

'''

class Heapsort(object):

    def __init__(self):
        print()

    def heapify(self, arr, n, i):
        largest = i
        l = 2 * i + 1  # left = 2*i + 1
        r = 2 * i + 2  # right = 2*i + 2

        if l < n and arr[i] < arr[l]:
            largest = l

        if r < n and arr[largest] < arr[r]:
            largest = r

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.heapify(arr, n, largest)

    def heapSort(self, arr):
        n = len(arr)

        for i in range(n, -1, -1):
            Heapsort.heapify(arr, n, i)

        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]  # swap
            Heapsort.heapify(arr, i, 0)


def main():
    unsorted = [7, 3, 8, 2, 1, 9, 4, 6, 5, 0]

    heap = Heapsort()

    heap.heapSort(unsorted)

    print(unsorted)

if __name__ == "__main__":
   # print(timeit.timeit("main()", setup="from __main__ import Heapsort"))

    main()
