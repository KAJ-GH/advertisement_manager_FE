from nicegui import ui
import requests
from utils.api import base_url

def view_ads_page():
    q = ui.context.client.request.query_params
    ad_id = q.get('id')

    if not ad_id:
        ui.notify("No advertisement ID provided.", type='negative')
        ui.navigate.to('/home')
        return

    try:
        response = requests.get(f"{base_url}/advert/{ad_id}")
        response.raise_for_status()
        json_data = response.json()
        
        if "data" not in json_data or not json_data["data"]:
            ui.notify("Advertisement not found.", type='negative')
            ui.navigate.to('/home')
            return
            
        advert = json_data["data"]
    except requests.exceptions.RequestException as e:
        ui.notify(f"Failed to load advertisement: {str(e)}", type='negative')
        ui.navigate.to('/home')
        return
    except (KeyError, ValueError) as e:
        ui.notify("Invalid response from server.", type='negative')
        ui.navigate.to('/home')
        return


    with ui.row().classes('w-full h-screen font-sans'):

        # --- LEFT SIDE: Image ---
        with ui.element('div').classes('flex-1 h-screen relative'):
            ui.image(advert.get('flyer_url', '/assets/placeholder.png')).classes('w-full h-full object-cover')

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
                        ui.label(advert.get('title', 'N/A')).classes('text-lg font-medium text-gray-800')
                    
                    with ui.element('div').classes('p-4 bg-gray-50 rounded-lg'):
                        ui.label('Description').classes('text-sm font-semibold text-gray-600 mb-1')
                        ui.label(advert.get('description', 'N/A')).classes('text-lg text-gray-800')
                    
                    with ui.element('div').classes('p-4 bg-gray-50 rounded-lg'):
                        ui.label('Price').classes('text-sm font-semibold text-gray-600 mb-1')
                        ui.label(f'₵{advert.get("price", 0):.2f}').classes('text-2xl font-bold text-blue-600')
                    
                    with ui.element('div').classes('p-4 bg-gray-50 rounded-lg'):
                        ui.label('Category').classes('text-sm font-semibold text-gray-600 mb-1')
                        ui.label(advert.get('category', 'N/A')).classes('text-lg text-gray-800')

                # Action buttons
                def edit_advert():
                    ui.navigate.to(f'/edit_event?id={ad_id}')
                
                def delete_advert():
                    # Confirmation dialog
                    with ui.dialog() as dialog, ui.card():
                        ui.label('Delete Advertisement').classes('text-xl font-bold mb-4 text-red-600')
                        ui.label('Are you sure you want to delete this advertisement? This action cannot be undone.').classes('mb-6')
                        
                        with ui.row().classes('gap-3 justify-end'):
                            ui.button('Cancel', on_click=dialog.close).classes('bg-gray-500 text-white px-4 py-2 rounded-lg')
                            
                            def confirm_delete():
                                response = requests.delete(f"{base_url}/advert/{ad_id}")
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
                ui.button('Back Home', on_click=lambda: ui.navigate.to('/home')).classes(
                        'flex-1 bg-green-500 text-white py-3 rounded-lg hover:bg-green-600 transition-colors'
                    )
            
