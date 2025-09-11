from nicegui import ui
from components.header import header
from components.footer import footer

def view_ads_page():
    with ui.column().classes('w-full'):
        #header()
        
        # Main content area with a sidebar for filters
        with ui.row().classes('w-full p-4'):
            # Sidebar for filters
            with ui.column().classes('w-1/4 p-4 bg-gray-100 rounded-lg'):
                ui.label('Filters').classes('text-xl font-bold mb-4')
                ui.label('Price Range').classes('font-semibold')
                with ui.row():
                    ui.input('Min').classes('w-1/2')
                    ui.input('Max').classes('w-1/2')
                
                ui.label('Condition').classes('font-semibold mt-4')
                ui.checkbox('New')
                ui.checkbox('Used')

            # Main product grid
            with ui.column().classes('w-3/4 p-4'):
                ui.label('Electronics').classes('text-2xl font-bold')
                with ui.row().classes('w-full justify-end items-center'):
                    ui.label('Sort By:')
                    ui.select(['Price', 'Newest']).classes('w-32')
                
                # Sample product card. This would be a loop of product data.
                with ui.card().classes('w-64'):
                    ui.image('https://picsum.photos/id/102/300/200').classes('rounded-t-lg')
                    with ui.column().classes('p-2'):
                        ui.label('Product Title').classes('text-lg font-semibold')
                        ui.label('$150').classes('text-xl text-green-600')
                        ui.button('View Details', on_click=lambda: ui.open('/products/1')).classes('mt-2')

                    # with ui.column().classes("w-screen"):
                    #     footer()