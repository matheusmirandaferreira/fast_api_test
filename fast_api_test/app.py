from fastapi import FastAPI, status
from fast_api_test.schemas import HelloWorld, UserSchema, UserSchemaResponse, UserDB

app = FastAPI()

database = []

@app.get('/', response_model=HelloWorld)
def read_root():
  return {"message": "Olá mundo 1"}

@app.post('/users', status_code=status.HTTP_201_CREATED, response_model=UserSchemaResponse)
def create_user(user: UserSchema):
  
  created_user = UserDB(
    id=len(database) + 1,
     user.model_dump()
  )
  
  database.append(create_user)
  
  return created_user
