import streamlit as st

st.title("Hello streamlit app")
st.subheader("Brewed with streamlit")
st.text("Welcome to your first ineteractive app")
st.write("Choose your fav. variety of streamlit")

chai = st.selectbox("Your fav chai:", ["Masala chai",
                                       "Lemon Tea",
                                       "Kesar chai",
                                       "Adark chai",
                                       "paan chai"])

st.write(f"You choose {chai}. Excellent chai")

st.success("Your chai has been brewed")