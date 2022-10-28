from flask import Flask, render_template, request
import pickle
import numpy as np
import sklearn

app = Flask(__name__)
model = pickle.load(open('Decision_tree_model.pkl', 'rb'))

@app.route('/',methods=["GET","POST"])
def home():
    result = ''
    return render_template('index.html',**locals())

@app.route('/predict',methods=["POST",'GET'])
def predict():
    PClass = int(request.form['Pclass'])
    Sex = int(request.form['Sex'])
    Age = str_converter(request.form['Age'])
    SibSp = int(request.form['SibSp'])
    Parch = int(request.form['Parch'])
    Fare = float(request.form['Fare'])
    result =  model.predict(np.array([PClass,Sex,Age,SibSp,Parch,Fare]).reshape(1,6))
    return render_template('index.html',**locals())




if __name__ == "__main__":
    app.run(debug=True)