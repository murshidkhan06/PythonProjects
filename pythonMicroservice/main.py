from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Employee(BaseModel):
    id: str
    name: str
    salary: float

# Initialize a list of employees statically
employees = [
    Employee(id="1", name="John Doe", salary=50000),
    Employee(id="2", name="Jane Smith", salary=60000),
    Employee(id="3", name="Alice Johnson", salary=55000)
]

@app.get("/employees", response_model=List[Employee])
def get_employees():
    return employees