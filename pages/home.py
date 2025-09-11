from nicegui import ui
from components.header import header
from components.footer import footer
from typing import List, Dict

# Sample data for categories.
CATEGORIES = [
    {'name': 'All Categories', 'icon': 'apps', 'ads': 'All'},
    {'name': 'Health & Beauty', 'icon': 'phone_iphone', 'ads': '39,286'},
    {'name': 'Work & Office', 'icon': 'laptop_mac', 'ads': '223,071'},
    {'name': 'Entertainment', 'icon': 'home', 'ads': '430,240'},
    {'name': 'Others', 'icon': 'home', 'ads': '330,240'},
]

# Sample data for featured ads
FEATURED_ADS = [
    {'title': 'Smartwatch Ultra 2', 'price': '$299', 'image': 'https://picsum.photos/id/101/300/200'},
    {'title': 'Wireless Headphones', 'price': '$149', 'image': 'https://picsum.photos/id/102/300/200'},
    {'title': '4K Smart TV', 'price': '$899', 'image': 'https://picsum.photos/id/103/300/200'},
    {'title': 'VR Headset', 'price': '$450', 'image': 'https://picsum.photos/id/104/300/200'},
    {'title': 'Gaming Laptop', 'price': '$1,200', 'image': 'https://picsum.photos/id/105/300/200'},
    {'title': 'Digital Camera', 'price': '$650', 'image': '/assets/laptop-1483974_1280.jpg'},
]

# A list of image URLs for the carousel
# CAROUSEL_IMAGES = [
#     'assets/herocover2.jpg',
#     'assets/herocover3.png',
#     'assets/laptop-1483974_1280.jpg'
# ]

def home_page():

    # Big container
    with ui.element("div").classes("w-full h-[600px] relative rounded-b-3xl shadow-xl overflow-hidden"):

        # Background carousel
        with ui.carousel().props("arrows autoplay swipe infinite").classes(
            "absolute inset-0 w-full h-screen z-[-2]"
        ).style("width: 100vw; height: 100vh;"):
            ui.carousel_slide().classes("w-full h-screen").style(
                "background-image: url(/assets/cover.jpg); background-size: cover; background-position: center; width: 100vw; height: 100vh;"
            )
            ui.carousel_slide().classes("w-full h-screen").style(
                "background-image: url(/assets/cover4.png); background-size: cover; background-position: center; width: 100vw; height: 100vh;"
            )
            ui.carousel_slide().classes("w-full h-screen").style(
                "background-image: url(/assets/cover2.jpg); background-size: cover; background-position: center; width: 100vw; height: 100vh;"
            )

# def home_page():
#     # Hero section container with a shadow and rounded bottom corners
#     with ui.column().classes('w-full h-[600px] relative rounded-b-3xl shadow-xl overflow-hidden'):
        
#         # Background carousel
#         with ui.carousel(animated=True, arrows=False, navigation=False).props('arrows autoplay swipe infinite').classes('absolute inset-0 w-screen h-full object-cover z-[-2]').style("width: 100vw; height: 100vh;"):
#             for image_url in CAROUSEL_IMAGES:
#                 ui.image(image_url).classes('w-full h-full object-cover')
        
        # A static overlay to ensure text is readable over all carousel images
        #ui.element('div').classes('absolute inset-0 bg-black opacity-40 z-10')

        # Header component to be visible on top of the hero section
        with ui.column().classes('absolute z-20 w-full'):
            header()

        # Hero content - Main title and search bar
        with ui.column().classes('relative z-20 w-full h-full flex flex-col items-center justify-center p-8'):
            ui.label('Discover. Post. Sell.').classes('text-6xl font-bold text-white mb-4')
            ui.label('Your Hub for Gadget Ads').classes('text-2xl text-white font-light')

            # Search and filter section
            with ui.row().classes('w-full max-w-4xl mt-8 p-2 rounded-full bg-white bg-opacity-90 backdrop-filter backdrop-blur-sm'):
                # Location dropdown
                ui.select(['All Categories', 'Health & Beauty', 'Entertainment', 'Home & Office'], value='All Categories') \
                    .classes('w-40 bg-transparent text-gray-800 rounded-l-full px-4')
                
                # Search bar
                ui.input(placeholder='What are you looking for?').classes('flex-grow px-6 py-2 text-lg text-gray-800 bg-transparent border-none focus:outline-none')
                
                # Search button
                ui.button(icon='search').classes('bg-green-600 hover:bg-green-700 px-3 py-3 text-white rounded-full transition-colors')

    # Categories section below the hero
    # Categories section as a grid slider
    # with ui.column().classes('w-full items-center -mt-24 relative z-30 p-8'):
    #     ui.label('Browse Categories').classes('text-3xl font-bold text-gray-800 mb-6')

    #     with ui.carousel().props('arrows swipe infinite').classes('w-full max-w-6xl'):
    #         # Chunk categories into groups of 3-4 per slide
    #         chunk_size = 6
    #         for i in range(0, len(CATEGORIES), chunk_size):
    #             with ui.carousel_slide().classes("flex gap-6 justify-center items-stretch"):
    #                 for category in CATEGORIES[i:i+chunk_size]:
    #                     with ui.card().classes(
    #                         'w-64 h-56 relative p-0 overflow-hidden transform transition-transform hover:scale-105 shadow-xl cursor-pointer'
    #                     ):
    #                         # Category image background
    #                         ui.image(f'assets/category_{category["name"].replace(" ", "_")}.jpg').classes('w-full h-full object-cover')

    #                         # Dark overlay
    #                         ui.element('div').classes('absolute inset-0 bg-black opacity-40')

    #                         # Category info
    #                         with ui.column().classes(
    #                             'absolute inset-0 flex items-center justify-center text-white text-center p-4 z-10'
    #                         ):
    #                             ui.icon(category['icon']).classes('text-3xl mb-2')
    #                             ui.label(category['name']).classes('text-xl font-bold')
    #                             if category['ads'] != 'All':
    #                                 ui.label(f'{category["ads"]} ads').classes('text-sm text-gray-300 mt-1')

    #                         # Hover "View" button
    #                         ui.button('View', on_click=lambda name=category['name']: ui.navigate.to(f'/view?category={name}')) \
    #                             .classes('absolute bottom-4 right-4 bg-yellow-400 text-gray-900 rounded-full px-4 py-2 opacity-0 hover:opacity-100 transition-opacity')

    with ui.column().classes('w-full items-center -mt-24 relative z-30 p-8'):
        with ui.carousel().props('arrows swipe infinite').classes('w-full max-w-6xl txt-purple'):
            # Chunk categories into groups of 3-4 per slide
            chunk_size = 4
            for i in range(0, len(CATEGORIES), chunk_size):
                with ui.carousel_slide().classes("flex gap-6 justify-center items-stretch bg-purple-700"):
                    for category in CATEGORIES[i:i+chunk_size]:
                        with ui.card().classes(
                            'w-64 h-56 relative p-0 overflow-hidden transform transition-transform hover:scale-105 shadow-xl cursor-pointer'
                        ):
                            # Category image background
                            ui.image(f'assets/category_{category["name"].replace(" ", "_")}.jpg').classes('w-full h-full object-cover')

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

                            # Hover "View" button
                            ui.button('View', on_click=lambda name=category['name']: ui.navigate.to(f'/view?category={name}')) \
                                .classes('absolute bottom-4 right-4 bg-yellow-400 text-gray-900 rounded-full px-4 py-2 opacity-0 hover:opacity-100 transition-opacity')
    
    # Product grid section
    # ---
    with ui.column().classes('w-full p-8 mt-12'):
        ui.label('Featured Ads').classes('text-4xl font-bold text-gray-800 mb-8')

        with ui.row().classes('w-full justify-start items-stretch gap-8'):
            for ad in FEATURED_ADS:
                with ui.card().classes('w-64 transform transition-transform hover:scale-105 hover:shadow-2xl cursor-pointer'):
                    ui.image(ad['image']).classes('rounded-t-lg w-full')
                    with ui.card_section().classes('p-4'):
                        ui.label(ad['title']).classes('text-xl font-semibold mb-2')
                        ui.label(ad['price']).classes('text-2xl font-bold text-blue-600')
                        ui.button('View Details', on_click=lambda: ui.navigate.to('/view'))

    with ui.column().classes("w-screen"):
        footer()
