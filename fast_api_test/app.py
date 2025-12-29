from http import HTTPStatus
from fastapi import FastAPI, HTTPException
from fast_api_test.schemas import HelloWorld, UserSchema, UserSchemaResponse, UserDB, UserListResponse, Message

app = FastAPI()

database = []

@app.get('/', response_model=HelloWorld)
def read_root():
  return {"message": "Olá mundo 1"}

@app.post('/users', status_code=HTTPStatus.CREATED, response_model=UserSchemaResponse)
def create_user(user: UserSchema):
  
  created_user = UserDB(
    id=len(database) + 1,
    **user.model_dump(),
  )
  
  database.append(created_user)

  return created_user

@app.get('/users', response_model=UserListResponse)
def read_users():
  return {'users': database}

@app.put('/users/{user_id}', response_model=UserSchemaResponse)
def update_user(user_id: int, user: UserSchema):
  if user_id < 1 or user_id > len(database):
    raise HTTPException(
      status_code=HTTPStatus.NOT_FOUND,
      detail='User not found'
    )
  
  updated_user = UserDB(id=user_id, **user.model_dump())
  
  database[user_id - 1] = updated_user
  
  return updated_user

@app.delete('/users/{user_id}', response_model=Message)
def delete_user(user_id: int):
  if user_id < 1 or user_id > len(database):
    raise HTTPException(
      status_code=HTTPStatus.NOT_FOUND,
      detail='User not found'
    )
  
  del database[user_id - 1]

  return {'message': "User deleted"}

  