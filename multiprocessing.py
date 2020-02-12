import random
from multiprocessing import Queue, Process


def rand_num():
    num = random.random()
    print num


if __name__ == "__main__":
    queue = Queue()

    process = [Process(target=rand_num, args=()) for x in range(4)]

    for p in process:
        p.start()

    for p in process:
        p.join()

