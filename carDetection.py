import torch


model = torch.hub.load("ultralytics/yolov5", "yolov5s")

img = "Datasets/dataTenOutput/00003.jpg"

results = model(img)

print(results)
results.print()