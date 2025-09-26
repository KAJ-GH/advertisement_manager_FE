import random
from nicegui import app, ui
from components.sidebar import show_sidebar
from components.footer import footer

# Dummy data
adverts_data = [
    {"id": 1, "title": "Gaming Laptop", "views": 1200, "clicks": 80, "status": "active"},
    {"id": 2, "title": "Smartwatch", "views": 850, "clicks": 45, "status": "active"},
    {"id": 3, "title": "Ergonomic Chair", "views": 980, "clicks": 65, "status": "expired"},
    {"id": 4, "title": "Bluetooth Speaker", "views": 1500, "clicks": 110, "status": "active"},
]
categories_data = {"Electronics": 3, "Wearables": 1, "Furniture": 1, "Apparel": 1}

# Calculate KPIs
total_adverts = len(adverts_data)
active_adverts = sum(1 for ad in adverts_data if ad['status'] == 'active')
top_category = max(categories_data, key=categories_data.get)

@ui.page("/vendor/dashboard")
def show_vendor_dashboard():
    # --- Role Protection ---
   # if not app.storage.user.get('authenticated') or app.storage.user.get('role') != 'Vendor':
     #   ui.notify('Access denied. Please log in as a vendor.', color='negative')
     #   ui.navigate.to('/login')
      #  return
    # --- End of Role Protection ---

    ui.add_head_html('<link href="https://cdnjs.cloudflare.com/libs/font-awesome/6.5.2/css/all.min.css" rel="stylesheet" />')
    
    # Header - a top-level element
    with ui.header().classes("w-full bg-white text-gray-800 shadow-md").props("elevated"):
        ui.label("Detailed Dashboard").classes("text-xl font-bold")
        ui.space()
        with ui.button(icon="settings").props("flat round"):
            with ui.menu():
                ui.menu_item('Light/dark Mode', on_click=ui.dark_mode.toggle).props('icon="lightbulb"')
                ui.menu_item("Profile", on_click=lambda: ui.navigate.to('/profile'))

    # Left Drawer (Sidebar) - a top-level element
    # Use ui.left_drawer() for a fixed, responsive sidebar
    with ui.left_drawer().classes("bg-gray-100 p-4").props("bordered no-swipe"):
        show_sidebar()
    
    # Main Content Area - this should be the primary content within the page
    # It will automatically adjust to the presence of the header and drawer
    with ui.column().classes("flex-grow p-8"):
        # KPI Cards
        with ui.grid(columns=3).classes("w-full gap-4 mb-8"):
            ui.card().classes("p-6 rounded-lg shadow-xl").add_slot('default', f"""
                <div class="text-gray-500">Total Adverts</div>
                <div class="text-4xl font-bold mt-2">{total_adverts}</div>
                <div class="text-sm text-green-500">+15% since last month</div>
            """)
            ui.card().classes("p-6 rounded-lg shadow-xl").add_slot('default', f"""
                <div class="text-gray-500">Active Adverts</div>
                <div class="text-4xl font-bold mt-2">{active_adverts}</div>
                <div class="text-sm text-blue-500">currently running</div>
            """)
            ui.card().classes("p-6 rounded-lg shadow-xl").add_slot('default', f"""
                <div class="text-gray-500">Top Category</div>
                <div class="text-2xl font-bold mt-2 text-purple-500">{top_category}</div>
                <div class="text-sm text-gray-600">with {categories_data[top_category]} ads</div>
            """)
        
        # Detailed Charts
        with ui.row().classes("w-full gap-4"):
            with ui.card().classes("w-2/3 p-6 rounded-lg shadow-xl"):
                ui.label("Ad Performance").classes("text-xl font-bold mb-4")
                ui.echart({
                    'xAxis': {'type': 'category', 'data': [ad['title'] for ad in adverts_data]},
                    'yAxis': {'type': 'value'},
                    'series': [
                        {'name': 'Views', 'data': [ad['views'] for ad in adverts_data], 'type': 'bar'},
                        {'name': 'Clicks', 'data': [ad['clicks'] for ad in adverts_data], 'type': 'bar'}
                    ]
                }).classes("w-full h-72")
            
            with ui.card().classes("w-1/3 p-6 rounded-lg shadow-xl"):
                ui.label("Category Breakdown").classes("text-xl font-bold mb-4")
                ui.echart({
                    'series': [{
                        'name': 'Adverts',
                        'type': 'pie',
                        'radius': ['40%', '70%'],
                        'data': [{'value': count, 'name': name} for name, count in categories_data.items()]
                    }]
                }).classes("w-full h-72")
    
    # Footer - a top-level element
    footer()
