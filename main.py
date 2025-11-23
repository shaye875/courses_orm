from courses_orm import *
if __name__ == "__main__":
    Course.create_db_and_tables()
    Course.add_course("sql basic",20,True)
    Course.add_course("Python Intro", 30, True)
    Course.add_course("Legacy System", 10, False)
    active = Course.get_active_courses()
    print("active courses")
    for c in active:
        print(f"{c.id}: {c.name} ({c.hours} hours)")
