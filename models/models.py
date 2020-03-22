from pydantic import BaseModel




class Item(BaseModel):
    email: str
    password: str




class Item1(BaseModel):
    token: str
    msg: str



    
class Item2(BaseModel):
    token: str