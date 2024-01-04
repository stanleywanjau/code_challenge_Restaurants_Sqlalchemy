from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import object_session
from .Review import Review
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
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    def favorite_restaurant(self):
        if not self.reviews:
            return  None
        else:
            return max (self.review(),key=lambda review: review.star_rating).restaurant()
    def add_review(self, restaurant, rating):
        new_review = Review( star_rating=rating, restaurant=restaurant,customer=self)
        self.reviews.append(new_review)
        return new_review
    def delete_reviews(self, restaurant, session):
        reviews_to_delete = [review for review in self.reviews if review.restaurant == restaurant]
        for review in reviews_to_delete:
            session.delete(review)
        session.commit()
        session.refresh(self) 