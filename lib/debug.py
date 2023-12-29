from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model.Restraurant import Restaurant
from model.Review import Review
from model.Customer import Customer

if __name__ == '__main__':
    
    engine = create_engine('sqlite:///Restaurant.db')
    Session = sessionmaker(bind=engine)
    session = Session()
       # print the name of the customers who made a review 
    print("\n customer list:")
    for review in session.query(Review).all():
            customer=review.customers
            print(f"Review by {customer.first_name} {customer.last_name}: {review.star_rating} stars")
    
    
   
    # rint the name of the restaurant that have been reviewed
    print("\n restaurant list :")
    for review in session.query(Review).all():
        restaurant= review.restaurants
        customer=review.customers
        print (f"review for {restaurant.name} {review.star_rating} stars ")
    
    
# Retrieving a restaurant and its associated reviews from the database
restaurant = session.query(Restaurant).first()

# Accessing the reviews using the relationship
all_reviews = restaurant.review()

# Printing the restaurant and its reviews

print("\nAll Reviews per restraurant:")
for r in all_reviews:
    print(f"review id : {r.id} rating: {r.star_rating} restaurant name : {restaurant.name}")

# print the name of customers who reviewed a certain restaurant
print("\nCustomer name and restaurant:")
restaurant=session.query(Restaurant).first()
all_customers = restaurant.customer()
for r in all_customers:
    print(f"review for {restaurant.name} by {r.first_name} {r.last_name}")

# prints the list of restaurant that have been made by a customer
print("\nCustomer name restaurant name and restaurant star rating:")
customer =session.query(Customer).first()
all_customers_reviews = customer.review()
for r in all_customers_reviews:
    print(f"review made by {customer.first_name +" "+ customer.last_name} for restaurant id {r.restaurant_id}  and gave a rating of {r.star_rating}")

#print customer name and the restaurant he/she reviewed 
print("\nCustomer name restaurant name and restaurant price:")
customer = session.query(Customer).first()
all_customers_reviewed_restaurants = customer.restaurant()
for r in all_customers_reviewed_restaurants:
    print (f"review for {r.name } by {customer.first_name + ' ' + customer.last_name}  with a price of {r.price}")

