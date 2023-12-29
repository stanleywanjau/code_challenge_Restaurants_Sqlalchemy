from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

# Base = declarative_base()
from .Base import Base

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    reviews = relationship('Review', back_populates='customers')
    restaurants = relationship('Restaurant',secondary='reviews' ,back_populates='customers',viewonly=True)

    def __repr__(self):
        return f"<Customer(id={self.id}, first_name='{self.first_name}', last_name='{self.last_name}')>"
    def review(self):
        return self.reviews
    def restaurant(self):
        return self.restaurants




