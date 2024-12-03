import streamlit as st

# Set the title of the app
st.title("Simple Streamlit App")

# Add a text input widget
name = st.text_input("Enter your name:")

# Add a button to trigger an action
if st.button("Greet Me"):
    if name:
        st.write(f"Hello, {name}! 👋")
    else:
        st.write("Hello! Please enter your name above.")
