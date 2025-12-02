from pydantic import BaseModel, EmailStr,Field, field_validator  # pydantic is used for data validation and settings management using python type annotations
from typing import List , Dict, Optional, Annotated 

class Patient(BaseModel):
    
    name : str 
    email : EmailStr
    age : int 
    weight : float = Field(gt=0) # weight should be greater than 0
    married : bool
    allergies :List[str] 
    contact_details : Dict[str,str] # only dict is not sufficient we need to specify the type of keys and values in the dict
    
    
    @field_validator('email') # field_validator is a decorator used to validate a specific field and it is a classmethod
    @classmethod
    def email_validator(cls,value):
        
        valid_domains =['hdfc.com','icici.com']
        
        domain_name = value.split('@')[-1] # get the domain name by splitting the email id from '@'
        
        if domain_name not in valid_domains:
            raise ValueError("Not a valid domain")
        
        return value
    
    @field_validator('name') # field_validator is a decorator used to validate a specific field and it is a classmethod
    @classmethod
    def transform_name(cls,value):
       return value.upper()
        
        
        
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
    "age": 21,
    "weight": 90,
    "married": False,
    "allergies": ["dust"],
    "contact_details": {"phone": "9129078650"}
}



patient1 = Patient(**patient_info) # ** to unpack the dictionary

# insert_patient_data(patient1)
update_patient_data(patient1)
 