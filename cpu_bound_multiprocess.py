import os
import threading
import time

from concurrent.futures import ProcessPoolExecutor

def calculate(n):
    print(f"Process ID: {os.getpid()} | Thread ID: {threading.get_ident()} | number: {n}")

    sum = 0

    for i in range(n):
        for j in range(n):
            for k in range(n):
                sum += i * j * k

    return sum

def main(numbers):
    with ProcessPoolExecutor(max_workers = 10) as process:
        result = list(process.map(calculate, numbers))
        print(result)

if __name__ == "__main__":
    start = time.time()
    main([300] * 10)
    print(f"elapsed-time: {time.time() - start}")