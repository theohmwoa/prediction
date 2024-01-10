import numpy as np
import os
from urllib.request import urlretrieve
from tqdm import tqdm
from sklearn.model_selection import train_test_split
from classes import classes

os.makedirs('quickdraw_data', exist_ok=True)

print(classes)


base_url = 'https://storage.googleapis.com/quickdraw_dataset/full/numpy_bitmap/'
for c in classes:
    cls_url = c.replace('_', '%20')
    path = f'quickdraw_data/{c}.npy'
    print(f'Downloading {c}', end='...')
    try:
        urlretrieve(f'{base_url}{cls_url}.npy', path)
    except Exception as e:
        print(f"An error occurred while downloading {cls_url}: {e}")

    print('Done!')


def load_data(classes, root='quickdraw_data'):
    x = np.empty([0, 784])
    y = np.empty([0])

    for idx, cls in enumerate(classes):
        cls_file = f'{root}/{cls}.npy'
        cls_data = np.load(cls_file)
        cls_data = cls_data.astype('float32') / 255.0
        cls_labels = np.full(cls_data.shape[0], idx)

        x = np.concatenate((x, cls_data), axis=0)
        y = np.concatenate((y, cls_labels), axis=0)

        print(f'{cls} data loaded')

    return x, y


x, y = load_data(classes)

x = x.reshape(x.shape[0], 28, 28, 1)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

np.save('dataset/x_train.npy', x_train)
np.save('dataset/x_test.npy', x_test)
np.save('dataset/y_train.npy', y_train)
np.save('dataset/y_test.npy', y_test)

