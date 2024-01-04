from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model.Restraurant import Restaurant
from model.Review import Review
from model.Customer import Customer

if __name__ == '__main__':
    
    engine = create_engine('sqlite:///Restaurant.db' )
    Session = sessionmaker(bind=engine)
    session = Session()
    # print the name of the customers who made a review 
#     print("\n customer list:")
#     for review in session.query(Review).all():
#             customer=review.customer()
#             print(f"Review by {customer.first_name} {customer.last_name}: {review.star_rating} stars")
    

#     # print the name of the restaurant that have been reviewed
#     print("\n restaurant list :")
#     for review in session.query(Review).all():
#         restaurant= review.restaurants
#         customer=review.customers
#         print (f"review for {restaurant} {review.star_rating} stars ")
    
    
# # Retrieving a restaurant and its associated reviews from the database
# restaurant = session.query(Restaurant).first()

# # Accessing the reviews using the relationship
# all_reviews = restaurant.review()

# # Printing the restaurant and its reviews

# print("\nAll Reviews per restraurant:")
# for r in all_reviews:
#     print(f"review id : {r.id} rating: {r.star_rating} restaurant name : {restaurant.name}")

# # print the name of customers who reviewed a certain restaurant
# print("\nCustomer name and restaurant:")
# restaurant=session.query(Restaurant).first()
# all_customers = restaurant.customer()
# for r in all_customers:
#     print(f"review for {restaurant.name} by {r.first_name} {r.last_name}")


# # prints the list of restaurant that have been made by a customer
# print("\nCustomer name restaurant name and restaurant star rating:")
# customer =session.query(Customer).first()
# all_customers_reviews = customer.review()
# for r in all_customers_reviews:
#     print(f"review made by {customer.first_name +" "+ customer.last_name} for restaurant id {r.restaurant_id}  and gave a rating of {r.star_rating}")

# #print customer name and the restaurant he/she reviewed 
# print("\nCustomer name restaurant name and restaurant price:")
# customer = session.query(Customer).first()
# all_customers_reviewed_restaurants = customer.restaurant()
# for r in all_customers_reviewed_restaurants:
#     print (f"review for {r.name } by {customer.first_name + ' ' + customer.last_name}  with a price of {r.price}")
# #prints customers full name
# print("\nCustomer full name")
# customer_full_name = session.query(Customer).first().full_name()
# print (customer_full_name)
# #prints customers favorite restaurant
# customer_favorite_restaurant =session.query(Customer).first()
# customer =customer_favorite_restaurant.favorite_restaurant()
# print (f"{customer_favorite_restaurant.full_name()} favorite restaurant is {customer.name} whose price is {customer.price}")

    # existing_customer = session.query(Customer).first()
    # existing_restaurant = session.query(Restaurant).first()

    # if existing_customer and existing_restaurant:
    #     # Add a new review for the existing customer and restaurant
    #     existing_customer.add_review(restaurant=existing_restaurant, rating=5)
    #     session.commit()

    #     # Retrieve and print customer's reviews after adding a new review
    #     print(f"\nCustomer's reviews after adding a new review for restaurant '{existing_restaurant.name}':")
    #     for review in existing_customer.reviews:
    #         print(f"Review id: {review.id}, Rating: {review.star_rating} ")

    #     # Assuming specific_customer and specific_restaurant are defined
    #     specific_customer = session.query(Customer).first()
    #     specific_restaurant = session.query(Restaurant).first()

    #     if specific_customer and specific_restaurant:
    #         # Print customer's reviews before deletion
    #         print("\nCustomer's reviews before deletion:")
    #         print("Review count before deletion:", session.query(Review).count())
    #         for review in specific_customer.reviews:
    #             print(f"Review id: {review.id}, Rating: {review.star_rating}")

    #         # Delete reviews for the specified restaurant
    #         specific_customer.delete_reviews(specific_restaurant, session)  # Pass session as an argument
    #         session.commit() 

    #         # Print customer's reviews after deletion
    #         print("\nCustomer's reviews after deletion:")
    #         for review in specific_customer.reviews:
    #             print(f"Review id: {review.id}, Rating: {review.star_rating}")
    #         print("Review count after deletion:", session.query(Review).count())
    #     else:
    #         print("Customer or restaurant not found.")
    # else:
    #     print("Customer or restaurant not found.")
    
    
review_id = 1 
review_instance = session.query(Review).filter_by(id=review_id).first()

# Use the full_review method
if review_instance:
    print(review_instance.full_review())
else:
    print("Review not found.")
    


# Test example for all_reviews
restaurant_id= 2
restaurant_instance = session.query(Restaurant).filter_by(id=restaurant_id).first()

if restaurant_instance:
    reviews = restaurant_instance.all_reviews()
    print(f"All reviews for {restaurant_instance.name}:\n")
    for review in reviews:
        print(review)
else:
    print("Restaurant not found.")




# Test example for fanciest
print("\nThe fanciest restaurant :")
fanciest_restaurant = Restaurant.fanciest(session)

if fanciest_restaurant:
    print(f"The fanciest restaurant is: {fanciest_restaurant.name} with a price of {fanciest_restaurant.price}.")
else:
    print("No restaurants found.")