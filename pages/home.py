from nicegui import ui
from components.header import header
from components.footer import footer
from typing import List, Dict
import requests
from utils.api import base_url

# Sample data for categories.
CATEGORIES = [
    {'name': 'Mobile Devices', 'icon': 'phone_iphone', 'ads': 'Browse', 'link_name': 'Mobile_Devices', 'image': 'assets/Category_Mobile_Devices/mobile_device.jpg'},
    {'name': 'Home & Office', 'icon': 'work', 'ads': 'Browse', 'link_name': 'Office', 'image': 'assets/Category_Home_&_Office/home_office.jpg'},
    {'name': 'Entertainment & Sound', 'icon': 'headset', 'ads': 'Browse', 'link_name': 'Entertainment', 'image': 'assets/category_entertainment_&_sound/others1.png'},
    {'name': 'Health & Beauty', 'icon': 'spa', 'ads': 'Browse', 'link_name': 'Health', 'image': 'assets/category_Health_&_Beauty/health_beauty.jpg'},
    {'name': 'Other Gadgets', 'icon': 'devices_other', 'ads': 'Browse', 'link_name': 'Gadgets', 'image': 'assets/category_Others/others.jpg'},
]

# Sample data for featured ads
FEATURED_ADS = []

@ui.page('/home')
def home_page():
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

    # Big container
    with ui.element("div").classes("w-full h-[600px] relative rounded-b-3xl shadow-xl overflow-hidden"):

        # Background carousel
        with ui.carousel().props("arrows autoplay swipe infinite").classes(
            "absolute inset-0 w-full h-full z-[-2]"
        ).style("width: 100vw; height: 100vh;"):
            ui.carousel_slide().classes("w-full h-full").style(
                "background-image: url(/assets/cover.jpg); background-size: cover; background-position: center; width: 100vw; height: 100vh;"
            )
            ui.carousel_slide().classes("w-full h-full").style(
                "background-image: url(/assets/cover4.png); background-size: cover; background-position: center; width: 100vw; height: 100vh;"
            )
            ui.carousel_slide().classes("w-full h-full").style(
                "background-image: url(/assets/cover2.jpg); background-size: cover; background-position: center; width: 100vw; height: 100vh;"
            )

        # Header component to be visible on top of the hero section
        with ui.column().classes('relative z-30 w-full'):
            header()

        # Hero content - Main title and search bar
        with ui.column().classes('relative z-20 w-full h-full flex flex-col items-center justify-center p-8'):
            ui.label('Discover. Post. Sell.').classes('text-8xl font-bold text-white mb-4')
            ui.label('Your No.1️⃣ Hub for Gadgets, Appliances & Electronics').classes('text-3xl text-white font-light')

            # Search and filter section
            #with ui.row().classes('w-full max-w-4xl mt-8 p-2 rounded-full bg-white bg-opacity-90 backdrop-filter backdrop-blur-sm'):
                # Location dropdown
                #ui.select(['Mobile Devices', 'Health & Beauty', 'Entertainment & Sound', 'Home & Office'], value='Mobile Devices') \
                    #.classes('w-40 bg-transparent text-gray-800 rounded-l-full px-4')
                
                # Search bar
        ui.input(placeholder='What are you looking for?').classes('flex-grow px-8 py-2 text-lg text-gray-800 bg-transparent border-none focus:outline-none')
                
                # Search button
        #ui.button(icon='search').classes('bg-green-600 hover:bg-green-700 px-3 py-3 text-white rounded-full transition-colors')

    # Categories section below the hero
    with ui.column().classes('w-full items-center -mt-24 relative z-30 p-8'):
        with ui.carousel().props('arrows swipe infinite').classes('w-full max-w-6xl txt-purple'):
            # Chunk categories into groups of 3-4 per slide
            chunk_size = 4
            for i in range(0, len(CATEGORIES), chunk_size):
                with ui.carousel_slide().classes("flex gap-6 justify-center items-stretch bg-purple-700"):
                    for category in CATEGORIES[i:i+chunk_size]:
                        with ui.card().classes(
                            'group w-64 h-56 relative p-0 overflow-hidden transform transition-transform hover:scale-105 shadow-xl cursor-pointer'
                        ).on('click', lambda e, name=category['link_name']: ui.navigate.to(f'/category_ads?category={name}')):
                        
                            # Category image background
                            ui.image(category['image']).classes('w-full h-full object-cover')

                            # Dark overlay
                            ui.element('div').classes('absolute inset-0 bg-black opacity-40')

                            # Category info
                            with ui.column().classes(
                                'absolute inset-0 flex items-center justify-center text-white text-center p-4 z-10'
                            ):
                                ui.icon(category['icon']).classes('text-3xl mb-2')
                                ui.label(category['name']).classes('text-xl font-bold')
                                if category['ads'] != 'All':
                                    ui.label(f'{category["ads"]} ads').classes('text-sm text-gray-300 mt-1')

                            ui.button(
                                'View'
                            ).classes(
                                'absolute bottom-4 right-4 bg-yellow-400 text-gray-900 rounded-full px-4 py-2 opacity-0 group-hover:opacity-100 transition-opacity pointer-events-none'
                            )
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
                        ui.button('Edit', on_click=lambda ad_id=ad_id: ui.navigate.to(f'/vendor/edit_ad?id={ad_id}'))

    # Call to Action Section (New)
    with ui.element('div').classes('w-full flex items-center justify-center my-12'):
        with ui.element('div').classes(
            'w-full max-w-5xl rounded-3xl p-10 flex flex-col items-center text-center text-white '
            'bg-gradient-to-r from-blue-600 to-purple-600 bg-opacity-90 backdrop-filter backdrop-blur-sm shadow-2xl space-y-6'
        ):
            ui.label('Post Your Ad Today!').classes('text-4xl font-bold md:text-5xl')
            ui.label('Got something to sell? Reach thousands of potential buyers in minutes.').classes('text-lg font-light md:text-xl')
            ui.button('Post an Ad', on_click=lambda: ui.navigate.to('/vendor/post_ad')).classes('bg-purple-600 hover:bg-green-700 text-white px-8 py-4 rounded-full transition-color')
            #ui.image()

        