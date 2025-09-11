from nicegui import ui, app, ElementFilter
from pages.welcome import welcome_page
from pages.home import home_page
from pages.view_ads import view_ads_page
from pages.post_ad import post_ad_page
from pages.edit_ad import edit_ad_page
from pages.category_ads import category_ads_page

# add header and footer components
from components.header import header
from components.footer import footer

# Expose the assets folder to the nicegui server
app.add_static_files("/assets", "assets")

# link external icons to the head
ui.add_head_html('''
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/7.0.1/css/all.min.css" 
                 integrity="sha512-2SwdPD6INVrV/lHTZbO2nodKhrnDdJK9/kg2XD1r9uGqPo1cUbujc+IYdlYdEErWNu69gVcYgdxlmVmzTWnetw==" 
                 crossorigin="anonymous" referrerpolicy="no-referrer" />

''')
ui.add_head_html('<link rel="stylesheet" href="/assets/reset.css" />')

# Wrapper for page
# def page_layout(content_fn):
#     with ui.column().classes('flex-1 bg-gray-50'):
#         header()
#         content_fn()              
#         footer()                   

# Define pages routes
@ui.page("/")
def welcome():
    welcome_page()
     

@ui.page("/home")
def home():
    home_page()

@ui.page("/view")
def view_ads():
    view_ads_page()

@ui.page("/add")
def post_ad():
    post_ad_page()

@ui.page("/edit")
def edit_ad():
   edit_ad_page()

@ui.page("/category")
def category_ads():
    category_ads_page()

ui.run(port=8000, title="BeGadgetized Ads Platform", storage_secret="your-secret-key-here")