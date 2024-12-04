from pydantic import BaseModel
from python_multipart.multipart import Field


class CreateOpinion(BaseModel):
    video: str
    full_name: str
    text: str

class UpdateOpinion(BaseModel):
    id: int = Field(...)
    video: str
    full_name: str
    text: str