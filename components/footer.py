from nicegui import ui, ElementFilter

ui.add_head_html('<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css" rel="stylesheet" />')

def footer():
    # Use ui.footer() for a clean footer component.
        with ui.row().classes('w-full justify-around bg-gradient-to-r from-blue-600 to-purple-600'):
            with ui.column().classes('items-center'):
                ui.label('Gadgetized').classes('text-2xl font-bold mb-2')
                ui.label('Your one-stop Hub for All Gadgets').classes('text-sm text-gray-400')
            
            with ui.column():
                ui.label('Quick Links').classes('font-bold mb-2')
                ui.link('About Us', '#').classes('text-gray-400 hover:text-white')
                ui.link('Contact', '#').classes('text-gray-400 hover:text-white')
                ui.link('Terms of Service', '#').classes('text-gray-400 hover:text-white')
            
            with ui.column():
                ui.label('Categories').classes('font-bold mb-2')
                ui.link('Health', '#').classes('text-gray-400 hover:text-white')
                ui.link('Office', '#').classes('text-gray-400 hover:text-white')
                ui.link('Home', '#').classes('text-gray-400 hover:text-white')

            # Social media icons section
            with ui.column():
                ui.label('Follow Us').classes('text-lg font-bold mb-2')
                with ui.row().classes("text-orange font-bold"):
                 ui.html('<i class="fa-brands fa-facebook-f"></i>')
                ui.html('<i class="fa-brands fa-instagram"></i>')
                ui.html('<i class="fa-brands fa-x-twitter"></i>')        
    
            
            ui.label('© 2025 Gadgetized. All rights reserved.').classes('bg-gradient-to-r from-blue-600 to-purple-600 text-white w-full text-center mt-8 text-xs')