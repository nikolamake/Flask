import asyncio
import aiohttp
import aiofiles
import time


async def download(url_: str):
    start_ = time.time()
    async with aiohttp.ClientSession() as session:
        async with session.get(url_) as response:
            if response.status == 200:
                filename = url_.split('/')[-1]
                content = await response.read()
                async with aiofiles.open(f'{filename}', 'wb') as file:
                    await file.write(content)

                print(f'Download {(time.time() - start_):.3f} second')


async def async_(urls_: list):
    tasks = []
    for url in urls_:
        task = asyncio.create_task(download(url))
        tasks.append(task)
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    urls = ['https://random.dog/c5a493db-526c-4563-9e97-f12b36d592d6.jpg',
            'https://random.dog/c22c077e-a009-486f-834c-a19edcc36a17.jpg',
            ' https://random.dog/f3ab5880-f3fd-4bff-9f5a-934c02c9fbfc.jpg',
            'https://random.dog/ed6c2ace-d58e-41d5-bc89-96846b110f92.jpg',
            ' https://random.dog/5d2a03a7-4f5b-4ace-8408-277af17f6d4f.jpg',
            'https://random.dog/d16849b9-135d-4550-a2e5-184203284a62.gif',
            ]
    start = time.time()
    asyncio.run(async_(urls))
    print(f'The program has ended: {(time.time() - start):.3f} second')