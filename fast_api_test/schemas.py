from pydantic import BaseModel, EmailStr

class HelloWorld(BaseModel):
  message: str

class UserSchema(BaseModel):
  name: str
  email: EmailStr
  password: str

class UserDB(UserSchema):
  id: int

class UserSchemaResponse(BaseModel):
  id: int
  name: str
  email: EmailStr
