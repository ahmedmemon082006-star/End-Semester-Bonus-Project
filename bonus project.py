import streamlit as st
# Functions for performing arithemetic operations.+
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b == 0:
        raise ZeroDivisionError("Division by zero not possible")
    return a/b
def calculate_input(a,b,Operation):
    if Operation == "add":
        return add(a,b)
    elif Operation == "subtract":
        return subtract(a,b)
    elif Operation == "multiply":
        return multiply(a,b)
    elif Operation == "divide":
        return divide(a,b)
#________________ Starting to program with streamlit ________________

st.set_page_config(page_title = "The Calculator App" , page_icon= "🔢")
st.title("🔢 The Calculator Application. ")
st.write("Description: The Calculator performs only basic arithemetic operations. This page is generated through streamlit and python.")
st.write("Made by Ahmed Memon. ID: 2540194")
num1 = st.number_input("Enter a valid first number:", format="%.3f")
num2 = st.number_input("Enter a valid second number:", format="%.3f")
operator = st.selectbox(
    "Please select an opeartor from the following options: ",
    ("add","subtract","multiply","divide")
)
if st.button("Calculate"):
    try:
        st.header("Calculator")
        output = calculate_input(num1 , num2 , operator)
        st.success(output)
    except ZeroDivisionError as error:
        st.error(error)
    except Exception:




# Here is the link for the calculator made above: https://am2540194calculators.streamlit.app/






      
        st.error("Invalid Input")
