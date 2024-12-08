"""
동기 실행 코드 - https://techblog-history-younghunjo1.tistory.com/570
elapsed-time: 24.02848529815674
"""

import os
import threading
import time

def calculate(n):
    print(f"Process ID: {os.getpid()} | Thread ID: {threading.get_ident()} | number: {n}")

    sum = 0

    for i in range(n):
        for j in range(n):
            for k in range(n):
                sum += i * j * k

    return sum

def main(numbers):
    result = [calculate(number) for number in numbers]
    print(result)

if __name__ == "__main__":
    start = time.time()
    main([300] * 10)
    print(f"elapsed-time: {time.time() - start}")