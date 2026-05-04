import streamlit as st
from src.tools import load_data, filter_cars, analyze_cars
from src.ollama_agent import ask_ollama
import pandas as pd

st.set_page_config(layout="wide")

# ---------- STYLE ----------
st.markdown("""
<style>
.card {background:white;border-radius:18px;padding:20px;margin-bottom:20px;}
.price {font-size:26px;font-weight:700;}
.subtle {color:#777;}
</style>
""", unsafe_allow_html=True)

st.title("🚗 Find Your Next Car")

# ---------- LOAD DATA ----------
cars_data = load_data()

# ---------- BRAND / MODEL ----------
brands = sorted(list(set([c["manufacturer"] for c in cars_data])))

models_by_brand = {}
for c in cars_data:
    models_by_brand.setdefault(c["manufacturer"], set()).add(c["model"])

for k in models_by_brand:
    models_by_brand[k] = sorted(list(models_by_brand[k]))

# ---------- FILTER UI ----------
col1, col2, col3, col4 = st.columns(4)

with col1:
    selected_brand = st.selectbox("Brand", ["All"] + brands)

with col2:
    if selected_brand != "All":
        model_options = models_by_brand[selected_brand]
    else:
        model_options = sorted(set([c["model"] for c in cars_data]))

    selected_model = st.selectbox("Model", ["All"] + model_options)

with col3:
    budget = st.slider("Max Price", 5000, 80000, 25000)

with col4:
    fuel = st.selectbox("Fuel", ["Any","gas","hybrid","electric"])

query = st.text_input("Search cars (optional)")

cars = []

# ---------- FILTER ----------
if query or selected_brand != "All" or selected_model != "All":
    cars = filter_cars(
        cars_data,
        query,
        budget,
        fuel,
        brand=selected_brand,
        model=selected_model
    )

    cars = analyze_cars(cars)

    cols = st.columns(3)

    for i, c in enumerate(cars[:9]):
        with cols[i % 3]:

            # SAFE IMAGE HANDLING
            image = c.get("images", ["https://cdn.pixabay.com/photo/2012/05/29/00/43/car-49278_1280.jpg"])

            if isinstance(image, list) and len(image) > 0:
                st.image(image[0], use_container_width=True)
            else:
                st.image("https://cdn.pixabay.com/photo/2012/05/29/00/43/car-49278_1280.jpg", use_container_width=True)

            st.markdown(f"### {c['model']} {c['year']}")
            st.markdown(f"<div class='price'>${c['price']:,}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='subtle'>{c['mileage']:,} miles • {c['fuel']}</div>", unsafe_allow_html=True)

            st.image(c["dealer_logo"], width=80)
            st.caption(c["dealer"])

            if c["is_suspicious"]:
                st.error("⚠️ Suspicious Listing")
            elif c["score"] > 70:
                st.success("🔥 Excellent Deal")
            elif c["score"] > 50:
                st.info("👍 Good Deal")
            else:
                st.warning("💸 Overpriced")

# ---------- INSIGHTS ----------
if cars:
    df = pd.DataFrame(cars)
    st.write("Average Price:", int(df["price"].mean()))

# ---------- AI ----------
st.markdown("### 🤖 AI Insights")

chat = st.text_input("Ask AI about cars")

if chat:
    st.info(ask_ollama(chat))
