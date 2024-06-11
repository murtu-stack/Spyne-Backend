
from database.create_tables import create_tables
from fastapi import FastAPI,Depends,HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.encoders import jsonable_encoder
from database.db_session import db
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from pydantic import BaseModel
from datetime import timedelta,timezone
from passlib.context import CryptContext
from interactions.create_user import create_user
from playhouse.postgres_ext import BigAutoField
from interactions.get_current_user import get_current_user
from interactions.get_login_for_access_token import login_for_access_token
from interactions.get_document import  get_document
from interactions.delete_document import delete_document
from interactions.share_document import share_document
from interactions.update_document import update_document
from interactions.create_document import create_document
from interactions.revert_to_version import revert_to_version




SECRET_KEY = "c2c78544f5fafc0673f1d2631c755571c11452d16dedf209060575b9d77ac82a"

ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTE = 30

class Token(BaseModel):
    access_token: str
    token_type: str

app = FastAPI()
# create_tables()
class UserData(BaseModel):
    user_name: str 
    email: str
    password: str 
    mobile_no: int=None
    first_name: str=None
    last_name: str=None
   
   
   
class DocumentCreate(BaseModel):
    title: str
    content: str
    is_private: bool = False
    
    
class DocumentGet(BaseModel):
    id: str
    
class DocumentUpdate(BaseModel):
    id: int
    title: str
    content: str

class DocumentRevert(BaseModel):
    version_id: int
    document_id: int
    title: str
    content: str

@app.post("/create_user")
def create_user_api(request: UserData):
    try:
        return create_user(request.model_dump())
    except Exception as e:
        raise
    
@app.post("/token",response_model=Token)
def login_api(request: OAuth2PasswordRequestForm = Depends()):
    return jsonable_encoder(login_for_access_token(request))
    

@app.post("/create_document")
def create_document_api(request: DocumentCreate,response = Depends(get_current_user)):
    try:
        data = create_document(request.dict(),response.get("user_name"))
        return JSONResponse(status_code=200, content=jsonable_encoder(data))
    except HTTPException as e:
        raise
    
@app.get("/get_document")
def get_document_api(request: DocumentGet,response = Depends(get_current_user)):
    try:
        data = get_document(request.dict(),response.get("user_name"))
        return JSONResponse(status_code=200, content=jsonable_encoder(data))
    except HTTPException as e:
        raise
    
@app.post("/update_document")
def update_document_api(request: DocumentUpdate,response = Depends(get_current_user)):
    try:
        data = update_document(request.dict(),response.get("user_name"))
        return JSONResponse(status_code=200, content=jsonable_encoder(data))
    except HTTPException as e:
        raise
    
@app.post("/document_")
def update_document_api(request: DocumentUpdate,response = Depends(get_current_user)):
    try:
        data = update_document(request.dict(),response.get("user_name"))
        return JSONResponse(status_code=200, content=jsonable_encoder(data))
    except HTTPException as e:
        raise
    
@app.get("/users/me/")
def read_users_me(request: UserData= Depends(get_current_user)):
    return request.model_dump()

