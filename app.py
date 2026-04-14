import streamlit as st

# Title
st.title("Simple Calculator NEW ")

# User Inputs
num1 = st.number_input("Enter Third Number", value=0.0)
num2 = st.number_input("Enter Second Number", value=0.0)

# Operation Selection
operation = st.selectbox(
    "Select Operation",
    ("Addition", "Subtraction", "Multiplication", "Division")
)

# Calculation
if st.button("Calculate"):
    if operation == "Addition":
        result = num1 + num2
    elif operation == "Subtraction":
        result = num1 - num2
    elif operation == "Multiplication":
        result = num1 * num2
    elif operation == "Division":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error! Division by zero."

    st.success(f"Result: {result}")
