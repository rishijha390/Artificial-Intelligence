from typing import Optional
from pydantic import BaseModel,Field
import re

class Employee(BaseModel):
    id: int
    name: str = Field(
        ...,
        min_length=3,
        max_length=50,
        description="Employee Name",
        examples="Rishi Jha"
    )

    department: Optional[str] = 'General'
    salary: float = Field(
        ...,
        ge=10000

    )

class User(BaseModel):
    email : str = Field( ...,pattern=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$' )
    phone: str = Field(...,pattern=r'^\+?[1-9]\d{1,14}$')
    age: int = Field(
        ...,
        ge=0,
        le=150,
        description="Age in years",
    )
    discount: float = Field(
        ...,
        ge=0,
        le=100,
        description="Discount percentage",
    )


u = User(email="rishi.jha@gmail.com", phone="+919876543210", age=28, discount=10)
print(u)

