'''
  Multi-threading.

  This is the Python implementation of Multi-threading.

  Running time: ?
  Data movement: ?

  @author James Piggott.

'''


import time
import threading

threads = [2]


def printsomething():
    print("Starting: ",threading.current_thread().getName())
    time.sleep(2)
    print("Exiting: ", threading.current_thread().getName())


if __name__ == "__main__":

    try:
        print("Now Thread-1 will be created")

        threadone = threading.Thread(name="Thread-1", target=printsomething())
        threads.append(threadone.start())

        print("Now Thread-2 will be created")

        threadtwo = threading.Thread(name="Thread-2", target=printsomething())
        threads.append(threadtwo.start())
    except:
        print("Error: unable to start thread")