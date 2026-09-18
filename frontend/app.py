import streamlit as st
import requests

def format_result(result):
    result = round(result, 2)

    if result.is_integer():
        result = int(result)

    return result

st.title("🧮 Calculator")

num1 = st.number_input("Enter first number")
num2 = st.number_input("Enter second number")

st.write("Choose an operation:")

col1, col2, col3, col4 = st.columns(4)

with col1:
    add = st.button("➕ Add")

    if add:
        response = requests.get(
            "http://127.0.0.1:8000/add",
            params={
                "num1": num1,
                "num2": num2
            }
        )

        data = response.json()
        result = format_result(data["result"])

        st.success(f"Result: {result}")

with col2:
    subtract = st.button("➖ Subtract")

    if subtract:
        response = requests.get(
            "http://127.0.0.1:8000/subtract",
            params={
                "num1": num1,
                "num2": num2
            }
        )

        data = response.json()
        result = format_result(data["result"])

        st.success(f"Result: {data['result']}")

with col3:
    multiply = st.button("✖️ Multiply")

    if multiply:
        response = requests.get(
            "http://127.0.0.1:8000/multiply",
            params={
                "num1": num1,
                "num2": num2
            }
        )

        data = response.json()
        result = format_result(data["result"])

        st.success(f"Result: {data['result']}")

with col4:
    divide = st.button("➗ Divide")

    if divide:
        response = requests.get(
            "http://127.0.0.1:8000/divide",
            params={
                "num1": num1,
                "num2": num2
            }
        )

        if response.status_code == 200:
            data = response.json()
            result = format_result(data["result"])

            st.success(f"Result: {result}")

        else:
            data = response.json()

            st.error(data["detail"])