from flask import Flask, request, make_response, render_template, jsonify, send_file
import numpy as np
import pandas as pd
import pickle
import os


def classification(input_data):
    
    with open('feature.pkl', 'rb') as fid:
        features = pickle.load(fid)

    input_data.dropna(inplace = True)

    doc_list = input_data[0].values.tolist()
    test_doc = []
    for t in doc_list:
        test_doc.append(t.split(' '))

    with open('model.pkl', 'rb') as fid:
        classifier = pickle.load(fid)

    prediction = []
    for i in range(len(test_doc)):
        prediction.append(classifier.classify(get_features(test_doc[i],features)))

    return prediction

# function to create features dictionary based on most freq words of training set
def get_features(doc,features):
    current_features = {}
    doc_set = set(doc)
    for f in features:
        current_features[f] = f in doc_set
    return current_features


app = Flask(__name__)


@app.route("/")
def start():
    return render_template('index.html')

@app.route("/api/predict", methods=['POST', 'GET'])
def predict():

    if request.method == 'GET':
        return render_template('index.html')
    else:
        uploaded_file = request.files['file']
        input_data = pd.read_csv(uploaded_file, sep=',', header = None)
        if input_data.empty:
            return render_template("error.html", error_message='Input file is empty!')
        else:
            input_data['Document'] = classification(input_data)
            response = make_response(input_data.to_csv(index=False))
            response.headers["Document"] = "attachment; filename=predictions.csv"
            response.headers["Content-Type"] = "text/csv"
            return response
            
            
if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0',port=80)