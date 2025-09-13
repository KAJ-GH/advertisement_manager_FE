from nicegui import ui

    
def header():
    #A modern, semi-transparent header that sits on top of hero sections.
    with ui.row().classes(
        'w-full items-center justify-between px-8 py-3 '
        'bg-gradient-to-r from-blue-900 to-purple-700 bg-opacity-25 backdrop-blur-sm text-white '
        'border-b border-gray-100 border-opacity-10'
    ):
        # Clickable logo that navigates to the welcome page
        with ui.link(target='/').classes('flex items-center gap-2'):
            ui.image('/assets/logo.png').classes('w-8 h-8')
            ui.label('BeGadgetized').classes('text-2xl font-bold hover:text-purple-300 transition-colors')
        
        # Navigation links
        with ui.row().classes('items-center gap-8 uppercase text-sm font-semibold'):
            ui.link('Home', target='/home').classes('hover:text-purple-300 transition-colors')
            # This link can be pointed to a dedicated "all ads" page in the future
            ui.link('All Ads', target='/home').classes('hover:text-purple-300 transition-colors')
            ui.link('Contact', target='#').classes('hover:text-purple-300 transition-colors')
            
        # Vendor-specific buttons
        with ui.row().classes('items-center'):
            # Corrected navigation to '/add_event' and improved button style
            ui.button('Sell', icon='add_circle_outline', on_click=lambda: ui.navigate.to('/add_event')).classes(
                'bg-purple-500 hover:bg-purple-600 text-white font-semibold rounded-full transition-colors'
            )