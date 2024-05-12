import streamlit as st

def admin():
    
    if st.session_state.admin :
        st.write("admin")

    else :
        st.write("You have to login as admin to access this page ! ")
