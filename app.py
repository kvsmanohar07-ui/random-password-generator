import streamlit as st
import random
import string

st.title("Random Password Generator")
st.write("Made by K.V.S. Manohar Reddy | OASIS INFOBYTE - Task 3")

length = st.slider("Select Password Length:", min_value=4, max_value=32, value=12)

include_letters = st.checkbox("Include Letters (a-z, A-Z)", value=True)
include_numbers = st.checkbox("Include Numbers (0-9)", value=True)
include_symbols = st.checkbox("Include Symbols (!@#$)", value=True)

if st.button("Generate Password"):
    characters = ""
    if include_letters:
        characters += string.ascii_letters
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    if not characters:
        st.error("Please select at least one option!")
    else:
        password = "".join(random.choice(characters) for _ in range(length))
        st.success(f"Your Password: {password}")
        st.write(f"Length: {length} characters")
        st.code(password)
