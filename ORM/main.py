from models import User,car, engine
from sqlalchemy.orm import sessionmaker

session = sessionmaker(bind=engine)
session = session()
 
"""u1 = User(name="Ashhal", email="ashhal@gmail.com")
u2 = User(name="John", email="john123@gmail.com")
u3 = User(name="Jane", email="jane@gmail.com")
session.add(u1)
session.add(u2)
session.add(u3)"""


"""all = session.query(User).all()
for u in all:
    print(u.name, u.email)"""

"""c1 = car(name="Toyota", model="Camry")
c2 = car(name="Honda", model="Civic")
c3 = car(name="Ford", model="Mustang")
session.add(c1)
session.add(c2)
session.add(c3)
"""

car1 = session.query(car).filter_by(model="Mustang").all()

session.delete(car1[0])
session.commit()


