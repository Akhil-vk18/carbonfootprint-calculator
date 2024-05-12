import streamlit as st
from streamlit_option_menu import option_menu
import home,login, cfc,admin
# Set wide layout and page name
st.set_page_config(layout="wide", page_title="Personal Carbon Calculator")


class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):

        self.apps.append({
            "title": title,
            "function": func
        })

    
    def run(self):
        
        with st.sidebar:        
            app = option_menu(
                menu_title='Carbon Footprint Calculator ',
                options=['Home','Account','Calculate',"Admin"],
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
        if app == "Admin":
            admin.admin()
   
           
          

if __name__ == "__main__":
    app = MultiApp()   # create an instance of the MultiApp class
    app.run()
    