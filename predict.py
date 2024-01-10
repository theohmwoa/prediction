import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from classes import classes

model = tf.keras.models.load_model('quickdraw_model.h5')

def predict_image(img_path):
    img = image.load_img(img_path, target_size=(28, 28), color_mode="grayscale")
    img_array = image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)

    predictions = model.predict(img_array)
    class_idx = np.argmax(predictions, axis=1)

    return class_idx

img_path = 'drawing.png'
predicted_class = predict_image(img_path)
print(f'Predicted class: {predicted_class} : {classes[predicted_class[0]]}')
