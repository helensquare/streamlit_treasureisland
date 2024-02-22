import streamlit as st

st.set_page_config(page_title="Treasure Island Game", page_icon="🏝️")

st.title("Welcome to Treasure Island!")

with st.form("beginning"):

    leftOrRight = st.selectbox(
        "Do you want to go left or right?", 
        ("Left", "Right"),
        index=None
        )
    
    beginningSubmit = st.form_submit_button(label="Submit")

    if beginningSubmit:
        if leftOrRight == "Left":
            st.write("You win!")
        else:
            st.write("You lose!")

# st.write(f"You decided to go {left_or_right}")

