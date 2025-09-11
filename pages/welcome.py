from nicegui import ui

def welcome_page():
    # Define a custom CSS keyframe animation for the background fade-in
    ui.add_head_html('''
        <style>
            @keyframes fadeIn {
                0% { opacity: 0; }
                100% { opacity: 1; }
            }
            @keyframes slideInUp {
                0% { transform: translateY(50px); opacity: 0; }
                100% { transform: translateY(0); opacity: 1; }
            }
            .background-animation {
                animation: fadeIn 2s ease-in-out forwards;
            }
            .content-animation {
                animation: slideInUp 1s ease-out forwards;
                animation-delay: 1.5s; /* Delay the content animation */
            }
        </style>
    ''')

    with ui.column().classes('w-full h-screen relative flex flex-col justify-center items-center overflow-hidden'):
        # Background image with a fading animation
        ui.image('https://picsum.photos/1920/1080').classes('absolute inset-0 w-full h-full object-cover background-animation')

        # Overlay to make text readable
        ui.label().classes('absolute inset-0 bg-black opacity-50')

        # Main content container with a sliding animation
        with ui.column().classes('relative z-10 text-white text-center items-center p-8 content-animation'):
            ui.label('Welcome to BeGagetized eStore').classes('text-5xl font-bold mb-4')
            ui.label('Discover amazing products and exclusive deals.').classes('text-xl font-light mb-8')

            # The call-to-action button
            ui.button('Your Journey to BeGadgetized starts Here ▶', on_click=lambda: ui.navigate.to('/home')).classes('mt-16 px-12 items-center py-4 text-xl font-semibold bg-blue-600 hover:bg-blue-700 rounded-full transition-colors duration-300 transform hover:scale-105')


# from nicegui import ui

# def welcome_page():
#     """
#     The animated welcome page for the website.
#     """
#     # Use a full-screen container with a dark background.
#     with ui.column().classes('absolute-full flex flex-col items-center justify-center bg-green-500'):
#         # Add a logo or a symbol that represents a gadget.
#         with ui.row().classes('items-center mb-8'):
#             ui.icon('flash_on', size='6rem').classes('text-blue-500 animate-pulse')
#             ui.label('BeGadgetized').classes('text-7xl font-bold text-white tracking-widest')

#         # Add an animation for the tagline.
#         with ui.column().classes('items-center animate-fade-in delay-500'):
#             ui.label("Your Hub for Gadgets, Appliances & Electronics").classes('text-2xl text-gray-400 mt-4')

#         # Add the 'Enter the Store' button with a click handler to navigate.
#         ui.button('Get started here', on_click=lambda: ui.navigate.to('/home')).classes('mt-16 px-12 py-4 text-xl font-semibold bg-blue-600 hover:bg-blue-700 rounded-full transition-colors duration-300 transform hover:scale-105')