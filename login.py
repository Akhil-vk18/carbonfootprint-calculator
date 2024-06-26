import streamlit as st
import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
from firebase_admin import auth
import json
import requests

# Check if the Firebase app has already been initialized
if not firebase_admin._apps:
    # Initialize the Firebase app with a unique name
    cred = credentials.Certificate(r"C:\Users\akhil\Desktop\snm\python code\mini\carbonfootprint calculator\carbon-footprint-calcula-a2259-firebase-adminsdk-qn2fb-65cf54671d.json")
    firebase_admin.initialize_app(cred,name='my-firebase-app-1')

def is_admin():
    """Check if the current user is an admin."""
    user = firebase_admin.auth.get_user_by_email(st.session_state.useremail)
    if user and 'admin' in user.custom_claims:
        return True
    return False

def login():
    st.title('Carbon Footprint Calculator')

    if 'username' not in st.session_state:
        st.session_state.username = ''
    if 'useremail' not in st.session_state:
        st.session_state.useremail = ''
    if 'admin' not in st.session_state:
        st.session_state.admin=False

    def sign_up_with_email_and_password(email, password, username=None, return_secure_token=True):
        try:
            rest_api_url = "https://identitytoolkit.googleapis.com/v1/accounts:signUp"
            payload = {
                "email": email,
              "password": password,
                "returnSecureToken": return_secure_token
            }
            if username:
                payload["displayName"] = username 
            payload = json.dumps(payload)
            r = requests.post(rest_api_url, params={"key": "AIzaSyAyZy7muAWri-zIstiP3SOKEgpOLLxT4wY"}, data=payload)
            try:
                return r.json()['email']
            except:
                st.warning(r.json())
        except Exception as e:
            st.warning(f'Signup failed: {e}')

    def sign_in_with_email_and_password(email=None, password=None, return_secure_token=True):
        rest_api_url = "https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword"

        try:
            payload = {
                "returnSecureToken": return_secure_token
            }
            if email:
                payload["email"] = email
            if password:
                payload["password"] = password
            payload = json.dumps(payload)
            r = requests.post(rest_api_url, params={"key": "AIzaSyAyZy7muAWri-zIstiP3SOKEgpOLLxT4wY"}, data=payload)
            try:
                data = r.json()
                user_info = {
                    'email': data['email'],
                    'username': data.get('displayName')  # Retrieve username if available
                }
                return user_info
            except:
                st.warning(data)
        except Exception as e:
            st.warning(f'Signin failed: {e}')

    def f():
        try:
            userinfo = sign_in_with_email_and_password(st.session_state.email_input,st.session_state.password_input)
            st.session_state.username = userinfo['username']
            st.session_state.useremail = userinfo['email']

            if is_admin():
                st.session_state.admin = True
            else:
                st.session_state.admin = False

            st.session_state.signedout = True
            st.session_state.signout = True

        except:
            st.warning('Login Failed')

    def t():
        st.session_state.signout = False
        st.session_state.signedout = False   
        st.session_state.username = ''
        st.session_state.useremail = ''
        st.session_state.admin = False
        

    if "signedout"  not in st.session_state:
        st.session_state["signedout"] = False
    if 'signout' not in st.session_state:
        st.session_state['signout'] = False    

    if  not st.session_state["signedout"]: # only show if the state is False, hence the button has never been clicked
        choice = st.selectbox('Login/Signup',['Login','Sign up'])
        email = st.text_input('Email Address')
        password = st.text_input('Password',type='password')
        st.session_state.email_input = email
        st.session_state.password_input = password

        if choice == 'Sign up':
            username = st.text_input("Enter  your unique username")

            if st.button('Create my account'):
                user = sign_up_with_email_and_password(email=email,password=password,username=username)
                st.success('Account created successfully!')
                st.markdown('Please Login using your email and password')
                st.balloons()
        else:
            st.button('Login', on_click=f)

    if st.session_state.signout:
        st.text('Name '+st.session_state.username)
        st.text('Email id: '+st.session_state.useremail)
        if st.button('Sign out', on_click=t):
            st.session_state.signout = False
            st.session_state.signedout = False
            
            

    if is_admin():
        st.sidebar.markdown('Hello, '+st.session_state.username)
        st.sidebar.markdown('You are logged in as an admin')
   

def is_admin():
    admin_users = ['adminakhil@gmail.com'] #  admin email ids 
    if st.session_state.useremail in admin_users:
        return True
    else:
        return False

login()

