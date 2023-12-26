from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model.Restraurant import Restaurant
from model.Review import Review
from model.Customer import Customer

if __name__ == '__main__':
    
    engine = create_engine('sqlite:///Restaurant.db')
    Session = sessionmaker(bind=engine)
    session = Session()
        
    print("\n customer list:")
    for review in session.query(Review).all():
            customer=review.customers
            print(f"Review by {customer.first_name} {customer.last_name}: {review.star_rating} stars")
    
    
   
    
    print("\n restaurant list :")
    for review in session.query(Review).all():
        restaurant= review.restaurants
        customer=review.customers
        print (f"review for {restaurant.name} {review.star_rating} stars ")