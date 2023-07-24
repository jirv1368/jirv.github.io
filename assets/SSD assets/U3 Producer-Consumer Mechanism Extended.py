# Lock function added to so only 1 thread is accesses at a time.
from threading import Thread, Lock
from queue import Queue

q = Queue()
final_results = []

lock = Lock()

# The producer funtion needs to get the lock before addingg an item.
def producer():
    for i in range(100):
        lock.acquire()
        q.put(i)
        lock.release()

# The producer funtion needs to get the lock before addingg an item.
# It will chek to ee if the ques is empty, items wiil be emptied using q.get()
def consumer():
    while True:
        lock.acquire()
        if not q.empty():
            number = q.get()
            result = (number, number**2)
            final_results.append(result)
            q.task_done()
        lock.release()

for i in range(5):
    t = Thread(target=consumer)
    t.daemon = True
    t.start()

producer()

q.join()

print(final_results)
