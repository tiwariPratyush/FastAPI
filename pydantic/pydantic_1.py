from pydantic import BaseModel, EmailStr,Field  # pydantic is used for data validation and settings management using python type annotations
from typing import List , Dict, Optional, Annotated 


class Patient(BaseModel):
    
    # name : str = Field(max_length=50) # name should not exceed 50 characters
    name : Annotated[str,Field(max_length=50,title="Name of the Patient",description="This field is used to store the name of the patient",examples = ["Pratyush","Saurabh"])] # using annotated to add more metadata
    email : EmailStr
    age : int = Field(gt=0,lt=60) # age should be greater than 0 and less than 60
    weight : float = Field(gt=0) # weight should be greater than 0
    # married : bool
    married : Annotated[bool,Field(default=None,title="Marital Status",description="This field indicates whether the patient is married or not",examples=[True,False])] # using annotated to add more metadata
    allergies : Optional[List[str]] = None  # only list is not sufficient we need to specify the type of elements in the list
    contact_details : Dict[str,str] # only dict is not sufficient we need to specify the type of keys and values in the dict
    
    
def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print("inserted" )
    
def update_patient_data(patient:Patient):
    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print("updated" )
    
    
patient_info = {"name":"Pratyush","email":"pratyush@gmail.com","age":21,"weight":90,"married":False,"contact_details":{"phone":"9129078650"}}


patient1 = Patient(**patient_info) # ** to unpack the dictionary

# insert_patient_data(patient1)
update_patient_data(patient1)
 