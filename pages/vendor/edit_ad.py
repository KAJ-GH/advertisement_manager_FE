from nicegui import ui
import requests
from components.sidebar import show_sidebar
from utils.api import base_url

@ui.page('/vendor/edit_ad')
def edit_ad_page():
    q = ui.context.client.request.query_params
    ad_id = q.get('id')
    new_flyer_content = None

    if not ad_id:
        ui.notify("No advertisement ID provided.", type='negative')
        ui.navigate.to('/home')
        return

    # Fetch the existing ad data from the API
    try:
        response = requests.get(f"{base_url}/advert/{ad_id}")
        response.raise_for_status()
        advert = response.json().get("data", {})
    except requests.exceptions.RequestException as e:
        ui.notify(f"Failed to load ad data: {e}", type='negative')
        advert = {} # Use an empty dict on failure

    def handle_flyer_upload(e):
        nonlocal new_flyer_content
        new_flyer_content = e.content
    
    
    with ui.row().classes("w-full"):
        with ui.column().classes("w-[20%]"):
            show_sidebar()
        with ui.column().classes("w-[80%]"):
  
    # Full screen background image container
            with ui.element('div').classes('w-full h-screen relative').style('background-image: url(/assets/ecommerce-3640321_1280.jpg); background-size: cover; background-position: center; background-repeat: no-repeat;'):
                
                # Centered form container
                with ui.element('div').classes('relative z-10 w-full h-full flex items-center justify-center p-8'):
                    with ui.card().classes('w-full max-w-md p-6 shadow-2xl rounded-xl bg-white bg-opacity-95 backdrop-blur-sm'):
                        ui.label('Edit Advert').classes('text-3xl font-bold mb-6 text-center text-blue-600')

                        # Display current image
                        ui.label('Current Image:').classes('text-lg font-semibold')
                        ui.image(advert.get('flyer_url', 'assets/placeholder.png')).classes('w-full rounded-lg mb-4 h-48 object-cover')

                        # Pre-filled form fields
                        title_input = ui.input(label='Title', value=advert.get('title', ''), validation={'Title is required': bool}).classes('w-full')
                        description_input = ui.textarea(label='Description', value=advert.get('description', ''), validation={'Description is required': bool}).classes('w-full')
                        price_input = ui.number(
                            label='Price (₵)', value=advert.get('price', 0.0), format='%.2f',
                            validation={'Price must be above 0': lambda v: v > 0}
                        ).classes('w-full')
                        category_input = ui.select(
                            # This list is now the single source of truth for categories.
                            # It includes legacy values like 'phone' to prevent errors.
                            [
                                'Mobile Devices',
                                'Home & Office',
                                'Entertainment & Sound',
                                'Health & Beauty',
                                'Other Gadgets',
                            ],
                            label='Category',
                            value=advert.get('category', ''),
                            validation={'Category is required': bool}
                        ).classes('w-full')

                        ui.label('Upload New Image (Optional):').classes('text-lg font-semibold mt-4')
                        ui.upload(on_upload=handle_flyer_upload).props('accept=".jpg,.png"').classes('w-full')

                        # Save (update) button
                        def update_advert():
                            if not all([title_input.value, description_input.value, category_input.value, price_input.value > 0]):
                                ui.notify('Please fill in all fields correctly.', type='warning')
                                return
                            updated_data = {
                                'title': title_input.value,
                                'description': description_input.value,
                                'price': price_input.value,
                                'category': category_input.value,
                            }
                            try:
                                if new_flyer_content:
                                    # If a new image is uploaded, send as multipart/form-data
                                    files = {"flyer": ("flyer_image.jpg", new_flyer_content, "image/jpeg")}
                                    response = requests.put(f"{base_url}/advert/{ad_id}", data=updated_data, files=files)
                                else:
                                    # If no new image, send as application/json
                                    # This prevents the backend from nullifying the existing flyer_url
                                    response = requests.put(f"{base_url}/advert/{ad_id}", json=updated_data)

                                response.raise_for_status()
                                ui.notify('Advert updated successfully!', type='positive')
                                ui.navigate.to(f'/view?id={ad_id}')

                            except requests.exceptions.RequestException as e:
                                ui.notify(f"Failed to update advert: {e}", type='negative')

                        with ui.row().classes('w-full gap-3 mt-4'):
                            ui.button('Cancel', icon='close', on_click=lambda: ui.navigate.to('/home')).classes(
                                'flex-1 bg-gray-500 text-white py-3 rounded-lg hover:bg-gray-600 transition-colors'
                            )
                            ui.button('Update Advert', on_click=update_advert).classes(
                                'flex-1 bg-green-500 text-white py-3 rounded-lg hover:bg-green-600 transition-colors'
                            )
