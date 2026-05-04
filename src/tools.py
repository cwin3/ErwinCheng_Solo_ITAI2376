import pandas as pd
import streamlit as st
import os

@st.cache_data
def load_data():
    if not os.path.exists("data/cars.csv"):
        from generated_dataset import generate_dataset
        generate_dataset()

    df = pd.read_csv("data/cars.csv")

    df["model"] = df["manufacturer"] + " " + df["model"]
    df["mileage"] = df["odometer"]

    return df.to_dict(orient="records")

def filter_cars(cars, query, max_price, fuel):
    query = query.lower()
    results = []

    for c in cars:
        if c["price"] > max_price:
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
