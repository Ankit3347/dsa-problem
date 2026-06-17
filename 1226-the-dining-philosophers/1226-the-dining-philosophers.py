from threading import Semaphore, Lock
from typing import Callable

class DiningPhilosophers:

    def __init__(self):
        self.forks = [Lock() for _ in range(5)]
        self.semaphore = Semaphore(4)

    def wantsToEat(self,
                   philosopher: int,
                   pickLeftFork: Callable[[], None],
                   pickRightFork: Callable[[], None],
                   eat: Callable[[], None],
                   putLeftFork: Callable[[], None],
                   putRightFork: Callable[[], None]) -> None:

        left = philosopher
        right = (philosopher + 1) % 5

        self.semaphore.acquire()

        with self.forks[left]:
            with self.forks[right]:
                pickLeftFork()
                pickRightFork()

                eat()

                putRightFork()
                putLeftFork()

        self.semaphore.release()