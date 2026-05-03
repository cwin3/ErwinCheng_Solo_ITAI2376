import requests
import random

# Backup dataset
fallback_cars = [
    {"model": "Toyota Camry", "price": 18000, "mileage": 50000, "image": "https://cdn.pixabay.com/photo/2012/05/29/00/43/car-49278_1280.jpg"},
    {"model": "Honda Civic", "price": 15000, "mileage": 40000, "image": "https://cdn.pixabay.com/photo/2013/07/13/10/07/car-156309_1280.png"},
    {"model": "Ford Escape", "price": 22000, "mileage": 30000, "image": "https://cdn.pixabay.com/photo/2012/05/29/00/43/car-49279_1280.jpg"},
    {"model": "BMW 3 Series", "price": 27000, "mileage": 60000, "image": "https://cdn.pixabay.com/photo/2012/05/29/00/43/car-49280_1280.jpg"},
]

def search_cars(query):
    # Simulate API call (replace with real API later)
    return fallback_cars

def calculate_score(price, mileage):
    score = 100 - (price / 1000) - (mileage / 2000)
    return round(score, 1)

def price_analysis(cars):
    results = []
    for car in cars:
        score = calculate_score(car["price"], car["mileage"])
        car["score"] = score
        results.append(car)
    return results
