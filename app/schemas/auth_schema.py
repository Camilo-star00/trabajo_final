from pydantic import BaseModel, Field

class LoginSchema(BaseModel):
    usuario: str = Field(..., example="camilo")
    password: str = Field(..., example="123456")