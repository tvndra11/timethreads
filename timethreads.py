import threading
def wait(timeToSleep):
    import time
    time.sleep(timeToSleep)
    print(timeToSleep + 's waited')
t1 = threading.Thread(target=wait,args=(1,))