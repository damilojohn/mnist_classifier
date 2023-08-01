import requests 
import json 
import numpy as np 

bucket_name = 'mnist_classifier'
key = 'validation/test_features.joblib'

data = {
    'bucket':bucket_name,
    'key':key
}


headers = {
    'Content-type':'application/json'
}

#main code for post HTTP request 

url = 'http://127.0.0.1:3000/predict'
response = requests.request('POST',url,headers=headers,data=json.dumps(data))

lambda_predictions = np.array(response.json())
show_cm(test_target, lambda_predictions, range(10))
