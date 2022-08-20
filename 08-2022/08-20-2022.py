# Good morning! Here's your coding interview problem for today.

# This problem was asked by Apple.

# Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
# Soln: https://sathishbabu96n.medium.com/daily-coding-problem-problem-10-da50b93bfc67 

import time
def scheduler(f, n):
    time.sleep(n)
    f()


from time import sleep, time
import heapq, threading

class Scheduler:
    def __init__(self):
        self.functions = []
        thread = threading.Thread(target=self._poll)
        thread.start()
    def _poll(self):
        while True:
            now = time() * 1000
            if len(self.functions) > 0:
                due, func, args, kwargs = self.functions[0]
                if now > due:
                    func(*args, **kwargs)
                self.functions = [(due, func, args, kwargs) for due, func, args, kwargs in self.functions if due < now]
            sleep(0.01)
    def schedule(self, func, n, *args, **kwargs):
        heapq.heappush(self.functions, (n + time() * 1000, func, args, kwargs))