import streamlit as st
from src.tools import load_data, filter_cars, analyze_cars
from src.ollama_agent import ask_ollama
import pandas as pd

st.set_page_config(layout="wide")

st.markdown("""
<style>
.card {background:white;border-radius:18px;padding:20px;margin-bottom:20px;}
.price {font-size:26px;font-weight:700;}
.subtle {color:#777;}
</style>
""", unsafe_allow_html=True)

st.title("Find Your Next Car")

cars_data = load_data()

col1,col2,col3 = st.columns(3)
with col1:
    budget = st.slider("Max Price",5000,80000,25000)
with col2:
    fuel = st.selectbox("Fuel",["Any","gas","hybrid","electric"])
with col3:
    sort_by = st.selectbox("Sort",["Best","Cheapest","Newest"])

query = st.text_input("Search cars")

cars=[]

if query:
    cars = analyze_cars(filter_cars(cars_data,query,budget,fuel))

    if sort_by=="Best":
        cars.sort(key=lambda x:x["score"],reverse=True)
    elif sort_by=="Cheapest":
        cars.sort(key=lambda x:x["price"])
    else:
        cars.sort(key=lambda x:x["year"],reverse=True)

    cols = st.columns(3)

    for i,c in enumerate(cars[:9]):
        with cols[i%3]:
            st.image(c["images"][0], use_container_width=True)
            st.markdown(f"### {c['model']} {c['year']}")
            st.markdown(f"<div class='price'>${c['price']:,}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='subtle'>{c['mileage']:,} miles</div>", unsafe_allow_html=True)
            st.image(c["dealer_logo"], width=80)

if query and cars:
    df=pd.DataFrame(cars)
    st.write("Avg Price:",int(df["price"].mean()))

st.markdown("### AI Insights")
chat=st.text_input("Ask AI")

if chat:
    st.info(ask_ollama(chat))
