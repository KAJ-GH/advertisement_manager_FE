from nicegui import ui
from components.header import header

def get_sample_ads():
    """Return sample ads data with local asset images"""
    return [
        {
            'id': '1',
            'title': 'iPhone 15 Pro',
            'price': 2500.00,
            'vendor_id': 'vendor1',
            'category': 'Mobile_Devices',
            'image': 'assets/Category_Mobile_Devices/iphone.jpg',
            'description': 'Excellent condition MacBook Pro with M1 chip'
        },
        {
            'id': '2',
            'title': 'Samsung Galaxy S24 Ultra',
            'price': 1200.00,
            'vendor_id': 'vendor1',
            'category': 'Mobile_Devices',
            'image': 'assets/Category_Mobile_Devices/samsung1.jpg',
            'description': 'Brand new Samsung Galaxy S24 Ultra, 256GB'
        },
        {
            'id': '3',
            'title': 'Infinix Hot 6',
            'price': 2200.00,
            'vendor_id': 'vendor1',
            'category': 'Mobile_Devices',
            'image': 'assets/Category_Mobile_Devices/infinix.jpg',
            'description': 'Brand new Infinix Hot 6, 256GB'
        },
        {
            'id': '4',
            'title': 'Itel',
            'price': 2500.00,
            'vendor_id': 'vendor1',
            'category': 'Mobile_Devices',
            'image': 'assets/Category_Mobile_Devices/itel.jpg',
            'description': 'Brand new Itel, 256GB'
        },
        {
            'id': '5',
            'title': 'Pixel',
            'price': 5500.00,
            'vendor_id': 'vendor1',
            'category': 'Mobile_Devices',
            'image': 'assets/Category_Mobile_Devices/pixel.jpg',
            'description': 'Brand new Pixel, 256GB'
        },
        {
            'id': '6',
            'title': 'Z-Flip',
            'price': 10000.00,
            'vendor_id': 'vendor1',
            'category': 'Mobile_Devices',
            'image': 'assets/Category_Mobile_Devices/z-flip.jpg',
            'description': 'Brand new Pixel, 256GB'
        },
        {
            'id': '7',
            'title': 'Gaming Headset',
            'price': 1500.00,
            'vendor_id': 'vendor2',
            'category': 'Entertainment',
            'image': 'assets/category_entertainment_&_sound/gaming.jpg',
            'description': 'High-quality gaming headset with noise cancellation'
        },
        {
            'id': '8',
            'title': 'Monitor',
            'price': 3000.00,
            'vendor_id': 'vendor2',
            'category': 'Office',
            'image': 'assets/Category_Home_&_Office/monitor.jpg',
            'description': 'Ergonomic office chair, perfect for long work hours'
        },
        {
            'id': '9',
            'title': 'Facial massage',
            'price': 800.00,
            'vendor_id': 'vendor2',
            'category': 'Health',
            'image': 'assets/category_Health_&_Beauty/beauty2.jpg',
            'description': 'Complete skincare routine set with natural ingredients'
        },
        {
            'id': '10',
            'title': 'Gaming Speaker',
            'price': 200.00,
            'vendor_id': 'vendor2',
            'category': 'Entertainment',
            'image': 'assets/category_entertainment_&_sound/enter2.jpg',
            'description': 'Portable Bluetooth speaker with excellent sound quality'
        },
        {
            'id': '11',
            'title': 'Home Theatre Set',
            'price': 4450.00,
            'vendor_id': 'vendor2',
            'category': 'Office',
            'image': 'assets/Category_Home_&_Office/home3.jpg',
            'description': 'Height-adjustable home theatre system with deep desk for better posture'
        },
        {
            'id': '12',
            'title': 'Fitness Tracker',
            'price': 1200.00,
            'vendor_id': 'vendor2',
            'category': 'Health',
            'image': 'assets/category_Health_&_Beauty/health1.jpg',
            'description': 'Smart fitness tracker with heart rate monitoring'
        },
        {
            'id': '13',
            'title': 'Camera Drone',
            'price': 850.00,
            'vendor_id': 'vendor1',
            'category': 'Gadgets',
            'image': 'assets/Gadgets/drone.jpg',
            'description': '4K camera drone with 30-minute flight time.'
        },
        {
            'id': '14',
            'title': 'Home Smart',
            'price': 4450.00,
            'vendor_id': 'vendor2',
            'category': 'Office',
            'image': 'assets/Category_Home_&_Office/home2.jpg',
            'description': 'For your homes and offices'
        },
        {
            'id': '15',
            'title': 'Mouse',
            'price': 4450.00,
            'vendor_id': 'vendor2',
            'category': 'Office',
            'image': 'assets/Category_Home_&_Office/mouse.jpg',
            'description': 'Mouse for office use'
        },
        {
            'id': '16',
            'title': 'Printer',
            'price': 4450.00,
            'vendor_id': 'vendor2',
            'category': 'Office',
            'image': 'assets/Category_Home_&_Office/printer.jpg',
            'description': 'For printing'
        },
        {
            'id': '17',
            'title': 'TCL Smart Television',
            'price': 4450.00,
            'vendor_id': 'vendor1',
            'category': 'Office',
            'image': 'aassets/Category_Home_&_Office/TV1.jpg',
            'description': 'A smart television with good quality'
        },
        {
            'id': '18',
            'title': 'TCL Smart Television',
            'price': 4450.00,
            'vendor_id': 'vendor1',
            'category': 'Office',
            'image': 'aassets/Category_Home_&_Office/TV1.jpg',
            'description': 'A smart television with good quality'
        },
        {
            'id': '19',
            'title': 'TCL Smart Television',
            'price': 4450.00,
            'vendor_id': 'vendor1',
            'category': 'Office',
            'image': 'aassets/Category_Home_&_Office/TV1.jpg',
            'description': 'A smart television with good quality'
        },
        {
            'id': '20',
            'title': 'TCL Smart Television',
            'price': 4450.00,
            'vendor_id': 'vendor2',
            'category': 'Health',
            'image': 'aassets/Category_Home_&_Office/TV1.jpg',
            'description': 'A smart television with good quality'
        },
        {
            'id': '21',
            'title': 'Fitness Tracker',
            'price': 4450.00,
            'vendor_id': 'vendor2',
            'category': 'Health',
            'image': 'assets/category_Health_&_Beauty/health2.jpg',
            'description': 'A smart television with good quality'
        },
        {
            'id': '22',
            'title': 'Beauty Eye Massager',
            'price': 4450.00,
            'vendor_id': 'vendor2',
            'category': 'Health',
            'image': 'assets/category_Health_&_Beauty/beauty3.jpg',
            'description': 'A smart television with good quality'
        },
        {
            'id': '25',
            'title': 'Skincare Set',
            'price': 4450.00,
            'vendor_id': 'vendor2',
            'category': 'Health',
            'image': 'assets/category_Health_&_Beauty/beauty1.jpg',
            'description': 'A smart television with good quality'
        },
        {
            'id': '26',
            'title': 'TCL Smart Television',
            'price': 4450.00,
            'vendor_id': 'vendor1',
            'category': 'Entertainment',
            'image': 'aassets/Category_Home_&_Office/TV1.jpg',
            'description': 'A smart television with good quality'
        },
        {
            'id': '27',
            'title': 'TCL Smart Television',
            'price': 4450.00,
            'vendor_id': 'vendor1',
            'category': 'Entertainment',
            'image': 'aassets/Category_Home_&_Office/TV1.jpg',
            'description': 'A smart television with good quality'
        },
        {
            'id': '28',
            'title': 'TCL Smart Television',
            'price': 4450.00,
            'vendor_id': 'vendor1',
            'category': 'Entertainment',
            'image': 'aassets/Category_Home_&_Office/TV1.jpg',
            'description': 'A smart television with good quality'
        },
        {
            'id': '29',
            'title': 'TCL Smart Television',
            'price': 4450.00,
            'vendor_id': 'vendor1',
            'category': 'Entertainment',
            'image': 'aassets/Category_Home_&_Office/TV1.jpg',
            'description': 'A smart television with good quality'
        },
        {
            'id': '30',
            'title': 'TCL Smart Television',
            'price': 4450.00,
            'vendor_id': 'vendor1',
            'category': 'Entertainment',
            'image': 'aassets/Category_Home_&_Office/TV1.jpg',
            'description': 'A smart television with good quality'
        },
        {
            'id': '31',
            'title': 'TCL Smart Television',
            'price': 4450.00,
            'vendor_id': 'vendor1',
            'category': 'Gadgets',
            'image': 'aassets/Category_Home_&_Office/TV1.jpg',
            'description': 'A smart television with good quality'
        },
        {
            'id': '32',
            'title': 'TCL Smart Television',
            'price': 4450.00,
            'vendor_id': 'vendor1',
            'category': 'Gadgets',
            'image': 'aassets/Category_Home_&_Office/TV1.jpg',
            'description': 'A smart television with good quality'
        },
        {
            'id': '33',
            'title': 'TCL Smart Television',
            'price': 4450.00,
            'vendor_id': 'vendor1',
            'category': 'Gadgets',
            'image': 'aassets/Category_Home_&_Office/TV1.jpg',
            'description': 'A smart television with good quality'
        },
        {
            'id': '34',
            'title': 'TCL Smart Television',
            'price': 4450.00,
            'vendor_id': 'vendor1',
            'category': 'Gadgets',
            'image': 'aassets/Category_Home_&_Office/TV1.jpg',
            'description': 'A smart television with good quality'
        },
    ]

# The route is now registered here, which is cleaner than in main.py
@ui.page('/category_ads') 
def category_ads_page():    
    q = ui.context.client.request.query_params
    # This line reads the category from the URL (e.g., ?category=Health)
    category = q.get('category') 

    with ui.column().classes('w-full min-h-screen bg-gray-50'):
        header()

        # This is your entire manual list of products
        all_ads = get_sample_ads()
        
        # This creates a new, smaller list with only the products for the current category
        filtered_ads = [
            ad for ad in all_ads if ad.get('category') == category
        ]

        # --- UI Section ---

        # Category header
        with ui.element('div').classes('w-full bg-gradient-to-r from-blue-600 to-purple-600 py-16'):
            with ui.column().classes('w-full max-w-6xl mx-auto px-8 text-center'):
                ui.label(f'{category} Ads').classes('text-4xl md:text-5xl font-bold text-white mb-4')
                ui.label(f'Discover amazing deals in {category}').classes('text-xl text-blue-100')
        
        # Product grid section
        with ui.column().classes('w-full max-w-6xl mx-auto px-8 pb-16'):
            if not filtered_ads:
                # If the filtered list is empty, show a "not found" message
                with ui.column().classes('w-full text-center py-16'):
                    ui.icon('search_off', size='xl').classes('text-gray-400 mb-4')
                    ui.label('No ads found').classes('text-2xl font-semibold text-gray-600 mb-2')
                    ui.label(f'There are currently no ads in the {category} category.').classes('text-gray-500 mb-6')
                    ui.button('Browse All Categories', on_click=lambda: ui.navigate.to('/')).classes('bg-blue-600 text-white px-6 py-3 rounded-lg hover:bg-blue-700')
            else:
                # If products were found, display them in a grid
                with ui.grid(columns=4).classes('grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6 pt-8'):
                    for ad in filtered_ads:
                        create_ad_card(ad)

def create_ad_card(ad):
    """Create an individual ad card"""
    with ui.card().classes('w-full transform transition-all duration-300 hover:scale-105 hover:shadow-xl overflow-hidden'):
        
        # Ad image from dummy data
        image_url = ad.get('image')
        if image_url:
            ui.image(image_url).classes('w-full h-48 object-cover')
        else:
            # Placeholder for when image is missing
            with ui.element('div').classes('w-full h-48 bg-gray-200 flex items-center justify-center'):
                ui.icon('image').classes('text-4xl text-gray-400')
        
        # Ad content
        with ui.card_section().classes('p-4'):
            # Title/Name
            ui.label(ad.get('title', 'Untitled')).classes('text-lg font-semibold text-gray-800 mb-2 truncate')
            
            # Price
            price = ad.get('price', 0)
            if isinstance(price, (int, float)) and price > 0:
                ui.label(f'₵{price:,.2f}').classes('text-xl font-bold text-green-600 mb-3')
            else:
                ui.label('Price on request').classes('text-lg font-medium text-gray-500 mb-3')
            
            # Action buttons
            with ui.row().classes('w-full gap-2 mt-2'):
                ui.button('View', icon='visibility', on_click=lambda a=ad: show_view_dialog(a)).props('color=primary').classes('w-full')

def add_to_cart(ad, quantity):
    """Placeholder function for adding an item to the cart."""
    ui.notify(f"Added {quantity} of '{ad.get('title')}' to cart!", color='positive')

def view_ad_details(ad):
    """Navigate to ad details page"""
    ad_id = ad.get('id') 
    if ad_id:
        ui.navigate.to(f'/view?id={ad_id}')
    else:
        ui.notify("Cannot view details: Product ID is missing.", color='negative')

def show_view_dialog(ad):
    """Show a dialog with product details, quantity selector, and add to cart button."""
    with ui.dialog() as dialog, ui.card().classes('w-full max-w-md'):
        # Product Image
        ui.image(ad.get('image')).classes('w-full h-64 object-cover')

        with ui.card_section():
            # Product Title
            ui.label(ad.get('title')).classes('text-2xl font-bold')
            # Product Price
            price = ad.get('price', 0)
            ui.label(f'₵{price:,.2f}').classes('text-xl font-semibold text-green-600 mb-4')
            # Product Description
            ui.label(ad.get('description')).classes('text-gray-600')

        with ui.card_actions().classes('justify-between items-center p-4'):
            # Quantity Selector
            quantity_input = ui.number(value=1, min=1, label='Quantity').classes('w-24')
            
            # Add to Cart Button
            ui.button('Add to Cart', icon='add_shopping_cart', on_click=lambda: add_to_cart(ad, quantity_input.value)).props('color=primary')

    dialog.open()
