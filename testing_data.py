import numpy as np
import requests
from PIL import Image
import io
from classes import classes


def download_and_process_quickdraw_data(classes, num_samples=100):
    base_url = "https://storage.googleapis.com/quickdraw_dataset/full/numpy_bitmap/"
    for cls in classes:
        url = f"{base_url}{cls}.npy"
        response = requests.get(url)
        response.raise_for_status()

        data = np.load(io.BytesIO(response.content))
        data = data[:num_samples]
        data = data.reshape((num_samples, 28, 28))

        for idx, drawing in enumerate(data):
            img = Image.fromarray(drawing)
            img.save(f"{cls}_{idx}.png")


download_and_process_quickdraw_data(classes, num_samples=10)
