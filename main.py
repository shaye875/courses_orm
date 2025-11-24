from courses_orm import *
if __name__ == "__main__":
    create_db_and_tables()
    add_course("sql basic",20,True)
    add_course("Python Intro", 30, True)
    add_course("Legacy System", 10, True)
    active = get_active_courses()
    print("active courses")
    for c in active:
        print(f"{c.id}: {c.name} ({c.hours} hours)")
