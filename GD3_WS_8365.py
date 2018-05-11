from flask import Flask,jsonify,request
from flasgger import Swagger
from sklearn.externals import joblib
import numpy as np

app = Flask(__name__)
Swagger(app)

@app.route('/')
def hello_world():
    return "GD 03"


@app.route('/input',methods=['POST'])
def inputData():
    """
    Ini adalah Endpoint untuk memprediksi Data IRIS
    ---
    tags :
        - Rest Controller
    parameters:
      - name: body
        in: body
        required: true
        schema:
          id: Petal
          required:
            -sepalLength
            -sepalWidth
            -petalLength
            -petalWidth
          properties:
            sepalLength:
              type: int
              description: Please input with valid Sepal and Petal Length-Width.
              default: 0
            sepalWidth:
              type: int
              description: Please input with valid Sepal and Petal Length-Width.
              default: 0
            petalLength:
              type: int
              description: Please input with valid Sepal and Petal Length-Width.
              default: 0
            petalWidth:
              type: int
              description: Please input with valid Sepal and Petal Length-Width.
              default: 0
    response:
        200:
            description: Success Input
    """
    dataBaru=request.get_json()
    petalLength=dataBaru['petalLength']
    petalWidth=dataBaru['petalWidth']
    sepalLength=dataBaru['sepalLength']
    sepalWidth=dataBaru['sepalWidth']

    petalBaru=np.array([[petalLength,petalWidth,sepalLength,sepalWidth]])
    clf=joblib.load('static/knnClassifier.pkl')
    resultPredict=clf[0].predict(petalBaru)
    return jsonify({'message':format(clf[1].target_names[resultPredict])})

app.run(debug=True)