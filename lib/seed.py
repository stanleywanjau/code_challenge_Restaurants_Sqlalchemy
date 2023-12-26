from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# from models import Restaurant, Customer, Review, Base
from faker import Faker
from model.Restraurant import Restaurant
from model.Customer import Customer
from model.Review import Review
from model.Base import Base


# Replace 'your_database_url' with the actual URL of your database.
engine = create_engine('sqlite:///Restaurant.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()
session.query(Customer).delete()
session.query(Review).delete()
session.query(Restaurant).delete()

fake = Faker()

def seed_data():
    # Create Restaurants
    restaurants = []
    for _ in range(5):
        restaurant = Restaurant(name=fake.company(), price=fake.random_int(1, 5))
        restaurants.append(restaurant)
        session.add(restaurant)

    # Create Customers
    customers = []
    for _ in range(10):
        customer = Customer(first_name=fake.first_name(), last_name=fake.last_name())
        customers.append(customer)
        session.add(customer)

    session.commit()

    # Create Reviews
    for _ in range(30):
        review = Review(
            star_rating=fake.random_int(1, 5),
            restaurants=fake.random_element(restaurants),
            customers=fake.random_element(customers)
        )
        session.add(review)

    session.commit()

if __name__ == '__main__':
    seed_data()
print("completed")