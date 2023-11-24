import torch
from pathlib import Path
from PIL import Image


# Загрузите предварительно обученную модель
# model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

model = torch.hub.load('ultralytics/yolov5:master', 'yolov5s', pretrained=True)

image_path = r'C:\Users\79249\PycharmProjects\pythonProject2\Datasets\data\00003_b.jpg'

img = Image.open(image_path)

results = model(img)
print(dir(results))

results.show()

# results.save(Path('output'))
print(results.names)
print(results.pred)
print(results.t)
print(results.s)

# print(results.xyxy[0][:, :4])
# print(results.xyxy[0][:, 4])