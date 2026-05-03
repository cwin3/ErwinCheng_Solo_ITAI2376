import requests

fallback = [
    {"model":"Toyota Camry","price":18000,"mileage":50000,"image":"https://cdn.pixabay.com/photo/2012/05/29/00/43/car-49278_1280.jpg"},
    {"model":"Honda Civic","price":15000,"mileage":40000,"image":"https://cdn.pixabay.com/photo/2013/07/13/10/07/car-156309_1280.png"},
    {"model":"Ford Escape","price":22000,"mileage":30000,"image":"https://cdn.pixabay.com/photo/2012/05/29/00/43/car-49279_1280.jpg"},
]

def search_cars(query):
    try:
        url = "https://cars-by-api-ninjas.p.rapidapi.com/v1/cars"
        headers = {"X-RapidAPI-Key":"YOUR_KEY"}
        res = requests.get(url, headers=headers, params={"model":"toyota"})
        data = res.json()

        cars = []
        for item in data[:5]:
            cars.append({
                "model": item["model"],
                "price": 20000,
                "mileage": 40000,
                "image": fallback[0]["image"]
            })
        return cars
    except:
        return fallback

def price_analysis(cars):
    for c in cars:
        c["score"] = round(100 - (c["price"]/1000) - (c["mileage"]/2000),1)
    return cars
