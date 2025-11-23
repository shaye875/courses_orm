from dataclasses import field
from typing import Optional
from sqlmodel import create_engine,Session,select
from sqlalchemy import table
from sqlmodel import SQLModel, Field
class Course(SQLModel,table = True):
    id:Optional[int] = Field(default=None,primary_key=True)
    name:str
    hours:int
    is_active:bool = True
    engine = create_engine("sqlite:///courses.db,echo = True")
    @staticmethod
    def create_db_and_tables():
        SQLModel.metadata.create_all(Course.engine)

    def add_course(self,name,hours,is_active = True):
        course = Course(name = name,hours = hours,is_active = is_active)
        with Session(self.engine) as session:
            session.add(course)
            session.commit()
            session.refresh(course)
        print(f"added course with id = {course.id}")
    @staticmethod
    def get_active_courses():
        pass
        # with Session(Course.engine) as session:
            # statement = select(Course).where(Course.is_active == True)
            # result = session.exec(statement)
            # courses = result.all()
            # return courses