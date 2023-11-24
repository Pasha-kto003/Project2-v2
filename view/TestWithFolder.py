import os
import torch
from pathlib import Path
from PIL import Image

folder_path = 'C:/Users/79249/PycharmProjects/pythonProject2/Datasets/datatest/'

model_path = 'path/to/your/yolov5/model.pt'

model = torch.hub.load('ultralytics/yolov5:master', 'yolov5s', pretrained=True)

image_files = [f for f in os.listdir(folder_path) if f.endswith(('.jpg', '.jpeg', '.png'))]

for image_file in image_files:
    image_path = os.path.join(folder_path, image_file)

    img = Image.open(image_path)

    results = model(img)
    print(results.names)
    results.show()

    output_path = os.path.join('output', image_file)
    results.save(Path(output_path))