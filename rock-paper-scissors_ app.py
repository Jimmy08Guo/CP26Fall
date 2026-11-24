import streamlit as st
import random

st.title("Rock, Paper, Scissors")

choices = ["Rock", "Paper", "Scissors"]

images = {
    "Rock": "rock.png",
    "Paper": "paper.png",
    "Scissors": "scissors.png"
}

def winner(player, computer):
    if player == computer:
        return "It's a tie!"
    if (
        (player == "Rock" and computer == "Scissors")
        or (player == "Paper" and computer == "Rock")
        or (player == "Scissors" and computer == "Paper")
    ):
        return "You win!"
    return "Computer wins!"

st.write("Choose one:")

columns = st.columns(3)

for i, choice in enumerate(choices):
    with columns[i]:
        st.image(images[choice], width=120)
        if st.button(choice, use_container_width=True):
            computer_choice = random.choice(choices)

            st.write(f"You chose: **{choice}**")
            st.write(f"Computer chose: **{computer_choice}**")
            st.success(winner(choice, computer_choice))
