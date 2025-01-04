import streamlit as st

# Streamlit UI

st.title("Power Calculator")
st.write("Enter a number to calculate its square, cube, and fourth power.")

# Get User Input

n = st.number_input("Enter an integer", value = 1, step =1)

# Calculate results

square = n**2
cube = n**3
fifth_power = n**4

# Display results

st.write(f"The sqaure of {n} is: {square}")
st.write(f"The cube of {n} is: {cube}")
st.write(f"The fifth power of {n} is: {fifth_power}")