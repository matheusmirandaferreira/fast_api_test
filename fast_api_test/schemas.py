from pydantic import BaseModel, EmailStr

class HelloWorld(BaseModel):
  message: str

class UserSchema(BaseModel):
  name: str
  email: EmailStr
  password: str

class UserSchemaResponse(BaseModel):
  name: str
  email: EmailStr
