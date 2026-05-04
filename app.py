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
brands = sorted(list(set([c.get("manufacturer", "") for c in cars_data if c.get("manufacturer")])))

models_by_brand = {}
for c in cars_data:
    brand = c.get("manufacturer")
    model = c.get("model")
    if brand and model:
        models_by_brand.setdefault(brand, set()).add(model)

for k in models_by_brand:
    models_by_brand[k] = sorted(list(models_by_brand[k]))

# ---------- FILTER UI ----------
col1, col2, col3, col4 = st.columns(4)

with col1:
    selected_brand = st.selectbox("Brand", ["All"] + brands)

with col2:
    if selected_brand != "All":
        model_options = models_by_brand.get(selected_brand, [])
    else:
        model_options = sorted(set([c.get("model", "") for c in cars_data if c.get("model")]))

    selected_model = st.selectbox("Model", ["All"] + model_options)

with col3:
    budget = st.slider("Max Price", 5000, 80000, 25000)

with col4:
    fuel = st.selectbox("Fuel", ["Any","gas","hybrid","electric"])

query = st.text_input("Search cars (optional)")

# ---------- SEARCH STATE ----------
if "search_clicked" not in st.session_state:
    st.session_state.search_clicked = False

colA, colB = st.columns([1, 1])

with colA:
    if st.button("🔍 Search"):
        st.session_state.search_clicked = True

with colB:
    if st.button("❌ Reset"):
        st.session_state.search_clicked = False
        st.rerun()

cars = []

# ---------- FILTER ----------
if st.session_state.search_clicked:
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

            # ✅ GENERIC SAFE IMAGE
            st.image(
                "https://cdn.pixabay.com/photo/2012/05/29/00/43/car-49278_1280.jpg",
                use_container_width=True
            )

            # ---------- TEXT ----------
            st.markdown(f"### {c.get('model','Unknown')} {c.get('year','')}")
            st.markdown(f"<div class='price'>${c.get('price',0):,}</div>", unsafe_allow_html=True)
            st.markdown(
                f"<div class='subtle'>{c.get('mileage',0):,} miles • {c.get('fuel','')}",
                unsafe_allow_html=True
            )

            # ---------- DEALER ----------
            dealer_logo = c.get("dealer_logo")

            if isinstance(dealer_logo, str) and dealer_logo.startswith("http"):
                st.image(dealer_logo, width=80)
            else:
                st.image("https://cdn-icons-png.flaticon.com/512/743/743007.png", width=80)

            st.caption(c.get("dealer","Unknown Dealer"))

            # ---------- DEAL STATUS ----------
            if c.get("is_suspicious"):
                st.error("⚠️ Suspicious Listing")
            elif c.get("score", 0) > 70:
                st.success("🔥 Excellent Deal")
            elif c.get("score", 0) > 50:
                st.info("👍 Good Deal")
            else:
                st.warning("💸 Overpriced")

# ---------- INSIGHTS ----------
if cars:
    df = pd.DataFrame(cars)
    if "price" in df.columns:
        st.write("Average Price:", int(df["price"].mean()))

# ---------- AI ----------
st.markdown("### 🤖 AI Insights")

chat = st.text_input("Ask AI about cars")

if chat:
    st.info(ask_ollama(chat))
