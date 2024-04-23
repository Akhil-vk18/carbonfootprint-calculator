import streamlit as st
from streamlit_option_menu import option_menu

import login, cfc,home

st.set_page_config(
        page_title="CARBON FOOTPRINT CALCULATOR",
)

class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):

        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):
        # app = st.sidebar(
        with st.sidebar:        
            app = option_menu(
                menu_title=' ',
                options=['Home','Account','Calculate'],
                icons=['house-fill','person-circle','tree-fill'],
                menu_icon='',
                default_index=1,
                styles={
                    "container": {"padding": "5!important","background-color":'black'},
        "icon": {"color": "white", "font-size": "23px"}, 
        "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
        "nav-link-selected": {"background-color": "#02ab21"},}
                
                )

        
        if app == "Home":
            home.app()
        if app == "Account":
            login.login()    
        if app == "Calculate":
            cfc.cfc()        
        #if app == 'Your Posts':
            #your.app()
        #if app == 'about':
            #about.app()    
             
          

if __name__ == "__main__":
    app = MultiApp()   # create an instance of the MultiApp class
    app.add_app("Home", home.app)   # add an app to the instance
    app.add_app("Account", login.login)   # add another app to the instance
    app.add_app("Calculate", cfc.cfc)   # add another app to the instance
    app.run()   # call the run() method on the instance