from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db import Base

class Shelter(Base):
    __tablename__ = 'shelters'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)

    pets = relationship('Pet', back_populates='shelter')

    def __repr__(self):
        return f"<Shelter(id={self.id}, name='{self.name}', location='{self.location}')>"
