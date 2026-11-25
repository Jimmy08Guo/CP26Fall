import streamlit as st
import random
from collections import Counter

st.set_page_config(page_title="Number Mastermind", page_icon="🟢")

# Green page background
st.markdown("""
<style>
.stApp {
    background-color: #bdf5c4;
}
.game-title {
    text-align: center;
    color: #145a32;
}
.circle {
    width: 58px;
    height: 58px;
    border-radius: 50%;
    display: inline-flex;
    justify-content: center;
    align-items: center;
    margin: 6px;
    color: white;
    font-size: 28px;
    font-weight: bold;
}
.feedback {
    font-size: 22px;
    letter-spacing: 4px;
}
</style>
""", unsafe_allow_html=True)

# Colour for each number
colours = {
    1: "#27d84d",  # green
    2: "#d83df0",  # purple
    3: "#2e68f5",  # blue
    4: "#ffc52e",  # yellow
    5: "#f00000",  # red
    6: "#ffffff"   # white
}

def make_circle(number):
    text_colour = "black" if number == 6 else "white"
    border = "3px solid #d8d8f0" if number == 6 else "none"

    return f"""
    <span class="circle"
          style="background:{colours[number]};
                 color:{text_colour};
                 border:{border};">
        {number}
    </span>
    """

def check_guess(secret, guess):
    exact = sum(a == b for a, b in zip(secret, guess))
    total_correct = sum((Counter(secret) & Counter(guess)).values())
    correct_wrong_place = total_correct - exact
    return exact, correct_wrong_place

# Start the game
if "secret" not in st.session_state:
    st.session_state.secret = random.sample(range(1, 7), 4)
    st.session_state.history = []

st.markdown("<h1 class='game-title'>Number Mastermind</h1>", unsafe_allow_html=True)
st.write("Choose four numbers. Try to guess the hidden pattern!")

# Choose numbers
with st.form("guess_form"):
    columns = st.columns(4)
    guess = []

    for i, column in enumerate(columns):
        with column:
            guess.append(
                st.selectbox(
                    f"Number {i + 1}",
                    [1, 2, 3, 4, 5, 6],
                    key=f"number_{i}"
                )
            )

    submitted = st.form_submit_button("Check my answer")

if submitted:
    exact, wrong_place = check_guess(st.session_state.secret, guess)
    st.session_state.history.insert(0, (guess, exact, wrong_place))

    if exact == 4:
        st.balloons()
        st.success("You won! You guessed all four numbers correctly.")

# Show guesses
for guess, exact, wrong_place in st.session_state.history:
    number_html = "".join(make_circle(number) for number in guess)

    feedback = "🟢" * exact + "🟠" * wrong_place
    feedback += "⚪" * (4 - exact - wrong_place)

    st.markdown(
        f"""
        <div style="background:white; padding:12px; border-radius:15px;
                    margin:10px 0; text-align:center;">
            {number_html}
            <div class="feedback">{feedback}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

if st.button("↻ New Game"):
    st.session_state.secret = random.sample(range(1, 7), 4)
    st.session_state.history = []
    st.rerun()

st.caption("🟢 = correct number in the correct spot | 🟠 = correct number in the wrong spot")
