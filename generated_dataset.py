import pandas as pd
import random
import uuid
import string
import os

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

def generate_vin():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=17))

def generate_dataset(n=10000):
    data = []

    for _ in range(n):
        brand = random.choice(list(brands_models))
        model = random.choice(brands_models[brand])
        year = random.randint(2010, 2023)

        price = random.randint(12000, 60000)
        mileage = random.randint(5000, 120000)

        listing_type = random.choices(
            ["normal","great_deal","overpriced","fraud"],
            weights=[0.7,0.1,0.1,0.1]
        )[0]

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
            "transmission": random.choice(["automatic","manual"]),
            "dealer": random.choice(dealers),
            "city": city,
            "state": state,
            "listing_type": listing_type,
            "image": "https://cdn.pixabay.com/photo/2012/05/29/00/43/car-49278_1280.jpg"
        })

    df = pd.DataFrame(data)
    df.to_csv("data/cars.csv", index=False)

generate_dataset()
print("Dataset generated successfully.")
