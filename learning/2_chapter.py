import streamlit as st

st.title("Chai Maker App")

if st.button("Make Chai"):
    st.success("Your chai is being Brewed")
    
add_masala = st.checkbox("Add Masala")

if add_masala:
    st.write("Masala added to your chai")
    
tea_type = st.radio("Pick your chai base: ",["Milk", "water", "Almond milk"])
st.write(f"Selected Base {tea_type}")

flavour = st.selectbox("Choose flavour: ", ["Adarak", "tulsi", "green tea"])
st.write(f"Selected Flavour: {flavour}")

sugar = st.slider("Sugar Level",0, 3, 1)

st.number_input("how many cups", min_value=1, max_value=20, step=1)

name = st.text_input("Enter Your Name")

if name:
    st.write(f"Welcome {name} your chai is on the way")
    
dob = st.date_input(f"Select your D.O.B")
st.write(f"You are ")