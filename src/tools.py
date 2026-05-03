import random

# Simulated car database
cars_db = [
    {"model": "Toyota Camry", "price": 18000, "mileage": 50000},
    {"model": "Honda Civic", "price": 15000, "mileage": 40000},
    {"model": "Ford Escape", "price": 22000, "mileage": 30000},
    {"model": "BMW 3 Series", "price": 27000, "mileage": 60000},
]

def search_cars(query):
    # Simulated search (replace later with API or scraping)
    return f"Found cars matching '{query}': {cars_db}"

def price_analysis(car_info):
    # Simple scoring logic
    try:
        price = int(car_info.split("price=")[1].split(",")[0])
        mileage = int(car_info.split("mileage=")[1])
    except:
        return "Could not analyze car."

    score = 100 - (price / 1000) - (mileage / 1000)
    
    if score > 70:
        return f"Excellent deal (Score: {score})"
    elif score > 50:
        return f"Good deal (Score: {score})"
    else:
        return f"Overpriced (Score: {score})"
