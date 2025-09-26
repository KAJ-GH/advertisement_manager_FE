from nicegui import ui, app
from pages.welcome import welcome_page
from pages.home import home_page
from pages.login import login_page
from pages.signup import signup_page
from pages.view_ads import view_ads_page
from pages.category_ads import category_ads_page
from components.footer import footer
from pages.vendor.dashboard import *
from pages.vendor.ads import *
from pages.vendor.post_ad import *
from pages.vendor.edit_ad import *


# Expose the assets folder to the nicegui server
app.add_static_files("/assets", "assets")

# link external icons to the head
ui.add_head_html('''
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/7.0.1/css/all.min.css" 
                 integrity="sha512-2SwdPD6INVrV/lHTZbO2nodKhrnDdJK9/kg2XD1r9uGqPo1cUbujc+IYdlYdEErWNu69gVcYgdxlmVmzTWnetw==" 
                 crossorigin="anonymous" referrerpolicy="no-referrer" />

''')
ui.add_head_html('<link rel="stylesheet" href="/assets/reset.css" />')
         

# Define pages routes
@ui.page("/")
def welcome():
    welcome_page()
     

@ui.page("/home")
def home():
    home_page()
    footer()


@ui.page("/view")
def view_ads():
    view_ads_page()
    footer()
   
@ui.page("/category")
def category_ads():
    category_ads_page()
    footer()

@ui.page("/vendor/post_ad")
def post_ad():
    post_ad_page()
    footer()

@ui.page("/login")
def login():
    login_page()

@ui.page("/signup")
def signup():
    signup_page()

ui.run(title="BeGadgetized Ads Platform", storage_secret="bfghdgufdjlkhhfdj")