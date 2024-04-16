import streamlit as st
import pyrebase

firebaseconfig = {
            'apiKey': "AIzaSyAyZy7muAWri-zIstiP3SOKEgpOLLxT4wY",
            'authDomain': "carbon-footprint-calcula-a2259.firebaseapp.com",
            'projectId': "carbon-footprint-calcula-a2259",
            'databaseURL':"https://carbon-footprint-calcula-a2259-default-rtdb.asia-southeast1.firebasedatabase.app/",
            'storageBucket': "carbon-footprint-calcula-a2259.appspot.com",
            'messagingSenderId': "895459444452",
            'appId': "1:895459444452:web:c86a6c6ad143ded0750ef1"
}

firebase = pyrebase.initialize_app(firebaseconfig)
auth = firebase.auth()

def app():
    st.title(':green[ Carbon Footprint Calculator🍃]')

    choice = st.radio('Login/Sign-Up', ['Login', 'Sign-Up'], captions=['Existing user', 'New user'], index=0,horizontal=True)

    if choice == 'Login':
        email = st.text_input('Email Address')
        password = st.text_input('Password', type='password')

        if st.button("Login"):
            try:
                user = auth.sign_in_with_email_and_password(email, password)
                st.success("User logged in successfully!")
                
                # Redirect or perform further actions after successful login
            except Exception as e:
                st.warning('Login failed. Please enter valid email and password.')
                st.error(str(e))

    else:
        email = st.text_input('Email Address')
        username = st.text_input('Username')
        password = st.text_input('Password', type='password')

        if st.button("Create My Account"):
            try:
                user = auth.create_user_with_email_and_password(email, password)
                st.success("Account created successfully")
                st.markdown("Please login using username and password")
                st.balloons()
            except Exception as e:
                st.warning("Account creation failed.")
                st.error(str(e))

app()
