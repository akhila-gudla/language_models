from pydantic import BaseModel, EmailStr,Field
from typing import Optional
class Student(BaseModel):
    name: str
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(ge=0.0, le=10.0,description="A decimal value representing cgpa of student")
# name: str='akhila' # can set like this also

new_student = {'name': 'John Doe', 'age': 21, 'email': 'akhila@gmail.com','cgpa':'4'}
student = Student(**new_student)
print(student)
print(student.name)

student_dict = dict(student)
print(student_dict['age'])
student_json = student.model_dump_json()
print(student_json)