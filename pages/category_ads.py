from nicegui import ui
from components.header import header
#from components.footer import footer
import requests
from utils.api import base_url

def get_sample_ads():
    """Return sample ads data with local asset images"""
    return [
        {
            'id': '1',
            'title': 'MacBook Pro 16-inch',
            'price': 2500.00,
            'category': 'Mobile Devices',
            'image': '/assets/laptop-1483974_1280.jpg',
            'description': 'Excellent condition MacBook Pro with M1 chip'
        },
        {
            'id': '2', 
            'title': 'iPhone 14 Pro Max',
            'price': 1200.00,
            'category': 'Mobile Devices',
            'image': '/assets/category_Mobile_Devices.jpg',
            'description': 'Brand new iPhone 14 Pro Max, 256GB'
        },
        {
            'id': '3',
            'title': 'Gaming Headset',
            'price': 150.00,
            'category': 'Entertainment & Sound',
            'image': '/assets/Category_Entertainment_&_Sound.jpg',
            'description': 'High-quality gaming headset with noise cancellation'
        },
        {
            'id': '4',
            'title': 'Office Chair',
            'price': 300.00,
            'category': 'Home & Office',
            'image': '/assets/Category_Work_&_Office.jpg',
            'description': 'Ergonomic office chair, perfect for long work hours'
        },
        {
            'id': '5',
            'title': 'Skincare Set',
            'price': 80.00,
            'category': 'Health & Beauty',
            'image': '/assets/category_Health_&_Beauty.jpg',
            'description': 'Complete skincare routine set with natural ingredients'
        },
        {
            'id': '6',
            'title': 'Wireless Speaker',
            'price': 200.00,
            'category': 'Entertainment & Sound',
            'image': '/assets/Category_Entertainment_&_Sound.jpg',
            'description': 'Portable Bluetooth speaker with excellent sound quality'
        },
        {
            'id': '7',
            'title': 'Standing Desk',
            'price': 450.00,
            'category': 'Home & Office',
            'image': '/assets/Category_Work_&_Office.jpg',
            'description': 'Height-adjustable standing desk for better posture'
        },
        {
            'id': '8',
            'title': 'Fitness Tracker',
            'price': 120.00,
            'category': 'Health & Beauty',
            'image': '/assets/category_Health_&_Beauty.jpg',
            'description': 'Smart fitness tracker with heart rate monitoring'
        },
        {
            'id': '9',
            'title': 'Camera Drone',
            'price': 850.00,
            'category': 'Other Gadgets',
            'image': '/assets/cover.jpg',
            'description': '4K camera drone with 30-minute flight time.'
        },
    ]

def category_ads_page():
    q = ui.context.client.request.query_params
    category = q.get('category')

    # To display the dummy data, we call get_sample_ads() instead of the API.
    all_ads = get_sample_ads()
    
    # Filter ads based on the category from the URL query
    filtered_ads = [
        ad for ad in all_ads if ad.get('category') == category
    ]

    with ui.column().classes('w-full min-h-screen bg-gray-50'):
        header()
        
        # Category header section
        with ui.element('div').classes('w-full bg-gradient-to-r from-blue-600 to-purple-600 py-16'):
            with ui.column().classes('w-full max-w-6xl mx-auto px-8 text-center'):
                ui.label(f'{category} Ads').classes('text-4xl md:text-5xl font-bold text-white mb-4')
                ui.label(f'Discover amazing deals in {category}').classes('text-xl text-blue-100')
        
        # Filters and search section
        with ui.row().classes('w-full max-w-6xl mx-auto px-8 py-6 gap-4'):
            # Search bar
            search_input = ui.input(placeholder='Search ads...').classes('flex-grow')
            
            # Sort dropdown
            sort_select = ui.select(
                ['Newest First', 'Price: Low to High', 'Price: High to Low', 'Title A-Z'],
                value='Newest First'
            ).classes('w-48')
            
            # Filter button
            ui.button('Filters', icon='tune').classes('bg-blue-600 text-white px-4 py-2')

        # Ads grid section
        with ui.column().classes('w-full max-w-6xl mx-auto px-8 pb-16'):
            if not filtered_ads:
                # No ads found message
                with ui.column().classes('w-full text-center py-16'):
                    ui.icon('search_off').classes('text-6xl text-gray-400 mb-4')
                    ui.label('No ads found').classes('text-2xl font-semibold text-gray-600 mb-2')
                    ui.label(f'There are currently no ads in the {category} category.').classes('text-gray-500 mb-6')
                    ui.button('Browse All Categories', on_click=lambda: ui.navigate.to('/')).classes(
                        'bg-blue-600 text-white px-6 py-3 rounded-lg hover:bg-blue-700'
                    )
            else:
                # Ads grid
                with ui.element('div').classes('grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6'):
                    for ad in filtered_ads:
                        create_ad_card(ad)

def create_ad_card(ad):
    """Create an individual ad card"""
    with ui.card().classes('w-full max-w-sm transform transition-all duration-300 hover:scale-105 hover:shadow-xl overflow-hidden'):
        
        # Ad image
        # Check for 'flyer_url' (from API) or 'image' (from dummy data)
        image_url = ad.get('flyer_url') or ad.get('image')
        if image_url:
            ui.image(image_url).classes('w-full h-48 object-cover')
        else:
            # Placeholder image
            with ui.element('div').classes('w-full h-48 bg-gray-200 flex items-center justify-center'):
                ui.icon('image').classes('text-4xl text-gray-400')
        
        # Ad content
        with ui.card_section().classes('p-4'):
            # Title/Name
            ui.label(ad.get('title', 'Untitled')).classes(
                'text-lg font-semibold text-gray-800 mb-2 truncate'
            )
            
            # Price
            price = ad.get('price', 0)
            if isinstance(price, (int, float)) and price > 0:
                ui.label(f'₵{price:,.2f}').classes('text-xl font-bold text-green-600 mb-3')
            else:
                ui.label('Price on request').classes('text-lg text-gray-500 mb-3')
            
            # Action buttons
            with ui.row().classes('w-full gap-2'):
                ui.button('View', icon='visibility', on_click=lambda a=ad: view_ad_details(a)).classes(
                    'flex-1 bg-blue-600 text-white py-2 rounded-lg hover:bg-blue-700 transition-colors'
                )
                #ui.button('Edit', icon='edit', on_click=lambda a=ad: edit_ad_details(a)).classes(
                #    'flex-1 bg-gray-600 text-white py-2 rounded-lg hover:bg-gray-700 transition-colors'
                #)

def view_ad_details(ad):
    """Navigate to ad details page"""
    ad_id = ad.get('id', ad.get('_id', ''))
    if ad_id:
        ui.navigate.to(f'/view?id={ad_id}')
    else:
        ui.navigate.to('/view')

def edit_ad_details(ad):
    """Navigate to edit ad page"""
    ad_id = ad.get('id', ad.get('_id', ''))
    if ad_id:
        ui.navigate.to(f'/edit_event?id={ad_id}')
    else:
        ui.navigate.to('/edit_event')
