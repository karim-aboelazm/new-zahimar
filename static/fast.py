from keras.models import load_model
from fastapi import FastAPI,File, UploadFile
from PIL import Image
import numpy as np
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()
origins = ["*"]
# Add the middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Load the model
model = load_model('model.h5')
class_labels = ['MildDemented', 'ModerateDemented', 'NonDemented', 'VeryMildDemented']

# Define a variable to store the prediction result
prediction_result = None

@app.post("/predict")
def predict(file: UploadFile):
    # Read the uploaded image file
    image = Image.open(file.file).convert('RGB')

    # Resize the image to the required input size of the model
    image = image.resize((208, 176))

    # Convert the image to a numpy array
    image_array = np.array(image)

    # Expand the dimensions of the array to match the expected input shape of the model
    image_array = np.expand_dims(image_array, axis=0)

    # Normalize the pixel values of the image
    image_array = image_array / 255.0

    # Make predictions using the loaded model
    predictions = model.predict(image_array)

    # Get the predicted class and its probability
    predicted_class_index = np.argmax(predictions[0])
    predicted_class = class_labels[predicted_class_index]
    prediction_result = {"class": predicted_class}

    # Return the prediction result
    return prediction_result

@app.get("/prediction")
def get_prediction():
    # Check if the prediction result is available
    if prediction_result:
        # Return the prediction result
        return prediction_result
    else:
        # Return an error message
        return {"message": "No prediction result available."}