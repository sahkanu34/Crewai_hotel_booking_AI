import streamlit as st
from crew_runner import run_crew

st.set_page_config(
    page_title="AI Hotel Booking Assistant",
    page_icon="🏨",
    layout="wide"
)

st.title("🏨 AI Hotel Booking Assistant")

st.markdown(
"""
Book hotels using a Multi-Agent CrewAI system powered by NVIDIA Llama 3.3 70B.
"""
)

with st.form("booking_form"):

    name = st.text_input("Customer Name")

    phone = st.text_input("Phone Number")

    destination = st.text_input("Destination")

    checkin = st.date_input("Check-in")

    checkout = st.date_input("Check-out")

    guests = st.number_input(
        "Guests",
        min_value=1,
        value=2
    )

    budget = st.number_input(
        "Budget per Night (USD)",
        min_value=20,
        value=120
    )

    hotel_type = st.selectbox(
        "Hotel Type",
        [
            "Luxury",
            "Budget",
            "Business",
            "Boutique",
            "Resort"
        ]
    )

    amenities = st.multiselect(
        "Amenities",
        [
            "Free WiFi",
            "Swimming Pool",
            "Breakfast",
            "Parking",
            "Gym",
            "Spa",
            "Lake View",
            "Airport Shuttle"
        ]
    )

    special = st.text_area(
        "Special Requests"
    )

    submit = st.form_submit_button("🔍 Find Hotels")


if submit:

    prompt = f"""
Customer Name: {name}

Phone Number: {phone}

Destination: {destination}

Check-in: {checkin}

Check-out: {checkout}

Guests: {guests}

Budget: {budget} USD/night

Hotel Type: {hotel_type}

Amenities:
{', '.join(amenities)}

Special Requests:
{special}

Please recommend the top 5 hotels and generate a professional booking confirmation.
"""

    with st.spinner("CrewAI is working..."):

        result = run_crew(prompt)

    st.success("Completed!")

    st.markdown("## Recommendation")

    st.code(result)