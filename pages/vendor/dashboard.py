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
    
    # Initialize dark mode functionality for the page
    dark_mode = ui.dark_mode(value=False)
    
    ui.add_head_html('<link href="https://cdnjs.cloudflare.com/libs/font-awesome/6.5.2/css/all.min.css" rel="stylesheet" />')
    
    # Main layout with a header and a left drawer
    with ui.header(elevated=True).classes('bg-white dark:bg-gray-800 text-black dark:text-white'):
        ui.label('Vendor Dashboard').classes('text-xl font-bold')
        ui.space()
        with ui.button(icon='settings', color='primary').props('flat round'):
            with ui.menu():
                ui.menu_item('Toggle Dark Mode', on_click=dark_mode.toggle).props('icon=lightbulb')
                ui.menu_item('Profile').props('icon=person') # Placeholder

    with ui.left_drawer(bordered=True).classes('bg-gray-100 dark:bg-gray-900'):
        show_sidebar()

    # Page content area that will adapt to the header and drawer
    with ui.column().classes('w-full p-4 md:p-8'):
        # KPI Cards Section
        with ui.grid(columns=3).classes('w-full gap-4 mb-8'):
            # KPI Card 1: Total Adverts
            with ui.card().classes('p-6 rounded-lg shadow-lg'):
                ui.label('Total Adverts').classes('text-gray-500 dark:text-gray-400')
                ui.label(f'{total_adverts}').classes('text-4xl font-bold mt-2')
                ui.label('+15% since last month').classes('text-sm text-green-500')

            # KPI Card 2: Active Adverts
            with ui.card().classes('p-6 rounded-lg shadow-lg'):
                ui.label('Active Adverts').classes('text-gray-500 dark:text-gray-400')
                ui.label(f'{active_adverts}').classes('text-4xl font-bold mt-2')
                ui.label('currently running').classes('text-sm text-blue-500')

            # KPI Card 3: Top Category
            with ui.card().classes('p-6 rounded-lg shadow-lg'):
                ui.label('Top Category').classes('text-gray-500 dark:text-gray-400')
                ui.label(f'{top_category}').classes('text-2xl font-bold mt-2 text-purple-500')
                ui.label(f'with {categories_data[top_category]} ads').classes('text-sm text-gray-600 dark:text-gray-300')

        # Charts Section
        with ui.row().classes('w-full gap-4'):
            # Ad Performance Chart
            with ui.card().classes('w-full md:w-2/3 p-6 rounded-lg shadow-lg'):
                ui.label('Ad Performance').classes('text-xl font-bold mb-4')
                ui.echart({
                    'tooltip': {'trigger': 'axis'},
                    'legend': {'data': ['Views', 'Clicks']},
                    'xAxis': {'type': 'category', 'data': [ad['title'] for ad in adverts_data]},
                    'yAxis': {'type': 'value'},
                    'series': [
                        {'name': 'Views', 'data': [ad['views'] for ad in adverts_data], 'type': 'bar'},
                        {'name': 'Clicks', 'data': [ad['clicks'] for ad in adverts_data], 'type': 'bar'}
                    ]
                }).classes('w-full h-72')

            # Category Breakdown Chart
            with ui.card().classes('w-full md:w-1/3 p-6 rounded-lg shadow-lg'):
                ui.label('Category Breakdown').classes('text-xl font-bold mb-4')
                ui.echart({
                    'tooltip': {'trigger': 'item'},
                    'legend': {'orient': 'vertical', 'left': 'left'},
                    'series': [{
                        'name': 'Adverts',
                        'type': 'pie',
                        'radius': ['40%', '70%'],
                        'avoidLabelOverlap': False,
                        'data': [{'value': count, 'name': name} for name, count in categories_data.items()]
                    }]
                }).classes('w-full h-72')
