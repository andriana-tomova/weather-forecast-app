import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather forecast for the next days.")
place = st.text_input("Places: ")
days = st.slider("Forecast days:", min_value=1, max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

dates = ["2022-10-10", "2022-11-10", "2022-12-10"]
temperatures = [12, 15, 17]

# t, d = get_data(temperatures, dates, kind)

figure = px.line(x=dates, y=temperatures, labels={"x":"Date", "y":"Temperature(C)"})
st.plotly_chart(figure)

