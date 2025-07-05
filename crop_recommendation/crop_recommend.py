# crop_recommendation/crop_recommend.py

import pickle
import numpy as np

# Load the model only once
model = pickle.load(open('crop_recommendation/model.pkl', 'rb'))

def recommend_crop(data):
    data = np.array(data).reshape(1, -1)  # reshape to 2D array
    prediction = model.predict(data)     # use the model correctly
    return prediction[0]
