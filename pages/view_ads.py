from nicegui import ui
import requests
from utils.api import base_url

def view_ads_page():
    q = ui.context.client.request.query_params
    ad_id = q.get('id')

    response = requests.get(f"{base_url}/advert/{ad_id}")
    json_data = response.json()
    advert = json_data["data"]


    with ui.row().classes('w-full h-screen font-sans'):

        # --- LEFT SIDE: Image ---
        with ui.element('div').classes('flex-1 h-screen relative'):
            ui.image(advert['flyer_url']).classes('w-full h-full object-cover')

            # View text overlay
            # with ui.element('div').classes('absolute inset-0 bg-black bg-opacity-40 flex items-center justify-center'):
            #     with ui.element('div').classes('text-center text-white px-8'):
            #         ui.label('Your Advertisement').classes('text-5xl font-bold mb-4 text-white drop-shadow-lg')
            #         ui.label('Review your listing details and manage your advert').classes('text-xl font-light mb-6 text-white drop-shadow-md')
            #         ui.label('Edit or delete your listing as needed →').classes('text-lg font-medium text-white drop-shadow-md animate-pulse')

        # --- RIGHT SIDE: Advert Details ---
        with ui.element('div').classes('flex-1 h-screen flex items-center justify-center overflow-y-auto'):
            with ui.card().classes('w-full max-w-md p-6 shadow-lg rounded-xl bg-white my-4'):
                ui.label('Advert Details').classes('text-3xl font-bold mb-6 text-center text-blue-600')

                # Display advert information
                with ui.element('div').classes('space-y-4'):
                    with ui.element('div').classes('p-4 bg-gray-50 rounded-lg'):
                        ui.label('Title').classes('text-sm font-semibold text-gray-600 mb-1')
                        ui.label(advert['title']).classes('text-lg font-medium text-gray-800')
                    
                    with ui.element('div').classes('p-4 bg-gray-50 rounded-lg'):
                        ui.label('Description').classes('text-sm font-semibold text-gray-600 mb-1')
                        ui.label(advert['description']).classes('text-lg text-gray-800')
                    
                    with ui.element('div').classes('p-4 bg-gray-50 rounded-lg'):
                        ui.label('Price').classes('text-sm font-semibold text-gray-600 mb-1')
                        ui.label(f'₵{advert["price"]:.2f}').classes('text-2xl font-bold text-blue-600')
                    
                    with ui.element('div').classes('p-4 bg-gray-50 rounded-lg'):
                        ui.label('Category').classes('text-sm font-semibold text-gray-600 mb-1')
                        ui.label(advert['category']).classes('text-lg text-gray-800')

                # Action buttons
                def edit_advert():
                    ui.navigate.to('/edit_event')
                
                def delete_advert():
                    # Confirmation dialog
                    with ui.dialog() as dialog, ui.card():
                        ui.label('Delete Advertisement').classes('text-xl font-bold mb-4 text-red-600')
                        ui.label('Are you sure you want to delete this advertisement? This action cannot be undone.').classes('mb-6')
                        
                        with ui.row().classes('gap-3 justify-end'):
                            ui.button('Cancel', on_click=dialog.close).classes('bg-gray-500 text-white px-4 py-2 rounded-lg')
                            
                            def confirm_delete():
                                response = requests.get(f"{base_url}/advert/{ad_id}")
                                if response.status_code == 200:
                                    ui.notify('Advertisement deleted successfully!', type='positive')
                                    dialog.close()
                                    ui.navigate.to("/home")
                                    # In a real app, this would delete from database and redirect
                            
                            ui.button('Delete', on_click=confirm_delete).classes('bg-red-500 text-white px-4 py-2 rounded-lg')
                    
                    dialog.open()

                with ui.row().classes('w-full gap-2 mt-4'):
                    ui.button('Edit Advert', icon='edit', on_click=edit_advert).classes(
                        'flex-1 bg-blue-600 text-white py-2 rounded-lg hover:bg-blue-700 transition-colors'
                    )
                    ui.button('Delete Advert', icon='delete', on_click=delete_advert).classes(
                        'flex-1 bg-red-500 text-white py-2 rounded-lg hover:bg-red-600 transition-colors'
                    )
# from components.header import header
# from components.footer import footer

# def view_ads_page():
#     with ui.column().classes('w-full'):
#         #header()
        
#         # Main content area with a sidebar for filters
#         with ui.row().classes('w-full p-4'):
#             # Sidebar for filters
#             with ui.column().classes('w-1/4 p-4 bg-gray-100 rounded-lg'):
#                 ui.label('Filters').classes('text-xl font-bold mb-4')
#                 ui.label('Price Range').classes('font-semibold')
#                 with ui.row():
#                     ui.input('Min').classes('w-1/2')
#                     ui.input('Max').classes('w-1/2')
                
#                 ui.label('Condition').classes('font-semibold mt-4')
#                 ui.checkbox('New')
#                 ui.checkbox('Used')

#             # Main product grid
#             with ui.column().classes('w-3/4 p-4'):
#                 ui.label('Electronics').classes('text-2xl font-bold')
#                 with ui.row().classes('w-full justify-end items-center'):
#                     ui.label('Sort By:')
#                     ui.select(['Price', 'Newest']).classes('w-32')
                
#                 # Sample product card. This would be a loop of product data.
#                 with ui.card().classes('w-64'):
#                     ui.image('https://picsum.photos/id/102/300/200').classes('rounded-t-lg')
#                     with ui.column().classes('p-2'):
#                         ui.label('Product Title').classes('text-lg font-semibold')
#                         ui.label('$150').classes('text-xl text-green-600')
#                         ui.button('View Details', on_click=lambda: ui.open('/products/1')).classes('mt-2')

#                     # with ui.column().classes("w-screen"):
#                     #     footer()