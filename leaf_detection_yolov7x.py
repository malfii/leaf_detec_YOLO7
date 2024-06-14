# -*- coding: utf-8 -*-
"""leaf_detection_YOLOv7x.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WhOjN9mHWflgMeVK9U04hDcPQhOLRAeA

<h1  align=center><font  size = 5>Leaf Detection using YOLOv7x</font></h1>

<img  src="https://i0.wp.com/www.bigtoolbox.com/wp-content/uploads/2019/09/weeds-in-a-vegtable-garden.jpg?resize=1080%2C675&ssl=1"  height=500  width=1000  alt="https://www.bigtoolbox.com/weeds-in-your-vegetable-garden/">  

<small>Picture Source: <a  href="https://www.bigtoolbox.com/weeds-in-your-vegetable-garden/">bigtoolbox</a></small>  

<br>

## Summary

This project utilizes the YOLOv7 architecture to develop an accurate and efficient leaf object detection model for agricultural applications. By leveraging a curated dataset of annotated images, the model can identify and classify leaves, aiding in crop management, disease detection, and weed control. The project focuses on robustness, efficiency, and interpretability, aiming to empower farmers and researchers with a reliable tool for informed decision-making. Through optimization and evaluation, the model demonstrates its potential to enhance crop productivity and sustainability.

<br>

## Introduction

Detecting and classifying objects within images is a fundamental challenge in the field of computer vision, and it finds numerous practical applications across various domains. In particular, accurate and efficient detection of specific objects, such as leaves, is crucial in agricultural settings for tasks like crop management, disease identification, and weed control.

<br>

In this project, we present a leaf object detection model based on the state-of-the-art **You Only Look Once** version 7 (YOLOv7) architecture. *YOLOv7* is a deep learning framework that achieves real-time object detection with impressive accuracy. By harnessing the power of convolutional neural networks and advanced computer vision techniques, our model aims to provide an effective and scalable solution for leaf detection in complex agricultural environments. To train and evaluate our *YOLOv7* leaf object detection model, we leverage a comprehensive dataset specifically curated for this purpose. The dataset contains diverse images of crops and weeds, annotated with bounding boxes that precisely delineate leaf objects. This rich dataset empowers our model to learn intricate patterns and generalizable representations, enabling it to accurately detect and classify leaves under varying conditions.

<br>

Throughout the development of our leaf object detection model, we adhere to the principles of robustness, efficiency, and interpretability. We optimize our model's architecture and hyperparameters to strike a balance between accuracy and computational efficiency, ensuring real-time performance in practical scenarios. Additionally, we focus on interpretable outputs, providing insights into the detected leaf objects and their corresponding bounding boxes.

<br>

Our ultimate goal is to empower farmers, researchers, and agricultural professionals with a reliable tool for leaf object detection that can facilitate informed decision-making and enhance crop management practices. By accurately identifying and analyzing leaves, we enable precise monitoring, early detection of diseases, and targeted interventions, ultimately leading to improved yields and sustainable agricultural practices.

<br>

## YOLO

*YOLO (You Only Look Once)* is an object detection algorithm that was introduced in 2015 by **Joseph Redmon** et al. It revolutionized the field of computer vision by providing a real-time object detection solution with impressive accuracy.



*   **Single Pass Detection**: YOLO takes a different approach compared to traditional object detection methods that use region proposal techniques. Instead of dividing the image into regions and examining each region separately, YOLO performs detection in a single pass. It divides the input image into a grid and predicts bounding boxes and class probabilities for each grid cell.

*   **Grid-based Prediction**: YOLO divides the input image into a fixed-size grid, typically, say, 7x7 or 13x13. Each grid cell is responsible for predicting objects that fall within it. For each grid cell, YOLO predicts multiple bounding boxes (each associated with a confidence score) and class probabilities.

*   **Anchor Boxes**: To handle objects of different sizes and aspect ratios, YOLO uses anchor boxes. These anchor boxes are pre-defined boxes of different shapes and sizes. Each anchor box is associated with a specific grid cell. The network predicts offsets and dimensions for anchor boxes relative to the grid cell, along with the confidence scores and class probabilities.

*   **Training**: YOLO is trained using a combination of labeled bounding box annotations and classification labels. The training process involves optimizing the network to minimize the localization loss (related to the accuracy of bounding box predictions) and the classification loss (related to the accuracy of class predictions).

*   **Speed and Accuracy Trade-off**: YOLO achieves real-time object detection by sacrificing some localization accuracy compared to slower methods like Faster R-CNN. However, it still achieves competitive accuracy while providing significantly faster inference speeds, making it well-suited for real-time applications.

<br>

Since its introduction, YOLO has undergone several improvements and variations. Different versions such as YOLOv2, YOLOv3, and YOLOv4 have been developed, each introducing enhancements in terms of accuracy, speed, and additional features.

It's important to note that this is a high-level overview of YOLO, and the algorithm has many technical details and variations. For a more in-depth understanding, it's recommended to refer to the original YOLO papers and related resources.

<br>

## Keywords  

<ul>
 <li>YOLOv7</li>
 <li>Leaf object detection</li>
 <li>Computer vision</li>
 <li>Agricultural applications</li>
 <li>Deep learning</li>
</ul>

<br>

<h1>Objective for this Notebook</h1>

<div class="alert alert-block alert-info" style="margin-top: 20px">
  <ol>
      <li><a href="">Importing Libraries</a></li>
      <li><a href="">Data Preprocessing</a></li>  
      <li><a href="">Clone YOLOv7 and Train the Model</a></li>
      <li><a href="">Uplad Test Images and Make Predictions</a></li>
      <li><a href="">Save the Results</a></li>
  </ol>
</div>
<br>

Feel free to modify and customize this introduction to align with your specific project objectives and goals. Good luck with your *YOLOv7* leaf object detection model!

Make sure your runtime is **GPU** (_not_ CPU or TPU). And if it is an option, make sure you are using _Python 3_. You can select these settings by going to `Runtime -> Change runtime type -> Select the above mentioned settings and then press SAVE`.

## Importing Libraries
"""

import os
import random
import shutil

"""## Data Preprocessing

### Dataset
The dataset used in this project is the Crop and Weed Detection Data with Bounding Boxes from Kaggle, which can be accessed [here](https://www.kaggle.com/datasets/ravirajsinh45/crop-and-weed-detection-data-with-bounding-boxes).

<br>

###  Description
[The Crop and Weed Detection dataset](https://www.kaggle.com/datasets/ravirajsinh45/crop-and-weed-detection-data-with-bounding-boxes) is a comprehensive collection of images specifically curated for leaf object detection in agricultural environments. It consists of a diverse range of images showcasing crops and weeds in various growth stages and conditions.

Each image in the dataset is annotated with bounding boxes that precisely delineate the leaf objects, providing ground truth information for training and evaluation. The annotations enable the model to learn intricate patterns and accurately identify and classify leaves within the images.

<br>

### Contents
The dataset includes the following components:

1. Images: A collection of high-resolution images depicting crops and weeds in different agricultural settings.

2. Annotations: XML files containing the bounding box coordinates and class labels for each leaf object present in the corresponding image.

<br>

### Preprocessing
As part of the data preprocessing pipeline, the images were resized and standardized to a consistent resolution suitable for training the YOLOv7 leaf object detection model. The annotations were parsed and converted into a compatible format for training and evaluation purposes.

<br>

### Usage
To utilize the Crop and Weed Detection dataset in this project, please follow these steps:

1. Download the dataset from the provided Kaggle link.

2. Extract the dataset files to a local directory.

3. Ensure that the dataset is properly organized, with images and corresponding annotation files placed in the appropriate folders.

4. Follow the installation and setup instructions in the project's README file to integrate the dataset into the training and evaluation pipeline.
"""

# Commented out IPython magic to ensure Python compatibility.
# %cd /content/

!unzip -q /content/archive.zip

# !rm -rf /content/agri_data
# !rm -rf /content/classes.txt
# !rm -rf /content/archive.zip

folder_path = "/content/agri_data/data"

"""Create directories for train and val."""

train_dir = os.path.join(folder_path, "train")
val_dir = os.path.join(folder_path, "val")
os.makedirs(train_dir, exist_ok=True)
os.makedirs(val_dir, exist_ok=True)

"""Create images and labels directories within train and val folders."""

train_images_dir = os.path.join(train_dir, "images")
train_labels_dir = os.path.join(train_dir, "labels")
val_images_dir = os.path.join(val_dir, "images")
val_labels_dir = os.path.join(val_dir, "labels")
os.makedirs(train_images_dir, exist_ok=True)
os.makedirs(train_labels_dir, exist_ok=True)
os.makedirs(val_images_dir, exist_ok=True)
os.makedirs(val_labels_dir, exist_ok=True)

"""Get a list of all image files in the folder."""

image_files = [f for f in os.listdir(folder_path) if f.endswith(".jpeg")]

num_val_files = int(len(image_files) * 0.2)
val_files = random.sample(image_files, num_val_files)

for val_file in val_files:
    image_file = os.path.join(folder_path, val_file)
    annotation_file = os.path.join(folder_path, val_file.replace(".jpeg", ".txt"))
    try:
        shutil.move(image_file, val_images_dir)
        shutil.move(annotation_file, val_labels_dir)
    except FileNotFoundError:
        print(f"File not found: {val_file}")

for image_file in image_files:
    annotation_file = os.path.join(folder_path, image_file.replace(".jpeg", ".txt"))
    try:
        shutil.move(os.path.join(folder_path, image_file), train_images_dir)
        shutil.move(annotation_file, train_labels_dir)
    except FileNotFoundError:
        print(f"File not found: {image_file}")

print("Data splitting completed!")

train_images_dir = "/content/agri_data/data/train/images"
val_images_dir = "/content/agri_data/data/val/images"

train_image_count = len([f for f in os.listdir(train_images_dir) if f.endswith(".jpeg")])
val_image_count = len([f for f in os.listdir(val_images_dir) if f.endswith(".jpeg")])

print(f"Number of images in train folder: {train_image_count}")
print(f"Number of images in val folder: {val_image_count}")

train_labels_dir = "/content/agri_data/data/train/labels"
val_labels_dir = "/content/agri_data/data/val/labels"

train_txt_count = len([f for f in os.listdir(train_labels_dir) if f.endswith(".txt")])
val_txt_count = len([f for f in os.listdir(val_labels_dir) if f.endswith(".txt")])

print(f"Number of TXT files in train labels folder: {train_txt_count}")
print(f"Number of TXT files in val labels folder: {val_txt_count}")

"""## Clone YOLOv7 and Train the Model"""

# Commented out IPython magic to ensure Python compatibility.
# %cd /content/

!git clone https://github.com/WongKinYiu/yolov7.git

# Commented out IPython magic to ensure Python compatibility.
# %cd /content/yolov7

"""You can change model from [WongKinYiu GitHub](https://github.com/WongKinYiu/yolov7) page."""

!wget https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7x.pt

"""Before training, you neet to go to `yolov7/data/coco.yaml` and define your number of class, class names and train-val paths like that:

```
# COCO 2017 dataset http://cocodataset.org

train: ../agri_data/data/train/images
val: ../agri_data/data/val/images

# number of classes
nc: 2

# class names
names: ['crop', 'weed']
```

*   `!python train.py`: This is the command to execute the Python script *train.py* for training the YOLOv7 model.

*  `--device 0`: This parameter specifies the device (GPU) to be used for training. In this case, it is set to device 0, indicating the first GPU device.

*  `--batch-size 16`: This parameter determines the number of images in each batch during training. A batch size of *16* means that the model will process 16 images at a time before updating the weights.

*  `--data data/coco.yaml`: This parameter specifies the path to the YAML file containing the dataset configuration. In this case, **the *coco.yaml* file is used, which provides information about the dataset, including the classes and paths to the training and validation data.**

*  `--img 640 640`: This parameter sets the input image size for the model. The YOLOv7 model requires square input images, and here the dimensions are set to 640x640 pixels.

*  `--epochs 64`: This parameter defines the number of epochs, which represents the number of times the entire training dataset will be passed through the model during training. In this case, the model will be trained for **64 epochs**.

*  `--weights yolov7x.pt`: This parameter specifies the initial weights of the model. The *yolov7x.pt* file contains the pre-trained weights for the *YOLOv7* model, which will be used as the starting point for training.

*  `--hyp data/hyp.scratch.p5.yaml`: This parameter indicates the path to the YAML file containing hyperparameters for training. Hyperparameters include learning rate, weight decay, and other settings that affect the training process. Here, the *hyp.scratch.p5.yaml* file is used.

*  `--name yolov7x`: This parameter sets the name of the model during training. The name can be customized, and in this case, it is set to *yolov7x*.

If you are using GPU, try this:
"""

!python train.py --device 0 --batch-size 16 --data data/coco.yaml --img 640 640 --epochs 64 --weights yolov7x.pt --hyp data/hyp.scratch.p5.yaml --name yolov7x

"""If you are using CPU, try this:"""

# !python train.py --device cpu --batch-size 16 --data data/coco.yaml --img 640 640 --epochs 64 --weights yolov7x.pt --hyp data/hyp.scratch.p5.yaml --name yolov7x

"""## Uplad Test Images and Make Predictions"""

# Commented out IPython magic to ensure Python compatibility.
# %cd /content/

!mkdir test

# Commented out IPython magic to ensure Python compatibility.
# %cd /content/test

from google.colab import files
uploaded = files.upload()

# Commented out IPython magic to ensure Python compatibility.
# %cd /content/yolov7

"""Upload your images into test folder."""

!python detect.py --weights runs/train/yolov7x/weights/best.pt --conf 0.50 --img-size 640 --source /content/test/agri_0_14.jpeg

"""In addition, you can upload video and make predictions."""

# !python detect.py --weights yolov7.pt --conf 0.25 --img-size 640 --source test/video_name.mp4

"""## Save the Results"""

from google.colab import drive
files.download('runs/train/yolov7x/weights/best.pt')
files.download('/content/yolov7/runs/train/yolov7x/F1_curve.png')
files.download('/content/yolov7/runs/train/yolov7x/PR_curve.png')
files.download('/content/yolov7/runs/train/yolov7x/confusion_matrix.png')
files.download('/content/yolov7/runs/train/yolov7x/hyp.yaml')
files.download('/content/yolov7/runs/train/yolov7x/opt.yaml')
files.download('/content/yolov7/runs/train/yolov7x/results.png')
files.download('/content/yolov7/runs/train/yolov7x/results.txt')
files.download('/content/yolov7/runs/train/yolov7x/test_batch0_labels.jpg')
files.download('/content/yolov7/runs/train/yolov7x/test_batch0_pred.jpg')
files.download('/content/yolov7/runs/train/yolov7x/test_batch1_labels.jpg')
files.download('/content/yolov7/runs/train/yolov7x/test_batch1_pred.jpg')
files.download('/content/yolov7/runs/train/yolov7x/test_batch2_labels.jpg')
files.download('/content/yolov7/runs/train/yolov7x/test_batch2_pred.jpg')
files.download('/content/yolov7/runs/train/yolov7x/train_batch0.jpg')
files.download('/content/yolov7/runs/train/yolov7x/train_batch1.jpg')
files.download('/content/yolov7/runs/train/yolov7x/train_batch2.jpg')
files.download('/content/yolov7/runs/train/yolov7x/train_batch3.jpg')
files.download('/content/yolov7/runs/train/yolov7x/train_batch4.jpg')
files.download('/content/yolov7/runs/train/yolov7x/train_batch5.jpg')
files.download('/content/yolov7/runs/train/yolov7x/train_batch6.jpg')
files.download('/content/yolov7/runs/train/yolov7x/train_batch7.jpg')
files.download('/content/yolov7/runs/train/yolov7x/train_batch8.jpg')
files.download('/content/yolov7/runs/train/yolov7x/train_batch9.jpg')
files.download('/content/yolov7/runs/detect/exp/agri_0_14.jpeg')
files.download('/content/yolov7/data/coco.yaml')

"""<h1>Contact Me</h1>
<p>If you have something to say to me please contact me:</p>

<ul>
  <li>Twitter: <a href="https://twitter.com/Doguilmak">Doguilmak</a></li>
  <li>Mail address: doguilmak@gmail.com</li>
</ul>
"""

from datetime import datetime
print(f"Changes have been made to the project on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")