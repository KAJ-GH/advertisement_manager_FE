from nicegui import ui

    # Use ui.header() for a clean header component.
    # with ui.header().classes('w-full items-center justify-between bg-gray-900 text-white shadow-lg'):
    #     ui.label('Gadgetized').classes('text-3xl font-bold')
    #     with ui.row().classes('items-center gap-4'):
    #         ui.button('Sell').classes('px-6 py-2 bg-white text-gray-800 font-semibold rounded-full hover:bg-gray-200 transition-colors')
    #         ui.icon('person', size='2rem').classes('cursor-pointer')

def header():
    with ui.row().classes('w-full items-center justify-between bg-purple-700 text-white shadow-lg'):
        # Logo or site title
        ui.link('BeGadgetized', target='/').classes('text-white text-3xl font-bold')
        
        # Navigation links
        with ui.row().classes('items-center gap-4 uppercase'):
            ui.button('Home', on_click=lambda: ui.navigate.to('/home')).classes('text-white hover:text-green-700 font-semibold')
            ui.link('Collection', target='/view').classes('text-white hover:text-green-700 font-semibold')
            
            
        # Vendor-specific buttons
        with ui.row().classes('items-center gap-4 bg-puple-500'):
            ui.button('Sell', on_click=lambda: ui.navigate.to('/add')).classes('px-6 py-2 bg-purple-400 text-gray-800 font-semibold rounded-full hover:bg-gray-200 transition-colors')
            ui.button(icon='call').classes('bg-purple-600 hover:bg-green-700 text-white rounded-full transition-colors')
            