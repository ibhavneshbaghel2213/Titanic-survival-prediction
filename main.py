from flask import Flask, render_template, request
import pickle
import numpy as np
import sklearn
from utility.utils import str_converter

app = Flask(__name__)
model = pickle.load(open('Decision_tree_model.pkl', 'rb'))

@app.route('/',methods=["GET","POST"])
def home():
    result = ''
    return render_template('index.html',**locals())

@app.route('/predict',methods=["POST",'GET'])
def predict():
    try:
        PClass = int(request.form['Pclass'])
        Sex = str_converter(request.form['Sex'])
        Age = float(request.form['Age'])
        SibSp = int(request.form['SibSp'])
        Parch = int(request.form['Parch'])
        Fare = float(request.form['Fare'])
        result =  model.predict(np.array([PClass,Sex,Age,SibSp,Parch,Fare]).reshape(1,6))[0]
        if result == 0:
            result = "A person is Not Survived"
        else:
            result = "A person is Survived"
        return render_template('index.html',**locals())
    except Exception as E:
        result = "Enter a correct values"
        return render_template(render_template, **locals())




if __name__ == "__main__":
    app.run(debug=True)