from nicegui import ui

def footer():
    with ui.column().classes('w-full bg-gray-900 text-white py-8'):
        # Main footer container
        with ui.row().classes('w-full max-w-6xl mx-auto items-start justify-between p-4'):
            # Quick links section
            with ui.column():
                ui.label('Quick Links').classes('text-lg font-bold mb-2')
                ui.link('Home', target='/').classes('text-gray-400 hover:text-white')
                ui.link('Product Categories', target='/categories').classes('text-gray-400 hover:text-white')
                ui.link('About Us', target='/about').classes('text-gray-400 hover:text-white')
                ui.link('Contact', target='/contact').classes('text-gray-400 hover:text-white')

            # Social media icons section
            with ui.column():
                ui.label('Follow Us').classes('text-lg font-bold mb-2')
                with ui.row().classes('gap-4'):
                    ui.link(target='[https://twitter.com](https://twitter.com)').classes('text-gray-400 hover:text-white')
                    ui.icon('fa-brands fa-twitter', size='md').classes('cursor-pointer')
                    ui.link(target='[https://facebook.com](https://facebook.com)').classes('text-gray-400 hover:text-white')
                    ui.icon('fa-brands fa-facebook', size='md').classes('cursor-pointer')
                    ui.link(target='[https://instagram.com](https://instagram.com)').classes('text-gray-400 hover:text-white')
                    ui.icon('fa-brands fa-instagram', size='md').classes('cursor-pointer')

        # Copyright section
        with ui.row().classes('w-full justify-center p-4 border-t border-gray-700 mt-4'):
            ui.label('© 2025 Tonaton. All Rights Reserved.').classes('text-gray-500 text-sm')