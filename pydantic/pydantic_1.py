from pydantic import BaseModel  # pydantic is used for data validation and settings management using python type annotations
from typing import List , Dict 


class Patient(BaseModel):
    
    name : str
    age : int
    weight : float
    married : bool
    allergies : List[str]  # only list is not sufficient we need to specify the type of elements in the list
    contact_details : Dict[str,str] # only dict is not sufficient we need to specify the type of keys and values in the dict
    
    
def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print("inserted" )
    
def update_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print("updated" )
    
    
patient_info = {"name":"Pratyush","age":21,"weight":90,"married":False,"allergies":["pollen","dust"],"contact_details":{"email":"pratyush@google.com","phone":"9129078650"}}


patient1 = Patient(**patient_info) # ** to unpack the dictionary

# insert_patient_data(patient1)
update_patient_data(patient1)
 