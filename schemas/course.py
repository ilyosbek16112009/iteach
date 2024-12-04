from pydantic import BaseModel
from typing import Optional

class CreateCourse(BaseModel):
    title: str
    period: str
    teacher: str
    lesson_count: int
    language: str
    image: Optional[str] = None
    video: Optional[str] = None


class UpdateCourse(BaseModel):
    title: Optional[str] = None
    period: Optional[str] = None
    teacher: Optional[str] = None
    lesson_count: Optional[int] = None
    language: Optional[str] = None
