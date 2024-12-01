"""
동기 실행 코드 - https://techblog-history-younghunjo1.tistory.com/570
"""

import requests
import time
import os
import threading

def get_web_page(url: str):
    print(f"Process ID: {os.getpid()} | Thread ID: {threading.get_ident()} | request to {url}")
    result = requests.get(url);
    print("============================")

def main():
    urls = [
        "https://www.naver.com",
        "https://www.google.com"
    ] * 30

    for url in urls:
        get_web_page(url)


if __name__ == '__main__':
    start = time.time()
    main()
    print(f"Total request time is {time.time() - start}")