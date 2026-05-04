import pandas as pd
import random
import uuid
import string
import os

def generate_vin():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=17))

def get_car_images(brand, model):
    base = f"https://source.unsplash.com/featured/?{brand},{model},car"
    return [
        base,
        f"https://source.unsplash.com/featured/?{brand},{model},interior",
        f"https://source.unsplash.com/featured/?{brand},{model},dashboard"
    ]

def get_dealer_logo(dealer):
    logos = {
        "CarMax": "https://upload.wikimedia.org/wikipedia/commons/4/4b/CarMax_Logo.png",
        "AutoNation": "https://upload.wikimedia.org/wikipedia/commons/3/3b/AutoNation_logo.svg",
        "DriveTime": "https://upload.wikimedia.org/wikipedia/commons/5/5c/DriveTime_logo.png",
        "Elite Motors": "https://cdn-icons-png.flaticon.com/512/743/743007.png"
    }
    return logos.get(dealer, logos["CarMax"])

def generate_dataset(n=10000):
    os.makedirs("data", exist_ok=True)

    brands_models = {
        "Toyota": ["Camry", "Corolla", "RAV4"],
        "Honda": ["Civic", "Accord", "CR-V"],
        "Ford": ["F-150", "Escape", "Explorer"],
        "BMW": ["3 Series", "5 Series", "X5"],
        "Mercedes-Benz": ["C-Class", "E-Class", "GLE"]
    }

    dealers = ["CarMax", "AutoNation", "DriveTime", "Elite Motors"]
    cities = [("Houston","TX"),("Los Angeles","CA"),("Chicago","IL"),("New York","NY")]

    data = []

    for _ in range(n):
        brand = random.choice(list(brands_models))
        model = random.choice(brands_models[brand])
        dealer = random.choice(dealers)

        year = random.randint(2010, 2023)
        price = random.randint(12000, 60000)
        mileage = random.randint(5000, 120000)

        listing_type = random.choice(["normal","great_deal","overpriced","fraud"])

        if listing_type == "great_deal":
            price *= 0.7
        elif listing_type == "overpriced":
            price *= 1.4
        elif listing_type == "fraud":
            price *= 0.3

        city, state = random.choice(cities)

        data.append({
            "id": str(uuid.uuid4()),
            "vin": generate_vin(),
            "manufacturer": brand,
            "model": model,
            "year": year,
            "price": int(price),
            "odometer": mileage,
            "fuel": random.choice(["gas","hybrid","electric"]),
            "dealer": dealer,
            "dealer_logo": get_dealer_logo(dealer),
            "city": city,
            "state": state,
            "listing_type": listing_type,
            "images": get_car_images(brand, model)
        })

    pd.DataFrame(data).to_csv("data/cars.csv", index=False)

if __name__ == "__main__":
    generate_dataset()
