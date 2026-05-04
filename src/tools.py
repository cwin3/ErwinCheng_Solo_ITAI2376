import pandas as pd
import streamlit as st
import os
import ast

@st.cache_data
def load_data():
    if not os.path.exists("data/cars.csv"):
        from generated_dataset import generate_dataset
        generate_dataset()

    df = pd.read_csv("data/cars.csv")

    # ---------- IMAGE FALLBACK ----------
    if "images" in df.columns:
        df["images"] = df["images"].apply(ast.literal_eval)
    elif "image" in df.columns:
        df["images"] = df["image"].apply(lambda x: [x])
    else:
        df["images"] = [["https://cdn.pixabay.com/photo/2012/05/29/00/43/car-49278_1280.jpg"]] * len(df)

    # ---------- DEALER LOGO FALLBACK ----------
    if "dealer_logo" not in df.columns:
        df["dealer_logo"] = "https://cdn-icons-png.flaticon.com/512/743/743007.png"

    df["model"] = df["manufacturer"] + " " + df["model"]
    df["mileage"] = df["odometer"]

    return df.to_dict(orient="records")

def filter_cars(cars, query, max_price, fuel, brand=None, model=None):
    query = query.lower()

    results = []

    for c in cars:
        if c["price"] > max_price:
            continue

        if brand and brand != "All" and c["manufacturer"] != brand:
            continue

        if model and model != "All" and c["model"] != model:
            continue

        if query and query not in c["model"].lower():
            continue

        if fuel != "Any" and c["fuel"] != fuel:
            continue

        results.append(c)

    return results

def analyze_cars(cars):
    for c in cars:
        score = 100 - (c["price"]/1000) - (c["mileage"]/2000)

        if c["listing_type"] == "great_deal":
            score += 15
        elif c["listing_type"] == "overpriced":
            score -= 15
        elif c["listing_type"] == "fraud":
            score -= 40

        c["score"] = round(score, 1)
        c["is_suspicious"] = c["listing_type"] == "fraud"

    return cars
