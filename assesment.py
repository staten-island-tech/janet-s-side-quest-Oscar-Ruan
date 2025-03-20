

""" movie_store = {
    "Inception": {"price": 4, "stock": 3,"genre": "Sci-Fi"},
    "The Conjuring": {"price": 5, "stock": 2,"genre": "Horror"},
    "Titanic": {"price": 3, "stock": 0,"genre": "Romance"},
    "Avengers": {"price": 6, "stock": 5,"genre": "Action"},
    "Joker": {"price": 4, "stock": 4,"genre": "Drama"}
}

rental_request = {
    "Inception": 1,
    "The Conjuring": 1,
    "Titanic": 1,
    "Avengers": 2
}

total_movies = 0
total_cost = 0
before = 0


for i, values in rental_request.items():
    total_movies = total_movies + values
    if movie_store[i]['stock'] == 0:
        print(f"Movie {i} is out of stock.")
    elif movie_store[i]['stock'] >= 1:
        before = before + ((movie_store[i]['price'])*(values))
        total_cost = total_cost + ((movie_store[i]['price'])*(values))
    if movie_store[i]['genre'] == "Horror":
        total_cost = total_cost - 2
        print("Applying $2 discount for renting a Horror movie.")
if total_movies >= 3:
    total_cost = total_cost*0.95
    print("Applying 5% discount or renting 3 or more movies.")

print(total_cost)
print(before) """

car_rental = {
    "Toyota Corolla": {"daily_rate": 30, "available": False, "category": "Standard"},
    "Honda Civic": {"daily_rate": 35, "available": True, "category": "Standard"},
    "BMW X5": {"daily_rate": 80, "available": True, "category": "Luxury"},
    "Mercedes C-Class": {"daily_rate": 90, "available": False, "category": "Luxury"},
    "Ford Focus": {"daily_rate": 28, "available": True, "category": "Standard"}
}
rental_request = {
    "model": "Toyota Corolla",
    "days": 8}

if car_rental[rental_request["model"]]["available"] == False:
    x = car_rental[rental_request["model"]]["category"]

for i,items in car_rental.items():
    if x == car_rental["category"]:
        print()