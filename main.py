from fastapi import FastAPI
import json

app = FastAPI()

def load_data(): 
    with open('patients.json', 'r') as f:
        data = json.load(f)
    return data

@app.get("/")
def hello():
    return {"Message": "Patient Management System API"}

@app.get("/about")
def about():
    return {"Message": "This API is designed to manage patient records efficiently."} 

@app.get("/view")
def view():
    data = load_data()
    return data