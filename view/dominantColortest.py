import cv2
import numpy as np
from sklearn.cluster import KMeans

def extract_colors(image_path, num_colors=3):
    image = cv2.imread(image_path)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    pixels = image_rgb.reshape((-1, 3))
    kmeans = KMeans(n_clusters=num_colors)
    kmeans.fit(pixels)
    dominant_colors = kmeans.cluster_centers_.astype(int)
    return dominant_colors


image_path = r'C:\Users\79249\PycharmProjects\pythonProject2\view\Datasets\images\00018_b.jpg'
dominant_colors = extract_colors(image_path)
print("Dominant Colors:")
for color in dominant_colors:
    print(f"RGB: {color}")