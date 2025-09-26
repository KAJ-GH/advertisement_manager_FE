from nicegui import ui, app
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

        # Right side icons and buttons
        with ui.row().classes('gap-4 items-center'):
            ui.icon('search', size='xs').classes('text-gray-700 cursor-pointer')
            with ui.button_group().props('outline rounded unelevated'):
                    ui.button('Login', on_click=lambda: ui.navigate.to('/login')).props(' outline color=primary')
                    ui.button('Register', on_click=lambda: ui.navigate.to('/signup')).props('color=primary unelevated')

            # --- Development: Always show vendor menu ---
            # This replaces the conditional login/logout buttons for easy access during development.
            with ui.button(icon='person').props('round color=primary unelevated'):
                with ui.menu().props('anchor="bottom end" self="top end"'):
                    ui.menu_item('My Shop', on_click=lambda: ui.navigate.to('/vendor/vendor_ads')).props('icon="storefront"')
                    ui.menu_item('Post Ad', on_click=lambda: ui.navigate.to('/vendor/post_ad')).props('icon="add_circle"')
                    ui.menu_item('Dashboard', on_click=lambda: ui.navigate.to('/vendor/dashboard')).props('icon="bar_chart"')
                    ui.separator()
                    
                    def handle_logout():
                        """Clear user session and redirect to home page."""
                        app.storage.user.clear()
                        ui.navigate.to('/home')
                        ui.notify('You have been logged out.', color='positive')

                    ui.menu_item('Logout', on_click=handle_logout).props('icon="logout"')