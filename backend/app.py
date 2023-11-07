# install Flask: pip install Flask
# run app: flask --app app run
# Running on http://127.0.0.1:5000

from flask import Flask, request
from flask_cors import CORS
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsClassifier
import pickle
import os
import numpy as np

#from PIL import Image
from io import BytesIO
import base64
import json
import re
import sys

app = Flask(__name__)
CORS(app)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000

model = None


def load_model():
    # load the pre-trained model (here we are using a model
    # pre-trained of week 8, but you can
    # substitute in your own networks just as easily)
    global model
        # create prediction
    model = KNeighborsClassifier(n_neighbors=4, weights='distance')
    model_filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), "knn_clf.pkl")
    with open(model_filename, 'rb') as f:
        model = pickle.load(f)


@app.route("/api/predict/", methods=['GET'])
def predict():
    bfs_number = int(request.args['bfs_number'])
    area = float(request.args['area'])
    rooms = float(request.args['rooms'])
    
    df_bfs_data = pd.read_csv(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'bfs_municipality_and_tax_data.csv'),
                            sep=',', encoding='utf-8')
    df_bfs_data['tax_income'] = df_bfs_data['tax_income'].str.replace("'", "")
    df = df_bfs_data[df_bfs_data['bfs_number']==bfs_number]

    randomforest_model = RandomForestRegressor()
    model_filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), "randomforest_regression.pkl")
    with open(model_filename, 'rb') as f:
        randomforest_model = pickle.load(f)

    # ['rooms' 'area' 'pop' 'pop_dens' 'frg_pct' 'emp' 'tax_income' 'm2_per_rooms']
    prediction = randomforest_model.predict([[rooms, area, df['pop'].iloc[0], df['pop_dens'].iloc[0], df['frg_pct'].iloc[0], df['emp'].iloc[0], df['tax_income'].iloc[0], area/rooms]])
    return str(round(prediction[0],2))

@app.route("/")
def hello_world():
    return "<p>Hello World</p>" + str(model)
    
# if this is the main thread of execution first load the model and
# then start the server
print('name')
print(__name__)

if __name__ == "__main__" or __name__ == "app" or __name__ == "flask_app":
    print(("* Loading model and Flask starting server..."
        "please wait until server has fully started"))
    load_model()

    print(sys.executable)
    print('running')
