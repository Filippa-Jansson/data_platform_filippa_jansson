from pydantic import BaseModel

class UserSchema(BaseModel):
    username: str
    password: str

class UserSchemaResponse(BaseModel):
    username: str