import streamlit as st
import plotly.express as px
from backend import get_data

# Add title, text input, slider, selectbox and subheader
st.title("Weather forecast for the next days.")
place = st.text_input("Places: ")
days = st.slider("Forecast days:", min_value=1, max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

# get the temperature/sky data
if place:
    filtered_data = get_data(place, days)
    if option == "Temperature":
        temperatures = [dict["main"]["temp"] for dict in filtered_data]
        dates = [dict["dt_txt"] for dict in filtered_data]
        # Create a temperature plot
        figure = px.line(x=dates, y=temperatures, labels={"x":"Dates",
                                                          "y":"Temperature(C)"})
        st.plotly_chart(figure)
    if option == "Sky":
        sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
        images = {"Clear":"images/clear.png", "Clouds":"images/cloud.png",
                  "Rain":"images/rain.png", "Snow":"images/snow.png"}
        image_paths = [images[condition] for condition in sky_conditions]
        st.image(image_paths, width=100)

