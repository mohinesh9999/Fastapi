from fastapi import FastAPI
from pydantic import BaseModel
from pymongo import MongoClient
import jwt
class Item(BaseModel):
    email: str
    password: str
class Item1(BaseModel):
    token: str
    msg: str
class Item2(BaseModel):
    token: str

client=MongoClient("mongodb+srv://test:test@cluster0-nc9ml.mongodb.net/test?retryWrites=true&w=majority")
db=client.get_database('emp')
record=db.emp_pe
app = FastAPI()
@app.get("/")
def read_root():
    return {"Hello": "World"}
@app.post("/signup")
def read_item(q:Item):
    try:
        record.insert_one({"_id":q.email,"password":q.password,"msg":[]})
        return {"status": "True"}
    except:
        return {"status": "False"}
@app.post("/login")
def read_item(q:Item):
    try:
        y=jwt.encode({"email":q.email},"mks")
        x=record.find_one({"_id":q.email,"password":q.password})
        if(x!=None):
            return {"status": "True","token":y}
        else:
            return {"status": "False"}
    except:
        return {"status": "False"}
@app.post("/msg")
def read_item(q:Item1):
    try:
        y=jwt.decode(q.token,"mks")
        print(y)
        x=record.find_one({"_id":y["email"]})
        x['msg'].append(q.msg)
        del x['_id']
        print(x)
        x=record.update_one({"_id":y["email"]},{"$set":x})
        return {"status": "True"}
    except:
        return {"status": "False"}
@app.post("/show_msg")
def read_item(q:Item2):
    try:
        y=jwt.decode(q.token,"mks")
        print(y)
        x=record.find_one({"_id":y["email"]})
        return {"status": "True","msg":x['msg']}
    except:
        return {"status": "False"}