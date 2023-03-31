from fastapi import FastAPI
from pydantic import BaseModel
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib
import pandas as pd

app = FastAPI()

# Load Boston Housing Dataset
boston = fetch_openml(name='boston')
X = boston.data
y = boston.target

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a linear regression model on the training set
model = LinearRegression()
model.fit(X_train, y_train)

# Save the trained model to disk
joblib.dump(model, "model.joblib")

# Define input parameters for the API endpoint
class InputParams(BaseModel):
    CRIM: float
    ZN: float
    INDUS: float
    CHAS: int
    NOX: float
    RM: float
    AGE: float
    DIS: float
    RAD: int
    TAX: float
    PTRATIO: float
    B: float
    LSTAT: float

# Define the API endpoint for predicting median value of owner-occupied homes
@app.post("/predict")
async def predict(input_params: InputParams):
    # Load the trained model from disk
    model = joblib.load("model.joblib")
    # Convert input parameters to a numpy array
    input_array = [[
        input_params.CRIM, input_params.ZN, input_params.INDUS, input_params.CHAS,
        input_params.NOX, input_params.RM, input_params.AGE, input_params.DIS,
        input_params.RAD, input_params.TAX, input_params.PTRATIO, input_params.B,
        input_params.LSTAT
    ]]
    # Use the model to predict the median value of owner-occupied homes
    prediction = model.predict(input_array)
    # Return the predicted value as a JSON response
    return {"prediction": prediction[0]}
