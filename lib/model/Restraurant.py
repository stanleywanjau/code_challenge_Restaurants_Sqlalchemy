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
    customers = relationship('Customer', secondary='reviews', back_populates='restaurants' ,viewonly=True)

    def __repr__(self):
        return f"<Restaurant(id={self.id}, name='{self.name}', price={self.price})>"
    def review(self):
        return self.reviews
    def customer(self):
        return self.customers
        



