from prac_model import student, engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

"""s1 = student(name="ash",age=20,course="ORM")
s2 = student(name="ahmad",age=22,course="SE")
s3 = student(name="Hasnat",age=21,course="DEVops")

session.add(s1)
session.add(s2)
session.add(s3)"""

"""students = session.query(student).all()
for s in students:
    print(s.name,s.age,s.course)"""

"""by_age = session.query(student).filter(student.age<=20).all()
for s in by_age:
    print(s.name,s.age,s.course)"""

"""s = session.query(student).filter(student.name=="ash").first()
s.course = "Software Engineering"
"""

#session.delete(session.query(student).filter(student.name=="ash").first())
#session.commit()