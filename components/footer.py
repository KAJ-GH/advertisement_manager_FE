from nicegui import ui

ui.add_head_html('<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css" rel="stylesheet" />')


def footer():
    # Use ui.footer() for a clean footer component.
        with ui.row().classes('w-full justify-around bg-purple-600 mt-24 mb-0'):
            with ui.column().classes('items-center'):
                ui.label('BeGadgetized').classes('text-2xl font-bold mb-2')
                ui.label('Your One-stop Hub for All Gadgets').classes('text-sm text-white font-bold')
            
            with ui.column():
                ui.label('Quick Links').classes('font-bold mb-2')
                ui.link('About Us', '#').classes('text-white hover:text-white')
                ui.link('Contact', '#').classes('text-white hover:text-white')
                ui.link('Terms of Service', '#').classes('text-white hover:text-white')
            
            with ui.column():
                ui.label('Categories').classes('font-bold mb-2')
                ui.link('Health', '#').classes('text-white hover:text-blue')
                ui.link('Office', '#').classes('text-white hover:text-blue')
                ui.link('Home', '#').classes('text-white hover:text-blue')

            # Social media icons section
            with ui.column():
                ui.label('Follow Us').classes('text-lg font-bold mb-2')
            with ui.row().classes("gap-4 justify-center text-4xl text-white"):
                ui.html('<a href="https://facebookcom" target="blank"><i class="fa-brands fa-facebook"></i></a>')
                ui.html('<a href="https://instagram.com" target="blank"><i class="fa-brands fa-instagram"></i></a>')
                ui.html('<a href="https://twitter.com" target="[https://twitter.com](https://twitter.com)"><i class="fa-brands fa-twitter"></i></a>')            
            # with ui.row().classes("text-orange font-bold"):
            #     ui.html('<i class="fa-brands fa-facebook-f"></i>')
            #     ui.html('<i class="fa-brands fa-instagram"></i>')
            #     ui.html('<i class="fa-brands fa-x-twitter"></i>')                

                # with ui.row().classes('gap-4'):
                #     ui.link(target='[https://twitter.com](https://twitter.com)').classes('text-white hover:text-white')
                #     ui.icon('fa-brands fa-twitter', size='md').classes('cursor-pointer')
                #     ui.link(target='[https://facebook.com](https://facebook.com)').classes('text-gray-400 hover:text-white')
                #     ui.icon('fa-brands fa-facebook', size='md').classes('cursor-pointer')
                #     ui.link(target='[https://instagram.com](https://instagram.com)').classes('text-gray-400 hover:text-white')
                #     ui.icon('fa-brands fa-instagram', size='md').classes('cursor-pointer text-white')        
    
            

            ui.label('© 2025 BeGadgetized. All rights reserved.').classes('bg-purple-600 text-white w-full text-center mt-8 text-xs')
    