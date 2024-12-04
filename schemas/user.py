from pydantic import BaseModel, Field


class CreateUser(BaseModel):
    name: str
    username: str
    email: str
    password: str = Field(..., min_length=8, max_length=16, description="Parol kamida 8 ta belgidan iborat bo'lishi kerak!!!")


class UpdateUser(BaseModel):
    name: str
    username: str
    email: str
    password: str = Field(..., min_length=8, max_length=16, description="Parol kamida 4 ta belgidan iborat bo'lishi kerak!!!")
