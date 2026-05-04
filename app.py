import streamlit as st
from src.tools import load_data, filter_cars, analyze_cars
from src.ollama_agent import ask_ollama
import pandas as pd

st.set_page_config(page_title="Car Finder", layout="wide")

st.title("🚗 Smart Car Finder")

if "favorites" not in st.session_state:
    st.session_state.favorites = []

cars_data = load_data()

# Sidebar
st.sidebar.header("Filters")
budget = st.sidebar.slider("Max Price", 5000, 80000, 25000)
fuel = st.sidebar.selectbox("Fuel Type", ["Any","gas","hybrid","electric"])
sort_by = st.sidebar.radio("Sort By", ["Best","Cheapest","Newest"])

query = st.text_input("Search cars (Toyota, BMW, SUV...)")

cars = []

if query:
    cars = filter_cars(cars_data, query, budget, fuel)
    cars = analyze_cars(cars)

    if sort_by == "Best":
        cars.sort(key=lambda x: x["score"], reverse=True)
    elif sort_by == "Cheapest":
        cars.sort(key=lambda x: x["price"])
    else:
        cars.sort(key=lambda x: x["year"], reverse=True)

    st.subheader("Results")
    cols = st.columns(3)

    for i, c in enumerate(cars[:9]):
        with cols[i % 3]:
            st.image(c["image"])
            st.write(f"**{c['model']} ({c['year']})**")
            st.write(f"${c['price']:,}")
            st.write(f"{c['mileage']:,} miles")
            st.write(c["dealer"])

            if c["is_suspicious"]:
                st.error("⚠️ Suspicious listing")
            elif c["score"] > 70:
                st.success(f"🔥 Excellent Deal ({c['score']})")
            elif c["score"] > 50:
                st.warning(f"👍 Good Deal ({c['score']})")
            else:
                st.warning(f"💸 Overpriced ({c['score']})")

            if st.button("❤️ Save", key=f"save_{i}"):
                st.session_state.favorites.append(c)

# Compare
st.markdown("---")
st.subheader("Compare")

if len(st.session_state.favorites) >= 2:
    cols = st.columns(len(st.session_state.favorites[:3]))
    for i, c in enumerate(st.session_state.favorites[:3]):
        with cols[i]:
            st.image(c["image"])
            st.write(c["model"])
            st.write(f"${c['price']:,}")

# AI Assistant
st.markdown("---")
st.subheader("Ask AI")

chat = st.text_input("Ask about cars...")

if chat:
    st.write(ask_ollama(chat))

# Insights
if query and len(cars) > 0:
    df = pd.DataFrame(cars)
    st.subheader("Market Insights")
    st.write("Average Price:", int(df["price"].mean()))
