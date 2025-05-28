from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db import Base

class Pet(Base):
    __tablename__ = 'pets'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    species = Column(String, nullable=False)
    age = Column(Integer, nullable=False)

    shelter_id = Column(Integer, ForeignKey('shelters.id'))
    shelter = relationship('Shelter', back_populates='pets')

    def __repr__(self):
        return f"<Pet(id={self.id}, name='{self.name}', species='{self.species}', age={self.age}, shelter_id={self.shelter_id})>"
