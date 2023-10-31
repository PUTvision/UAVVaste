from pycocotools.coco import COCO
from pathlib import Path
import json
import cv2
import numpy as np
from tqdm import tqdm



def convert_json_to_yolo_mask(annotation_path: str, images_dir_path: str, dest_path: str, train_val_test: dict):
    keys = train_val_test.keys()
    dataset = COCO(annotation_path)
    
    for img_id in tqdm(dataset.imgs):
        img_info = dataset.imgs[img_id]
        img_name = img_info['file_name']
        img_path = Path(images_dir_path) / img_name
        img = cv2.imread(str(img_path))
        
        img_h, img_w, _ = img.shape
        
        ann_ids = dataset.getAnnIds(imgIds=img_id)
        anns = dataset.loadAnns(ann_ids)
        
        if img_name in train_val_test['train']:
            dest_dir = Path(dest_path) / 'train'
        elif img_name in train_val_test['val']:
            dest_dir = Path(dest_path) / 'val'
        elif img_name in train_val_test['test']:
            dest_dir = Path(dest_path) / 'test'
            
        dest_dir.mkdir(parents=True, exist_ok=True)
        
        cv2.imwrite(str(dest_dir / img_name), img)
        
        with open(str(dest_dir / img_name).replace('.jpg', '.txt').replace('.JPG', '.txt').replace('.PNG', '.txt'), 'w') as f:
            for ann in anns:
                row = '0'
                
                for i in range(0, len(ann['segmentation'][0]), 2):
                    row += f' {ann["segmentation"][0][i] / img_w} {ann["segmentation"][0][i+1] / img_h}'
                    
                row += '\n'
                
                f.write(row)       
        
    
if __name__ == '__main__':
    annotation_path = './annotations/annotations.json'
    images_dir_path = './images/'
    
    dest_path = './yolo_masks/'
    
    with open('./annotations/train_val_test_distribution_file.json', 'r') as f:
        train_val_test = json.load(f)
    
    convert_json_to_yolo_mask(annotation_path, images_dir_path, dest_path, train_val_test)
