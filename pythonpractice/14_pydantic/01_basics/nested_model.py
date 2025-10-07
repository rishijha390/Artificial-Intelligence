from typing import List , Optional
from pydantic import BaseModel

class Address(BaseModel):
    street: str
    city: str
    state: str
    pincode: str

class User(BaseModel):
    id: int
    name: str
    address: Address


address = Address(
    street="123 Main St",
    city="Springfield",
    state="IL",
    pincode="12345"
)

user = User(
    id=1,
    name="John Doe",
    address=address,
)

user_data = {
    "id": 1,
    "name": "John Doe",
    "address": {
        "street": "123 Main St",
        "city": "Springfield",
        "state": "IL",
        "pincode": "12345",
}
}
user = User(**user_data)  
print(user)
