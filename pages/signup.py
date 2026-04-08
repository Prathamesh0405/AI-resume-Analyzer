import streamlit as st
from auth import signup

# 🚫 Hide sidebar ONLY here
st.set_page_config(page_title="Signup", initial_sidebar_state="collapsed")

st.markdown("""
<style>
[data-testid="stSidebar"] {display: none;}
[data-testid="stSidebarNav"] {display: none;}
</style>
""", unsafe_allow_html=True)

st.title("📝 Signup")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Register"):
    if username and password:
        result = signup(username, password)

        if result == "exists":
            st.warning("User already exists! Try login.")
        else:
            st.success("Account created successfully!")
            st.info("Go to Login page")

    else:
        st.error("Fill all fields")

st.markdown("---")

if st.button("Go to Login"):
    st.switch_page("pages/login.py")