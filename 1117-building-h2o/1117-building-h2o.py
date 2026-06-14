from threading import Semaphore, Barrier

class H2O:
    def __init__(self):
        self.h_sem = Semaphore(2)   # allow 2 H
        self.o_sem = Semaphore(1)   # allow 1 O
        self.barrier = Barrier(3)   # wait for 3 threads

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        self.h_sem.acquire()

        self.barrier.wait()

        releaseHydrogen()

        self.h_sem.release()

    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        self.o_sem.acquire()

        self.barrier.wait()

        releaseOxygen()

        self.o_sem.release()