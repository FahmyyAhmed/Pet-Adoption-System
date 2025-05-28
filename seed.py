from db import engine, Session
from models.shelter import Shelter
from models.pet import Pet
from db import Base

Base.metadata.create_all(engine)

session = Session()

shelter1 = Shelter(name="Al-Rahma Shelter", location="Cairo")
shelter2 = Shelter(name="Dar Al-Karim", location="Istanbul")
shelter3 = Shelter(name="Bayt Al-Hilal", location="Jakarta")
session.add_all([shelter1, shelter2, shelter3])
session.commit()

pet1 = Pet(name="Aisha", species="Cat", age=2, shelter=shelter1)
pet2 = Pet(name="Bilal", species="Dog", age=3, shelter=shelter2)
pet3 = Pet(name="Fatima", species="Rabbit", age=1, shelter=shelter3)
pet4 = Pet(name="Hassan", species="Bird", age=4, shelter=shelter1)
pet5 = Pet(name="Khadija", species="Turtle", age=5, shelter=shelter2)
pet6 = Pet(name="Omar", species="Fish", age=1, shelter=shelter3)

session.add_all([pet1, pet2, pet3, pet4, pet5, pet6])
session.commit()

session.close()
print("Database seeded بنجاح!")