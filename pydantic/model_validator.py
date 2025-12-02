from pydantic import BaseModel, EmailStr,Field, model_validator  # pydantic is used for data validation and settings management using python type annotations
from typing import List , Dict, Optional, Annotated 

class Patient(BaseModel):
    
    name : str 
    email : EmailStr
    age : int 
    weight : float = Field(gt=0) # weight should be greater than 0
    married : bool
    allergies :List[str] 
    contact_details : Dict[str,str] # only dict is not sufficient we need to specify the type of keys and values in the dict
    
    @model_validator(mode='after')
    def validate_emergency_contact(cls,model):
        if model.age>60 and 'emergency' not in model.contact_details :
            raise ValueError('Patients above age 60 must have emergency conntact')
        return model
        
    
    
def update_patient_data(patient:Patient):
    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print("updated")
    
    
patient_info = {
    "name": "Pratyush",
    "email": "pratyush@hdfc.com",
    "age": 61,
    "weight": 90,
    "married": False,
    "allergies": ["dust"],
    "contact_details": {"phone": "9129078650","emergency":"123456"}
}



patient1 = Patient(**patient_info) # ** to unpack the dictionary

# insert_patient_data(patient1)
update_patient_data(patient1)   