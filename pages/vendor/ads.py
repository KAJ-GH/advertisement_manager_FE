from nicegui import ui, app
import requests
from utils.api import base_url
from components.sidebar import show_sidebar
from components.footer import footer
from pages.category_ads import get_sample_ads # Use a single source of truth for ads

ui.add_head_html('<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css" rel="stylesheet" />')

@ui.page("/vendor/vendor_ads")
def show_vendor_ads():

    try:
        response = requests.get(f"{base_url}/advert")
        response.raise_for_status()
        json_data = response.json()
        if "data" not in json_data:
            json_data = {"data": []}
            ui.notify("No advertisements available at the moment.", type='info')

    except requests.exceptions.RequestException as e:
        ui.notify(f"Failed to load advertisements: {str(e)}", type='negative')
        json_data = {"data": []}

    except (KeyError, ValueError) as e:
        ui.notify("Invalid response from server.", type='negative')
        json_data = {"data": []}

    if not app.storage.user.get('authenticated') or app.storage.user.get('role') != 'Vendor':
        ui.notify('Access denied. Please log in as a vendor.', color='negative')
        ui.navigate.to('/login')
        return

    # --- Data Filtering ---
    vendor_id = app.storage.user.get('id')
    all_ads = get_sample_ads() # This get_sample_ads needs to fetch ads from the db.
    # Filter ads to show only those belonging to the logged-in vendor
    
    adverts_data = [ad for ad in all_ads if ad.get('vendor_id') == vendor_id]

    with ui.row().classes("w-full h-screen p-0 m-0"):
        # Side Navigation Bar        
        with ui.column().classes("h-full bg-gray-100 p-4 w-1/4 min-w-[200px] md:w-[25%] lg:w-[20%]"):
            # Vendor details (Brand logo, name, etc.)
            show_sidebar()
        

        # Main content area
        with ui.column().classes("flex-grow h-full p-6 bg-white"):
            # Header with page title and filter/view options
            with ui.row().classes("w-full items-center justify-between mb-4"):
                ui.label("My adverts").classes("text-2xl font-bold")
                
                # Top-right controls (Sell button, notifications, etc.)
                with ui.row().classes("items-center gap-4"):
                    ui.button("HOME", on_click=lambda: ui.navigate.to('/home'), color="blue", icon="home").classes("gap-5 font-semibold flex-items items-justify")
                    ui.button("SELL", on_click=lambda: ui.navigate.to('/vendor/post_ad'), color="green", icon="add_circle").classes("px-4 py-2 font-semibold")
                    #ui.avatar("person", size="sm").classes("text-white bg-green-500 cursor-pointer hover:text-gray-700")                  
                    with ui.button('PROFILE', icon='person').classes(
                        'cursor-pointer text-white hover:text-green-300 relative bg-purple-500 hover:bg-purple-600 text-white font-semibold rounded-full transition-colors'
                    ) as profile_icon:
                        with ui.menu().props('anchor="bottom end"') as menu: # anchor="bottom end" makes it open below and aligned to the right
                            # "My shop" / Vendor Dashboard
                            ui.menu_item('My shop', on_click=lambda: ui.navigate.to('/vendor/vendor_ads')).props('icon="storefront"')
                            ui.menu_item('Reviews', on_click=lambda: ui.navigate.to('/vendor/review')).props('icon="feedback"')
                            ui.menu_item('Performance', on_click=lambda: ui.navigate.to('/vendor/dashhboard')).props('icon="bar_chart"')
                            ui.separator()
                            def handle_logout():
                                app.storage.user.clear()
                                ui.navigate.to('/login')
                            ui.menu_item('Log out', on_click=handle_logout).props('icon="logout"')

            # Adverts content
            if not adverts_data:
                # Placeholder for no adverts
                with ui.column().classes("w-full h-full items-center justify-center"):
                    ui.image("image_d83146.png").classes("h-48")
                    ui.label("There are no adverts yet. Create new one now!").classes("text-lg font-semibold text-gray-500 mt-4")
            else:
                # Filter section with dropdowns
                with ui.row().classes("w-full items-center mb-4"):
                    ui.label("Filter by:").classes("text-md font-semibold")
                    ui.select(options=["Price", "Category", "Date"], label="Filter Option").classes("w-48")
                    ui.input(placeholder="Search by title or keyword").classes("flex-grow")
                
                ui.separator().classes("my-4")
                
                # Grid/List view toggle
                with ui.row():
                    ui.icon("view_list", size="lg").classes("cursor-pointer hover:text-blue-500")
                    ui.icon("grid_view", size="lg").classes("cursor-pointer hover:text-blue-500")


                # Grid view of adverts
                with ui.grid(columns="1 gap-4 sm:grid-cols-2 md:grid-cols-3"):
                    for advert in adverts_data:
                        with ui.card().classes("w-full p-4 border rounded-lg shadow-sm hover:shadow-lg transition-shadow"):
                            ui.label(advert.get("title")).classes("text-lg font-semibold")
    # Product grid section
    with ui.column().classes('w-full p-8 mt-12'):
        ui.label('Featured Ads').classes('text-4xl font-bold text-gray-800 mb-8')

        with ui.row().classes('w-full justify-start items-stretch gap-8'):
            for ad in json_data.get("data", []):
                with ui.card().classes('w-64 transform transition-transform hover:scale-105 hover:shadow-2xl cursor-pointer'):
                # Use 'flyer_url' which is provided by the API, with a fallback
                    ui.image(ad.get('flyer_url', 'assets/placeholder.png')).classes('rounded-t-lg w-full h-48 object-cover')
                    with ui.card_section().classes('p-4'):
                        ui.label(ad.get('title', 'No Title')).classes('text-xl font-semibold mb-2')
                        ui.label(f"₵{ad.get('price', 0):.2f}").classes('text-2xl font-bold text-blue-600')
                        ad_id = ad.get('id') or ad.get('_id')
                        ui.button('View Details', on_click=lambda ad_id=ad_id: ui.navigate.to(f'/view?id={ad_id}'))
                        ui.label(f"₵{advert.get('price', 0):.2f}").classes("text-xl font-bold text-green-600 mt-2")
                        ui.label(f"Category: {advert.get('category')}").classes("text-sm text-gray-500")
                        ui.label(advert.get("description")).classes("text-sm text-gray-700 mt-2")
                        with ui.row().classes("mt-4 justify-end w-full gap-2"):
                                            ui.button("View", on_click=lambda ad=advert: ui.navigate.to(f"/view?id={ad.get('id')}") ,color="blue")
                                            ui.button("Edit", on_click=lambda ad=advert: ui.navigate.to(f"/vendor/edit_ad?id={ad.get('id')}"), color="green")

                        footer()                    


    # Add a global style for better responsiveness and overall look
    ui.add_head_html('<style>html, body { margin: 0; padding: 0; }</style>')
