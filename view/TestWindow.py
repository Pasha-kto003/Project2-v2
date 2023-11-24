import torch
from pathlib import Path
from PIL import Image

# Загрузка предварительно обученной модели YOLOv5
model = torch.hub.load('ultralytics/yolov5:master', 'yolov5s', pretrained=True)

# Путь к вашему изображению
image_path = 'C:/Users/79249/PycharmProjects/pythonProject2/Datasets/data/00032_g.jpg'


img = Image.open(image_path)

results = model(img)


results.show()


results.save(Path('output'))

print(results.xyxy[0][:, :4])
print(results.xyxy[0][:, 4])