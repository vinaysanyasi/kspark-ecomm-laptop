from pydantic import BaseModel


class Laptop(BaseModel): 
    id: int
    brand: str
    capacity: int
    screensize: float 