from relationModel import engine, Car, Company
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

def get_companyID(company_name):
    company = session.query(Company).filter_by(name=company_name).first()
    if company:
        return company.id
    else:
        return None

"""comp = Company (name = "Toyota")
comp2 = Company (name = "Honda")
comp3 = Company (name = "Ford")

car1 = Car (model = "Supra", company=comp)
car2 = Car (model = "Civic", company=comp2)
car3 = Car (model = "Mustang", company=comp3)

session.add(car1)
session.add(car2)
session.add(car3)
session.commit()"""

"""new_car = Car (model = "NSX", company_id=2)
session.add(new_car)"""


"""ID = get_companyID("Honda")
print (ID)

del_car = session.query(Car).filter(Car.company_id == ID).all()
for car in del_car:
    session.delete(car)
session.commit()
session.delete(session.query(Company).filter(Company.id == ID).first())
session.commit()
"""