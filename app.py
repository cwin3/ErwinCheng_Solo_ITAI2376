import streamlit as st
from src.agent import agent
from src.tools import search_cars, price_analysis

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="Car Finder", layout="wide")

# ---------- LOGIN ----------
USERS = {"erwin": "1234"}

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.title("🔐 Login")
    user = st.text_input("Username")
    pwd = st.text_input("Password", type="password")

    if st.button("Login"):
        if USERS.get(user) == pwd:
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("Invalid login")
    st.stop()

# ---------- STATE ----------
if "favorites" not in st.session_state:
    st.session_state.favorites = []

# ---------- STYLE ----------
st.markdown("""
<style>
.card {
    background:white;
    padding:15px;
    border-radius:12px;
    border:1px solid #ddd;
}
.card:hover {box-shadow:0 4px 15px rgba(0,0,0,0.1);}
</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown("<h1 style='text-align:center;'>🚗 Car Finder</h1>", unsafe_allow_html=True)

# ---------- SIDEBAR ----------
st.sidebar.title("Filters")
budget = st.sidebar.slider("Max Price", 5000, 50000, 20000)
sort_by = st.sidebar.radio("Sort By", ["Best Deal", "Cheapest", "Newest"])

st.sidebar.markdown("## ❤️ Favorites")
for fav in st.session_state.favorites:
    st.sidebar.write(f"{fav['model']} - ${fav['price']}")

# ---------- SEARCH ----------
query = st.text_input("Search cars (e.g. SUV under 20k)")

if query:
    cars = search_cars(query)
    cars = price_analysis(cars)

    # Filter
    cars = [c for c in cars if c["price"] <= budget]

    # Sort
    if sort_by == "Best Deal":
        cars.sort(key=lambda x: x["score"], reverse=True)
    elif sort_by == "Cheapest":
        cars.sort(key=lambda x: x["price"])
    else:
        cars.sort(key=lambda x: x["mileage"])

    st.markdown("## 🚗 Results")

    cols = st.columns(3)

    for i, car in enumerate(cars[:6]):
        with cols[i % 3]:
            st.markdown("<div class='card'>", unsafe_allow_html=True)
            st.image(car["image"], use_container_width=True)
            st.markdown(f"### {car['model']}")
            st.write(f"${car['price']}")
            st.write(f"{car['mileage']} miles")

            score = car["score"]
            if score > 70:
                st.success(f"Excellent Deal ({score})")
            elif score > 50:
                st.warning(f"Good Deal ({score})")
            else:
                st.error(f"Overpriced ({score})")

            if st.button("❤️ Save", key=f"save{i}"):
                st.session_state.favorites.append(car)

            st.markdown("</div>", unsafe_allow_html=True)

# ---------- COMPARE ----------
st.markdown("---")
st.markdown("## ⚖️ Compare")

if len(st.session_state.favorites) >= 2:
    cols = st.columns(len(st.session_state.favorites[:3]))
    for i, car in enumerate(st.session_state.favorites[:3]):
        with cols[i]:
            st.image(car["image"])
            st.write(car["model"])
            st.write(f"${car['price']}")
            st.write(f"{car['mileage']} miles")
            st.write(f"Score: {car.get('score')}")
else:
    st.info("Add at least 2 favorites to compare")

# ---------- CHAT ----------
st.markdown("---")
st.markdown("## 💬 Ask AI")

chat = st.text_input("Ask about cars...")

if chat:
    with st.spinner("Thinking..."):
        response = agent.run(chat)
    st.write(response)
