import asyncio
import threading
import os
import time

file_directory_path = "/home" 
max_file_count = 12

# 1. async.io 라이브러리를 사용하는 경우
async def use_async_io():
    start = time.time()
    await asyncio.wait([
        asyncio.create_task(async_sort_files(file_directory_path, max_file_count)),
        asyncio.create_task(async_sort_files(file_directory_path, max_file_count)),
    ])
    print(f"multi thread time is {time.time() - start}")

# 2. 직접 스레드를 만들어 그 안에서 실행하는 경우
def use_thread():
    start = time.time()
    file_thread = threading.Thread(target=sort_files, args=(file_directory_path, max_file_count))
    url_thread = threading.Thread(target=sort_files, args=(file_directory_path, max_file_count))

    file_thread.start()
    url_thread.start()
    file_thread.join()
    url_thread.join()
    print(f"coroutine time is {time.time() - start}")

def sort_files(files='', max_file_count=0):
    #time.sleep(1)  # simulate some delay
    return list(
        sorted(
            os.listdir(files),
            key=lambda x: os.stat(os.path.join(files, x)).st_mtime
        )
    )[:max_file_count]

async def async_sort_files(files='', max_file_count=0):
    #await asyncio.sleep(1)  # simulate some delay
    return list(
        sorted(
            os.listdir(files),
            key=lambda x: os.stat(os.path.join(files, x)).st_mtime
        )
    )[:max_file_count]

async def main():
    await use_async_io()
    use_thread()

if __name__ == '__main__':
    asyncio.run(main())
