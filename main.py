from fastapi import FastAPI,Path
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

@app.get("/patient/{patient_id}")
def view_patient(patient_id: str=Path(..., description="ID of the patient in the DB",example="P001")):
    # load all patients data
    data = load_data()
    
    if patient_id in data:
        return data[patient_id]
    return {"Error": "Patient not found."}