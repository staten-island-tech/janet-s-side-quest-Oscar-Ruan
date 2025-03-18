

movie_store = {
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

z = 0
a = 0
idk = {}

for i, values in rental_request.items():
    z = z + values
    if (movie_store[i["stock"]]) == 0:
        idk.append(movie_store[i])
    if (movie_store[i["stock"]]) >=0:
        a = movie_store["price"]*values

print(a)
print(idk)
