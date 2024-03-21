import threading

class SuspendResumeThread(threading.Thread):
    
    def __init__(self, iterations):
        threading.Thread.__init__(self)
        self.suspended = False
        self.event = threading.Event()
        self.iterations = iterations
    
    def run(self):
        print("Thread is running...")
        for i in range(self.iterations):
            if self.suspended:
                # Thread is suspended, wait until resumed
                self.event.wait()
                self.event.clear()
            else:
                # Thread is running
                print("thread is running:", i)
                # Do some work here
    
    def suspend(self):
        self.suspended = True
    
    def resume(self):
        self.suspended = False
        self.event.set()
        
# Create a new thread with 6 iterations
thread = SuspendResumeThread(int(input("enter a number :")))
thread.start()

# Suspend and resume the thread with a predefined number of iterations
thread.suspend()  # Suspend the thread
thread.resume()   # Resume the thread
thread.suspend()  # Suspend the thread
thread.resume()   # Resume the thread
thread.suspend()  # Suspend the thread
thread.resume()   # Resume the thread


