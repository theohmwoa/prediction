from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from classes import classes
import io
from PIL import Image

app = Flask(__name__)
CORS(app)

model = tf.keras.models.load_model('quickdraw_model.h5')

def predict_image(img):
    img = img.convert('L')

    img = img.resize((28, 28))

    img_array = image.img_to_array(img)

    img_array = np.expand_dims(img_array, axis=0)

    predictions = model.predict(img_array)
    sorted_indices = np.argsort(predictions[0])[::-1]

    sorted_classes = [classes[idx] for idx in sorted_indices]

    return sorted_classes

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return "No file part", 400

    file = request.files['file']

    if file.filename == '':
        return "No selected file", 400

    if file:
        img = Image.open(io.BytesIO(file.read()))
        sorted_class_names = predict_image(img)
        return jsonify({'sorted_class_names': sorted_class_names})

if __name__ == '__main__':
    app.run(debug=True)
