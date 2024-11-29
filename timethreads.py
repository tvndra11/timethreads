import threading
def wait(timeToSleep):
    import time
    timedef1 = time.perf_counter()
    while timedef2 <= timedef1 + timeToSleep:
        timedef2 = time.perf_counter()
    print(timeToSleep + 's waited')
pool = concurrent.futures.ThreadPoolExecutor(max_workers=2)

pool.submit(wait,1)
pool.submit(wait,5)

pool.shutdown(wait=True)
