import streamlit as st
from auth import login

# 🚫 Hide sidebar ONLY here
st.set_page_config(page_title="Login", initial_sidebar_state="collapsed")

st.markdown("""
<style>
[data-testid="stSidebar"] {display: none;}
[data-testid="stSidebarNav"] {display: none;}
</style>
""", unsafe_allow_html=True)

st.title("🔐 Login")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    user = login(username, password)
    if user:
        st.session_state.user = username
        st.success("Login successful!")
        st.switch_page("app.py")
    else:
        st.error("Invalid username or password")

st.markdown("---")

if st.button("Create new account"):
    st.switch_page("pages/signup.py")