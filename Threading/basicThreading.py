"""
start()
can be called only once per thread
RunTimeError if called more than once
invokes run() method

===============================================
daemon()
lets the thread run even though main thread is finished
===============================================
join()
wait until thread is finished
By default, join() blocks indefinitely
pass a timeout argument to wait until timeout ends

join() returns None always either when:
1. Thread done
2. Timeout occurs
3. Exception

Need to call isAlive() when join() returns to check which condition was hit
================================================

enumerate()
Returns list of all alive threads
Includes daemonic threads, dummy threads and main thread
Excludes terminated threads and threads not started.

================================================
Timer()
Subclass of Thread.
Action starts only after timeout/delay specified
Can be canceled before start using cancel()
Start with start()
Cancel with cancel()

================================================
Event()
Communication between threads
set() - Sets flag
clear() - clears flag

wait(timeout) - blocks until flag is true
returns on either flag set, timeout
returns boolean - True when flag is set, False when timeout

isSet() - non-blocking call to check if event is set

=================================================
Lock()
Control access to shared resource
Synchronization primitive not owned by any thread when locked
Can be acquired on ONLY ONE thread

acquire()
when in unlocked state: changes state to locked, returns immediately
when in locked state: blocks until release() called by other thread changes state to unlocked.
                      Resets lock to locked and returns.

release()
Should only be called in locked state
Changes state to unlocked and returns immediately.
RunTimeError is release an unlocked lock.
====================================================

RLock()
Re-entrant locks
safely called again, meaning no global variables in use
Multiple threads can call this code with no impact to each other

RLock - can be acquired more than once.
In the same thread, can be "re-acquire" ed multiple times.
=====================================================

with context

All object with acquire(), release() calls can be used 'with' context
Dont need to explicitly call acquire() and release()

Block Enter: acquire() called
Block exit: release() called

with some_lock:
    # do something...

IS SAME AS

some_lock.acquire()
try:
    # do something...
finally:
    some_lock.release()
=========================================================
Condition Object

Synchronizing threads - condition object
Always associated with a lock
Lock can be passed in Or will have a default lock
When several CV need to share same lock, need to pass a lock
Can also be used as 'with' context manager

wait()
Consumer waits on CV being set
Releases the lock and blocks until another thread calls notify() or notifyAll()


notify()
notifyALL()
Producer calls this to wake up waiting consumer threads
These dont release the lock immediately. Need to finish the thread calling notify

Producer-Consumer Psuedocode
with cv:
    while not item_available:
        cv.wait()
    get_available_item()

with cv:
    make_item_available()
    cv.notify()
===========================================================




"""


import threading
import time
import random




"""
Helper Functions - Create + Start + Name threads

start()
can be called only once per thread
RunTimeError if called more than once
invokes run() method

"""
def fFunc():
    print("\n Thread started")
    time.sleep(1)
    print("Thread ended \n")


def fidFunc(id):
    print("\n Thread started: name: {}, id: {}".format(threading.current_thread().getName(), id))
    time.sleep(3)
    print("Thread ended: name: {}, id: {} \n".format(threading.current_thread().getName(), id))

def createThread():
    print(' ******** Creat + Start threads **********')
    for i in range(3):
        t = threading.Thread(target=fFunc)
        t.start()
        t.join() # Wait until t finishes

    t = threading.Thread(target=fidFunc, name='testThread', args=(1,))
    t.start()


"""
daemon()
lets the thread run even though main thread is finished
"""

def nFunc():
    print('\n Starting thread: {}'.format(threading.current_thread().getName()))
    print('Ending thread: {} \n'.format(threading.current_thread().getName()))

def dFunc():
    print('\n Starting thread: {}'.format(threading.current_thread().getName()))
    time.sleep(5)
    print('Ending thread: {} \n'.format(threading.current_thread().getName()))


def daemonThread():
    # Daemon threads
    print('\n********* Testing daemon threads *********\n')
    d = threading.Thread(target=dFunc, name='daemon')
    t = threading.Thread(target=nFunc, name='non-daemon')
    d.setDaemon(True)

    d.start()   # Allowed to die even after main program ends
    t.start()
    print('\n Thread : {} still running even though main thread is done\n'.format(d.getName()))

"""
Helper Functions - Join threads
join()
wait until thread is finished
By default, join() blocks indefinitely
pass a timeout argument to wait until timeout ends

join() returns None always either when:
1. Thread done
2. Timeout occurs
3. Exception

Need to call isAlive() when join() returns to check which condition was hit
"""

def joinThread():
    # Join, isAlive
    print("\n ******* Testing join ********** \n")
    d2 = threading.Thread(target=dFunc, name='daemon')
    t2 = threading.Thread(target=nFunc, name='non-daemon')
    d3 = threading.Thread(target=dFunc, name='daemon')
    d2.setDaemon(True)
    d3.setDaemon(True)

    d2.start()   # Allowed to die even after main program ends
    t2.start()
    d3.start()

    d2.join(3.0)
    print(d2.isAlive())
    d3.join(7.0)
    print(d3.isAlive())
    t2.join()


"""
enumerate()
Returns list of all alive threads
Includes daemonic threads, dummy threads adn main thread
Excludes terminated threads and threads not started.

"""
def fRand():
    t = threading.current_thread()
    r = random.randint(1,10)
    print("\n Sleeping for {}".format(r))
    time.sleep(r)
    print('Ending thread {}'.format(t.getName()))
    return


def enumerateThread():
    print("\n ******* Testing enumerate ********** \n")
    for i in range(3):
        t = threading.Thread(target=fRand)
        t.setDaemon(True)
        t.start()

    main_thread = threading.current_thread()
    for t in threading.enumerate():
        if t is not main_thread:
            t.join()

"""
Timer()
Subclass of Thread.
Action starts only after timeout/delay specified
Can be canceled before start using cancel()
Start with start()
Cancel with cancel()

"""

def hello():
    print("Hello Timer: {}".format(threading.current_thread().getName()))



def timerObject():
    t = threading.Timer(3.0, hello)
    t.setName('testTimer')
    t.start()

    t1 = threading.Timer(5.0, hello)
    t1.setName('t1')
    t2 = threading.Timer(5,hello)
    t2.setName('t2')

    print("\n Starting timers \n")
    t1.start()
    t2.start()

    print("Sleeping for 2 and checking on t2")
    time.sleep(2)
    t2.isAlive()
    print('Cancelling t2')
    t2.cancel()
    print("Sleeping for 2 and checking on t2")
    t2.isAlive()

    t1.join()
    t2.join()

"""
Event

Communication between threads
set() - Sets flag
clear() - clears flag

wait(timeout) - blocks until flag is true
returns on either flag set, timeout
returns boolean - True when flag is set, False when timeout

isSet() - non-blocking call to check if event is set

"""

def wait_for_event(e):
    print('\n wait_for_event_starting')
    event_is_set = e.wait()
    print('\n Event set: {}'.format(event_is_set))


def wait_for_event_timeout(e, t):
    print('\n wait_for_event_timeout starting')
    event_is_set = e.wait(t)
    print(' event set: {}'.format(event_is_set))
    if event_is_set:
        print('Processing event')
    else:
        print('Event not set but timeout ended. So proceeding with othr things')


def eventObject():
    e = threading.Event()

    t1 = threading.Thread(name='blocking',
                           target=wait_for_event,
                          args=(e,))

    t1.start()

    t2 = threading.Thread(name='non-blocking',
                          target=wait_for_event_timeout,
                          args=(e,2))
    t2.start()

    print('\n Waiting for 3 before setting event')
    time.sleep(3)
    e.set()
    print('Event set \n')

"""
Lock()
Control access to shared resource
Synchronization primitive not owned by any thread when locked

acquire()
when in unlocked state: changes state to locked, returns immediately
when in locked state: blocks until release() called by other thread changes state to unlocked.
                      Resets lock to locked and returns.

release()
Should only be called in locked state
Changes state to unlocked and returns immediately.
RunTimeError is release an unlocked lock.
"""
class Counter(object):
    def __init__(self, start=0):
        self.value = start
        self.lock = threading.Lock()

    def increment(self):
        print('\n Waiting for lock to increment')
        self.lock.acquire()
        try:
            print(' \n Acquired the lock')
            self.value += 1
        finally:
            print(' Releasing lock')
            self.lock.release()


def worker(c):
    for i in range(2):
        r = random.random()
        print(' \n Sleeping for {}'.format(r))
        time.sleep(r)
        c.increment()
    print('\n Done at lock worker')

def lockObject():
    # Increment a counter using lock
    counter = Counter()
    for i in range(2):
        t = threading.Thread(target=worker, args=(counter,))
        t.start()

    print(' \n Waiting for worker threads \n')
    main_thread = threading.current_thread()

    for t in threading.enumerate():
        if t is not main_thread:
            t.join()
    print('\n Counter: {}'.format(counter.value))


# Example 2
def locker2(lock):
    print('\n Starting locker')
    while True:
        lock.acquire()
        try:
            print('Locking for 1')
            time.sleep(1)
        finally:
            print('Releasing finally')
            lock.release()

        time.sleep(1)
    return

def worker2(lock):
    print('\n Starting worker2')
    num_tries, num_acquires = 0, 0
    while num_acquires < 3:
        time.sleep(0.5)
        print(' \n Trying to acquire \n')
        acquired = lock.acquire(0)
        try:
            num_tries += 1
            if acquired:
                num_acquires += 1
            else:
                print('\n Could not acquire on attempt : {}'.format(num_tries))
        finally:
            if acquired:
                lock.release()

    print(' \n Finished attempting {} tries \n'.format(num_tries))

def lockObject2():
    lock = threading.Lock()

    locker = threading.Thread(target=locker2, args=(lock,), name='Locker')
    locker.setDaemon(True)
    locker.start()

    worker = threading.Thread(target=worker2, args=(lock,), name='Worker')
    worker.start()

"""
RLock()
Re-entrant locks
safely called again, meaning no global variables in use
Multiple threads can call this code with no impact to each other

RLock - can be acquired more than once.
In the same thread, can be "re-acquire" ed multiple times.


"""
def RLockObject():
    lock = threading.Lock()
    print('First try: {}'.format(lock.acquire()))
    print('Second try: {}'.format(lock.acquire(0)))

    lock = threading.RLock()
    print('First try: {}'.format(lock.acquire()))
    print('Second try: {}'.format(lock.acquire(0)))


"""
with context

All object with acquire(), release() calls can be used 'with' context
Dont need to explicitly call acquire() and release()

Block Enter: acquire() called
Block exit: release() called

with some_lock:
    # do something...

IS SAME AS

some_lock.acquire()
try:
    # do something...
finally:
    some_lock.release()
"""
def worker_with(lock):
    with lock:
        print('\n Lock acquired via with \n')

def worker_not_with(lock):
    lock.acquire()
    try:
        print('\n Lock acquired directly using acquire \n')
    finally:
        lock.release()

def contextManager():
    lock = threading.Lock()
    w = threading.Thread(target=worker_with, args=(lock,), name='UsingWith')
    nw = threading.Thread(target=worker_not_with, args=(lock,), name='NotUsingWith')

    w.start()
    nw.start()


"""
Condition

Synchronizing threads - condition object
Always associated with a lock
Lock can be passed in Or will have a default lock
When several CV need to share same lock, need to pass a lock
Can also be used as 'with' context manager

wait()
Consumer waits on CV being set
Releases the lock and blocks until another thread calls notify() or notifyAll()


notify()
notifyALL()
Producer calls this to wake up waiting consumer threads
These dont release the lock immediately. Need to finish the thread calling notify

Producer-Consumer Psuedocode
with cv:
    while not item_available:
        cv.wait()
    get_available_item()

with cv:
    make_item_available()
    cv.notify()


"""
def consumer(condition):
    print('\n Consumer thread started \n ')
    with condition:
        condition.wait()
        print('Consumer consumed the resource')

def producer(condition):
    print('\n Producer thread started \n')
    with condition:
        print('\n Resource made available\n')
        condition.notifyAll()

def conditionObject():
    condition = threading.Condition()
    cs1 = threading.Thread(target=consumer, args=(condition,), name='consumer1')
    cs2 = threading.Thread(target=consumer, args=(condition,), name='consumer2')
    p = threading.Thread(target=producer, args=(condition,), name='producer')

    cs1.start()
    time.sleep(2)
    cs2.start()
    time.sleep(2)
    p.start()


if __name__ == "__main__":

    createThread()
    daemonThread()
    joinThread()
    enumerateThread()
    timerObject()
    eventObject()
    lockObject()
    lockObject2()
    RLockObject()
    contextManager()
    conditionObject()














