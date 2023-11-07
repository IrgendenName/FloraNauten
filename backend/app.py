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


@app.route('/hook', methods=['POST'])
def save_canvas():
    try:
        image_data = re.sub('^data:image/.+;base64,', '', request.get_json()['image'])
        from PIL import Image
        im = Image.open(BytesIO(base64.b64decode(image_data)))
        # im.save('canvas.png')
        im28x28 = im.resize((28, 28)).convert('L') #resize the image to 28x28 and converts it to gray scale

        # image to numpy
        np_image = np.asarray(im28x28)
        # assert(np_image.shape == (28, 28))
        print(np.abs(np_image.reshape(28*28)-[255]))

        # np.abs(np_image.reshape(28*28)-[255]) 
        # reshapes the image to 28x28 pixes, substracts 255 from every value and applys abs to the matrix.
        # this has to be done, becuase the mnist values are "Pixel values are 0 to 255. 0 means background (white), 255 means foreground (black). " (s. http://yann.lecun.com/exdb/mnist/)
        # Grayscale uses 0 for black and 255 for white.
        predicted_number = model.predict([np.abs(np_image.reshape(28*28)-[255])])
        print(predicted_number)

        buffered = BytesIO()
        im28x28.save(buffered, format="PNG")
        # im28x28.save('canvas2.png')
        img_str = base64.b64encode(buffered.getvalue())
        img_base64 = bytes("data:image/png;base64,", encoding='utf-8') + img_str
        return json.dumps({'image': str(img_base64.decode('utf-8')), 'prediction': predicted_number[0]}), 200, {'ContentType': 'application/json'}
    except Exception as err:
        return json.dumps({'error': str(err)})

@app.route("/")
def hello_world():

    print(request.args)
    return "<p>Current model!</p>" + str(model)
    
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
