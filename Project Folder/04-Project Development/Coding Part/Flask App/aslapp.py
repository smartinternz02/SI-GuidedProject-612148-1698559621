
import numpy as np
import pandas as pd
from PIL import Image
import os
import tensorflow as tf
from flask import Flask, app, request, render_template
from keras.models import Model
from keras.preprocessing import image
from tensorflow.python.ops.gen_array_ops import Concat
from keras.models import load_model

model = load_model(r"asl.h5",compile=False)
app=Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/prediction.html')
def prediction():
    return render_template('prediction.html')
@app.route('/index.html')
def home():
    return render_template("index.html")
@app.route('/logout.html')
def logout():
    return render_template('logout.html')
def preprocess_image (image_path):
    img = Image.open(image_path)
    img = img.resize((64, 64))
    img = np.array(img)
    img = tf.keras.applications.mobilenet_v2.preprocess_input(img)
    return img
@app.route('/result',methods=["GET","POST"])
def res():
    if request.method=="POST":
        f=request.files['image']
        basepath = os.path.dirname(__file__)

        filepath=os.path.join(basepath,'uploads',f.filename)

        f.save(filepath)
        labels = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','DELETE','NOTHING','SPACE']
        img = preprocess_image(filepath)
        predictions = model.predict(np.array([img]))
        predicted_class= labels[np.argmax(predictions)]
        return render_template('logout.html',pred=predicted_class)
    
if __name__ == "__main__":
    app.run(debug=True)