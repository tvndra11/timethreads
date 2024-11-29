import threading
import concurrent.futures
timerlen = []
def wait(timeToSleep):
    import time
    timedef1 = time.perf_counter()
    timedef2 = 0
    while timedef2 <= timedef1 + timeToSleep:
        timedef2 = time.perf_counter()
    print(str(timeToSleep) + 's waited')
timers = int(input('how many timers do you want: '))
for i in range(timers):
    timerlen.append(int(input('how long for timer')))
pool = concurrent.futures.ThreadPoolExecutor(max_workers=timers)
for i in range(timers):
    pool.submit(wait,timerlen[i])
pool.shutdown(wait=True)