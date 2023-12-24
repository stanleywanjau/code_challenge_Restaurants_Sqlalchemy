from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    ForeignKey,
    CheckConstraint,
    UniqueConstraint,
    DateTime,
    Table,
    MetaData
    
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship,backref

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)
engine = create_engine('sqlite:///Restaurant.db')

Base = declarative_base()




class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)
    reviews=relationship('Review',back_populates=('restaurants'))
    

    

    def __repr__(self):
        return f"<Restaurant(id={self.id}, name='{self.name}', price={self.price})>"
class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    reviews=relationship('Review',back_populates=('customers'))
    
    def __repr__(self):
        return f"<Customer(id={self.id}, first_name='{self.first_name}', last_name='{self.last_name}')>"
      
class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    star_rating = Column(Integer)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    customer_id = Column(Integer, ForeignKey('customers.id'))
    
    restaurants = relationship('Restaurant', back_populates=('reviews'))
    customers = relationship('Customer', back_populates=('reviews')) 
    
    def __repr__(self):
        return f"<Review(id={self.id}, star_rating={self.star_rating}, restaurant_id={self.restaurant_id}, customer_id={self.customer_id})>"