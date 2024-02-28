from fastapi import FastAPI
import pickle

app = FastAPI()

@app.get("/")
def root():
    return {'greeting':"hello"}

@app.get("/predict")
def predict(sepal_length,
            sepal_width,
            petal_length,
            petal_width):

    with open('models/best_model.pkl', 'rb') as file:
        model = pickle.load(file)

    prediction = model.predict([[sepal_length,sepal_width,petal_length,petal_width]])

    return {"prediction": float(prediction[0])}
