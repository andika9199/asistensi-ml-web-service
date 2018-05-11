from flask import Flask,jsonify,request
from flasgger import Swagger
from Model.Dataseed import tasks
from Model.Petal import Petal

app = Flask(__name__)
Swagger(app)

@app.route('/')
def hello_world():
    return "Halooo"


@app.route('/getData',methods=['GET'])
def getData():
    """
    Ini Adalah Endpoint untuk mengambil seluruh data yang ada.
    ---
    tags :
        -Rest Controller
    parameter:
    responses:
        200:
            description: Success Get All Data
    """
    return jsonify({'tasks':tasks,'success':True})


@app.route('/input',methods=['POST'])
def inputData():
    """
    Ini adalah Endpoint untuk menambahkan Data Task
    ---
    tags :
        - Rest Controller
    parameters:
      - name: body
        in : body
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
    panjang1=dataBaru['panjang']
    lebar1=dataBaru['lebar']
    panjang2=dataBaru['panjang2']
    lebar2=dataBaru['lebar2']

    petalBaru=Petal(panjang1,lebar1,panjang2,lebar2)
    tasks.append(petalBaru.__dict__)
    return jsonify({'message':'success'})


@app.route('/update/<int:id>',methods=['PUT'])
def updateData(id):
    """
    Ini adalah Endpoint untuk mengupdate Data Task
    ---
    tags :
        - Rest Controller
    parameters:
       - in: path
         name: id
         required: true
         type: integer
       - in: body
         name: body
         required: true
         schema:
           id: Product
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
            description: Success Update
    """
    dataBaru=request.get_json()
    panjang1=dataBaru['panjang']
    lebar1=dataBaru['lebar']
    panjang2=dataBaru['panjang2']
    lebar2=dataBaru['lebar2']

    petalBaru=Petal(panjang1,lebar1,panjang2,lebar2)
    tasks[id]=petalBaru.__dict__
    return jsonify({'message':'success'})

@app.route('/delete/<int:id>',methods=['DELETE'])
def deleteTask(id):
    """
       Ini adalah Endpoint untuk menghapus Data Task tertentu
       ---
       tags :
           - Rest Controller
       parameters:
         - in: path
           name: id
           required: true
           type: integer
       response:
           200:
               description: Success Delete
    """
    del tasks[id]
    return jsonify({'message':'success delete'})


# if __name__=='__main__':
#     app.run()