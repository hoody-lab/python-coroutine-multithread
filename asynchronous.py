"""
비동기 실행 코드 - https://techblog-history-younghunjo1.tistory.com/570
Total request time is 0.48593878746032715
"""

import aiohttp    # request 대신 aiohttp 라이브러리 사용
import time
import os
import threading
import asyncio

async def get_web_page(session, url: str):
    print(f"Process ID: {os.getpid()} | Thread ID: {threading.get_ident()} | request to {url}")
    async with session.get(url) as response:
        result = await response.text()
    print("============================")

async def main():
    urls = [
        "https://www.naver.com",
        "https://www.google.com"
    ] * 30

    async with aiohttp.ClientSession() as session:
        await asyncio.gather(*[get_web_page(session, url) for url in urls])

if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    print(f"Total request time is {time.time() - start}")