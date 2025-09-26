from nicegui import ui
# from components.cart import cart_sidebar

# Dummy product data for the cart
# cart_items = [
#     {"id": 1, "name": "Bang & Olufsen Beoplay HX Comfortable Wireless ANC Over-Ear Headphones", "price": 9500, "quantity": 1, "image": "image_12345.png"},
#     {"id": 2, "name": "Beyerdynamic Free Byrd True Wireless Bluetooth® in-ear headphones with ANC", "price": 2490, "quantity": 1, "image": "image_12345.png"},
# ]

# cart_visible = ui.toggle(False)
    
def header():
    #A modern, semi-transparent header that sits on top of hero sections.
    with ui.row().classes('w-full bg-white px-8 py-4 items-center justify-between shadow-sm'):
        # Clickable logo that navigates to the welcome page
        with ui.link(target='/').classes('flex items-center gap-2'):
            ui.image('/assets/logo.png').classes('w-8 h-8')
            ui.label('BeGadgetized').classes('text-2xl font-bold hover:text-purple-300 transition-colors no-underline')
        
        # Navigation links
        with ui.row().classes('items-center gap-8 uppercase text-sm font-semibold'):
            ui.link('Home', target='/home').classes('hover:text-purple-300 transition-colors no-underline')
            # This link can be pointed to a dedicated "all ads" page in the future
            ui.link('Trending Ads', target='/category_ads').classes('hover:text-purple-300 transition-colors no-underline')
            ui.link('Blog', target='/contact').classes('hover:text-purple-300 transition-colors no-underline')
        # Right side icons
        with ui.row().classes('gap-4 items-center'):
            ui.link('Login', '/login').classes('text-gray-700 hover:text-pink-600 no-underline')
            ui.link('Register', '/signup').classes('text-gray-700 hover:text-pink-600 no-underline')
            
            ui.icon('search', size='xs').classes('text-gray-700 cursor-pointer')
        # Vendor-specific buttons
        with ui.row().classes('items-center'):
            #with ui.icon('person', size='lg').classes('cursor-pointer text-white hover:text-green-300 relative') as profile_icon:
            with ui.button('Vendor', icon='person').classes(
                'cursor-pointer text-white hover:text-green-300 relative bg-purple-500 hover:bg-purple-600 text-white font-semibold rounded-full transition-colors'
            ) as profile_icon:
                with ui.menu().props('anchor="bottom end"') as menu: # anchor="bottom end" makes it open below and aligned to the right
                    # "My shop" / Vendor Dashboard
                    ui.menu_item('My shop', on_click=lambda: ui.navigate.to('/vendor/vendor_ads')).props('icon="storefront"')
                    ui.menu_item('Make Money', on_click=lambda: ui.navigate.to('/vendor/post_ad')).props('icon="attach_money"')
                    ui.menu_item('Dashboard', on_click=lambda: ui.navigate.to('/vendor/dashboard')).props('icon="bar_chart"')
                    ui.separator()
                    ui.menu_item('Log out', on_click=lambda: ui.navigate.to('/logout')).props('icon="logout"')              