from fastapi import FastAPI, status
from fast_api_test.schemas import HelloWorld, UserSchema, UserSchemaResponse

app = FastAPI()

@app.get('/', response_model=HelloWorld)
def read_root():
  return {"message": "Olá mundo 1"}

@app.post('/users', response_model=UserSchemaResponse, status_code=status.HTTP_201_CREATED)
def create_user(user: UserSchema):
  print(user) 
  return None