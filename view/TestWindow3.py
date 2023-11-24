import torch
import os
import csv
import cv2


def find_car(input_dir, output_cars ='output.csv'):
    input_dir = r'C:\Users\79249\PycharmProjects\pythonProject2\Datasets\datatest'
    cars, imgs = ['car', 'truck', 'bus'], []

    for file_name in os.listdir(input_dir):
        imgs.append(cv2.imread(os.path.join(input_dir, file_name)))

    model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
    results = model(imgs)

    output_folder = 'Datasets/images'
    os.makedirs(output_folder, exist_ok=True)

    with open(output_cars, 'w', newline='') as f:
        writer = csv.writer(f)

        for i, file_name in enumerate(os.listdir(input_dir)):
            res = [n in results.pandas().xyxy[i]['name'].unique() for n in cars]
            writer.writerow([file_name, bool(sum(res))])
            if any(res):
                output_path = os.path.join(output_folder, file_name)
                cv2.imwrite(output_path, imgs[i])
                print(f"Фото с машиной сохранено: {output_path}")



find_car('datatest')