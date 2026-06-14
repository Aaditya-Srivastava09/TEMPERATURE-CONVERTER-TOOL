import streamlit as st

st.title("🌡️ Temperature Conversion Tool")
st.markdown("---")

option = st.selectbox("Select Conversion Type", [
    "Celsius to Fahrenheit",
    "Celsius to Kelvin",
    "Fahrenheit to Celsius",
    "Kelvin to Celsius"
])

if option == "Celsius to Fahrenheit":
    c = st.number_input("Enter temperature in Celsius", value=0.0)
    if st.button("Convert"):
        f = (c * 1.8) + 32
        st.success(f"The corresponding temperature in Fahrenheit is: **{f:.2f} °F**")

elif option == "Celsius to Kelvin":
    c = st.number_input("Enter temperature in Celsius", value=0.0)
    if st.button("Convert"):
        k = 273 + c
        st.success(f"The corresponding temperature in Kelvin is: **{k:.2f} K**")

elif option == "Fahrenheit to Celsius":
    f = st.number_input("Enter temperature in Fahrenheit", value=32.0)
    if st.button("Convert"):
        c = (f - 32) * (5 / 9)
        st.success(f"The corresponding temperature in Celsius is: **{c:.2f} °C**")

elif option == "Kelvin to Celsius":
    k = st.number_input("Enter temperature in Kelvin", value=273.0)
    if st.button("Convert"):
        c = k - 273
        st.success(f"The corresponding temperature in Celsius is: **{c:.2f} °C**")