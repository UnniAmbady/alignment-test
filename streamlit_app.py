import streamlit as st

st.title("🎈 Aligh=nment Test")


# Configure the page for a cleaner, wider look
st.set_page_config(layout="wide", page_title="Streamlit Button Layout")

st.title("Streamlit Layout Example")
st.markdown("---")

# --- First Row: Start Button and Instruction Text (on the same line) ---
st.subheader("Row 1: Button and Text on the Same Line")

# Updated column ratio to [0.5, 0.5]. This creates two equal-width columns.
# This is functionally equivalent to st.columns([1, 1]).
col_start_button, col_start_text = st.columns([0.5, 0.5])

with col_start_button:
    # 1. Start Button
    start_pressed = st.button("Start", type="primary")

with col_start_text:
    # 2. Instruction Text, using st.text to maintain alignment
    st.text("<<- Press Start")


# --- Second Row: Test and Speak Buttons (close together, left-aligned) ---
st.markdown("---")
st.subheader("Row 2: Two Buttons Close Together")

# Use three columns: [1, 1, 4]. The first two columns hold the buttons, 
# and the larger third column acts as a spacer, pushing the buttons to the left.
col_test, col_speak, col_spacer = st.columns([1, 1, 4])

with col_test:
    # 3. Test Button
    test_pressed = st.button("Test")

with col_speak:
    # 4. Speak Button
    speak_pressed = st.button("Speak")

# --- Placeholder Logic for Demonstration ---
st.markdown("---")
st.subheader("Interaction Output:")

if start_pressed:
    st.success("✅ Start button pressed! Initialization logic goes here.")
if test_pressed:
    st.info("ℹ️ Test button pressed! Running tests...")
if speak_pressed:
    st.warning("🔊 Speak button pressed! Ready to synthesize audio.")

if not (start_pressed or test_pressed or speak_pressed):
    st.text("Press any button to see the action.")
