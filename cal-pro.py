import streamlit as st

# Function to perform calculation
def calculate(operation, num1, num2):
    if operation == 'Add':
        return num1 + num2
    elif operation == 'Subtract':
        return num1 - num2
    elif operation == 'Multiply':
        return num1 * num2
    elif operation == 'Divide':
        if num2 == 0:
            return "Cannot divide by zero"
        return num1 / num2

# Streamlit UI
st.title("Simple Calculator")

# User input for numbers
num1 = st.number_input("Enter first number", format="%.2f")
num2 = st.number_input("Enter second number", format="%.2f")

# Dropdown for operation selection
operation = st.selectbox("Select Operation", ['Add', 'Subtract', 'Multiply', 'Divide'])

# Calculate button
if st.button("Calculate"):
    result = calculate(operation, num1, num2)
    st.write(f"Result: {result}")
