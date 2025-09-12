from nicegui import ui

    
def header():
    with ui.row().classes('w-full items-center justify-between bg-gradient-to-r from-blue-500 to-purple-600 text-white shadow-lg backdrop-blur-sm'):
        # Logo or site title
        ui.link('BeGadgetized', target='/').classes('text-white text-3xl font-bold')
        
        # Navigation links
        with ui.row().classes('items-center gap-4 uppercase'):
            ui.link('Home', target='/home').classes('text-white hover:text-green-700 font-semibold')
            ui.link('All Ads').classes('text-white hover:text-green-700 font-semibold')
            ui.link('Contact').classes('text-white hover:text-green-700 font-semibold')
            
            
        # Vendor-specific buttons
        with ui.row().classes('items-center gap-4 bg-puple-500'):
            ui.button('Sell', on_click=lambda: ui.navigate.to('/add')).classes('px-6 py-2 bg-purple-400 text-gray-800 font-semibold rounded-full hover:bg-gray-200 transition-colors')