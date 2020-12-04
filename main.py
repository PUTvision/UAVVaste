import csv
import requests
from pycocotools.coco import COCO
from tqdm import tqdm
import os

anns_path = './annotations/annotations.json'
dest_path = './images/'



def try_download(source: str, dest: str, name: str):
    r = requests.get(source, allow_redirects=True)
    if r.ok:
        with open(f'{dest}{name}', 'wb') as f:
            f.write(r.content)
    else:
        print(f'Failed to download the file: {name}')
        

def download(img: dict, dest_path: str):
    if img['flickr_url'] is not None and not os.path.isfile(f'{dest_path}{img["file_name"]}'):
        try_download(img['flickr_url'], dest_path, img['file_name'])

def main():
    dataset = COCO(anns_path)

    for img in tqdm(dataset.imgs.values()):
        download(img, dest_path)


if __name__ == '__main__':
    main()