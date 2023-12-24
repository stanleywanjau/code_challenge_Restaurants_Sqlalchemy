from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

# Base = declarative_base(
from .Base import Base

class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)
    reviews = relationship('Review', back_populates='restaurants')

    def __repr__(self):
        return f"<Restaurant(id={self.id}, name='{self.name}', price={self.price})>"



