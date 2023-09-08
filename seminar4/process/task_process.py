import requests
import multiprocessing
import time


def download(url: str):
    start_ = time.time()
    response = requests.get(url)
    if response.status_code == 200:
        filename = url.split('/')[-1]
        with open(f'{filename}', 'wb') as file:
            file.write(response.content)
        print(f'Download {filename}: {(time.time() - start_):.3f} second')


def multiprocessing_(urls_: list):
    processes = []
    for url in urls_:
        process = multiprocessing.Process(target=download, args=(url,))
        processes.append(process)
        process.start()

    for p in processes:
        p.join()


if __name__ == '__main__':
    urls = ['https://random.dog/c5a493db-526c-4563-9e97-f12b36d592d6.jpg',
            'https://random.dog/c22c077e-a009-486f-834c-a19edcc36a17.jpg',
            ' https://random.dog/f3ab5880-f3fd-4bff-9f5a-934c02c9fbfc.jpg',
            'https://random.dog/ed6c2ace-d58e-41d5-bc89-96846b110f92.jpg',
            ' https://random.dog/5d2a03a7-4f5b-4ace-8408-277af17f6d4f.jpg',
            'https://random.dog/d16849b9-135d-4550-a2e5-184203284a62.gif',
            ]
    start = time.time()
    multiprocessing_(urls)
    print(f'The program has ended: {(time.time() - start):.3f} second')