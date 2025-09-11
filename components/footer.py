from nicegui import ui, ElementFilter

def footer():
    # Use ui.footer() for a clean footer component.
        with ui.row().classes('w-full justify-around bg-blue-500'):
            with ui.column().classes('items-center'):
                ui.label('Gadgetized').classes('text-2xl font-bold mb-2')
                ui.label('Your one-stop shop for electronics').classes('text-sm text-gray-400')
            
            with ui.column():
                ui.label('Quick Links').classes('font-bold mb-2')
                ui.link('About Us', '#').classes('text-gray-400 hover:text-white')
                ui.link('Contact', '#').classes('text-gray-400 hover:text-white')
                ui.link('Terms of Service', '#').classes('text-gray-400 hover:text-white')
            
            with ui.column():
                ui.label('Categories').classes('font-bold mb-2')
                ui.link('Health', '#').classes('text-white-400 hover:text-white')
                ui.link('Office', '#').classes('text-white-400 hover:text-white')
                ui.link('Home', '#').classes('text-white-400 hover:text-white')

            # Social media icons section
            with ui.column():
                ui.label('Follow Us').classes('text-lg font-bold mb-2')
                with ui.row().classes('gap-4'):
                    ui.link(target='[https://twitter.com](https://twitter.com)').classes('text-white hover:text-white')
                    ui.icon('fa-brands fa-twitter', size='md').classes('cursor-pointer')
                    ui.link(target='[https://facebook.com](https://facebook.com)').classes('text-gray-400 hover:text-white')
                    ui.icon('fa-brands fa-facebook', size='md').classes('cursor-pointer')
                    ui.link(target='[https://instagram.com](https://instagram.com)').classes('text-gray-400 hover:text-white')
                    ui.icon('fa-brands fa-instagram', size='md').classes('cursor-pointer text-white')        
    
            

            ui.label('© 2025 Gadgetized. All rights reserved.').classes('bg-blue-500 text-white w-full text-center mt-8 text-xs')
    
    
        # with ui.row().classes('w-full max-w-6xl mx-auto items-start justify-between p-4'):
        #     # Quick links section
        #     with ui.column():
        #         ui.label('Quick Links').classes('text-lg font-bold mb-2')
        #         ui.link('Home', target='/').classes('text-gray-400 hover:text-white')
        #         ui.link('Product Categories', target='/categories').classes('text-gray-400 hover:text-white')
        #         ui.link('About Us', target='/about').classes('text-gray-400 hover:text-white')
        #         ui.link('Contact', target='/contact').classes('text-gray-400 hover:text-white')

        #     # Social media icons section
        #     with ui.column():
        #         ui.label('Follow Us').classes('text-lg font-bold mb-2')
        #         with ui.row().classes('gap-4'):
        #             ui.link(target='[https://twitter.com](https://twitter.com)').classes('text-white hover:text-white')
        #             ui.icon('fa-brands fa-twitter', size='md').classes('cursor-pointer')
        #             ui.link(target='[https://facebook.com](https://facebook.com)').classes('text-gray-400 hover:text-white')
        #             ui.icon('fa-brands fa-facebook', size='md').classes('cursor-pointer')
        #             ui.link(target='[https://instagram.com](https://instagram.com)').classes('text-gray-400 hover:text-white')
        #             ui.icon('fa-brands fa-instagram', size='md').classes('cursor-pointer')

        # # Copyright section
        # with ui.row().classes('w-full justify-center p-4 border-t border-gray-700 mt-4'):
        #     ui.label('© 2025 Tonaton. All Rights Reserved.').classes('text-gray-500 text-sm')