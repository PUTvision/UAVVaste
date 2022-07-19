<p align="center">
    <img src="https://uavvaste.github.io/images/trash.png" />
</p>

# UAVVaste dataset

The UAVVaste dataset consists to date of 772 images and 3718 annotations. The main motivation for the creation of the dataset was the lack of domain-specific data. Therefore, this image set is recommended for object detection evaluation benchmarking but also for developing solutions related to UAVs, remote sensing, or even environmental cleaning. The dataset is made publicly available and will be expanded.

<center>

| **Date**      | **Images count**  | **Annotations count** |
|---------------|:-----------------:|:---------------------:|
| 14.11.2020    |      772          |        3718           |

</center>

The dataset is a part of the research paper: [,,Autonomous, Onboard Vision-Based Trash and Litter Detection in Low Altitude Aerial Images Collected by an Unmanned Aerial Vehicle'' Marek Kraft, Mateusz Piechocki, Bartosz Ptak and Krzysztof Walas - MDPI Remote Sensing](https://www.mdpi.com/2072-4292/13/5/965).

<p align="center">
    <img src="https://github.com/UAVVaste/UAVVaste.github.io/blob/master/50699048692_ea5f052204_o.gif?raw=true" />
</p>

# Usage

## Requirements

``` python
pip3 install -r requirements.txt
```

## Download

``` python
python3 main.py
```

# Contribute

If you want to contribute to the UAVVaste dataset, please contact us via email [uavvaste@gmail.com](uavvaste@gmail.com). We will be grateful for all images taken from the UAV with litter annotations in the COCO format (bounding boxes and segmentation masks).

# Citation

```
@Article{rs13050965,
AUTHOR = {Kraft, Marek and Piechocki, Mateusz and Ptak, Bartosz and Walas, Krzysztof},
TITLE = {Autonomous, Onboard Vision-Based Trash and Litter Detection in Low Altitude Aerial Images Collected by an Unmanned Aerial Vehicle},
JOURNAL = {Remote Sensing},
VOLUME = {13},
YEAR = {2021},
NUMBER = {5},
ARTICLE-NUMBER = {965},
URL = {https://www.mdpi.com/2072-4292/13/5/965},
ISSN = {2072-4292},
DOI = {10.3390/rs13050965}
}
```
