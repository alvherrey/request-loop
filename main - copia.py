from threading import Thread 
import os 
from request import request
import sys
import time

def curl_function():
    print("lanzando curl")
    return request()


def create_threads(files_list):
    try:
        threads, results = [], []
        
        for _ in range(files_list):
            thread_object = ThreadWithReturnValue(target = curl_function)
            threads.append(thread_object)
            thread_object.start()
            time.sleep(3)

        for thread in threads:
            results.append(thread.join())

        i=0
        for result in results:
            with open(f"resultado_{i}", "w") as f:
                f.write(str(result))
            i+=1
        #print(str(results))
        return

    except Exception as e:
        raise e


class ThreadWithReturnValue(Thread):
    def __init__(self, group = None, target = None, name = None, args = (), kwargs = {}, Verbose = None):
        try:
            Thread.__init__(self, group, target, name, args, kwargs)
            self._return = None

        except Exception as e:
            raise e

    def run(self):
        try:
            if self._target is not None:
                self._return = self._target(*self._args, **self._kwargs)

        except Exception as e:
            raise e

    def join(self, *args):
        try:
            Thread.join(self, *args)
            return self._return

        except Exception as e:
            raise e



def main():
    create_threads(int(sys.argv[1]))


if __name__ == '__main__':
    main()
