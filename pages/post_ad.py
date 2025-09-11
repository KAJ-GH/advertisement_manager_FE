from nicegui import ui
import requests
from utils.api import base_url

def save_advert(data):
    response = requests.post(f"{base_url}/advert",data)
    print(response.json())

@ui.page('/add_event')
def post_ad_page():
    flyer_content= None

    def handle_flyer_upload(e):
        nonlocal flyer_content
        flyer_content= e.content

    # Full screen background image container
    with ui.element('div').classes('w-full h-screen relative').style('background-image: url(assests/laptop-1478822_640.jpg); background-size: cover; background-position: center; background-repeat: no-repeat;'):
        
        # Dark overlay for better text readability
        ui.element('div').classes('absolute inset-0 bg-black bg-opacity-50')
        
        # Centered form container
        with ui.element('div').classes('relative z-10 w-full h-full flex items-center justify-center p-8'):
            with ui.card().classes('w-full max-w-md p-6 shadow-2xl rounded-xl bg-white bg-opacity-95 backdrop-blur-sm'):
                ui.label('Add New Advert').classes('text-3xl font-bold mb-6 text-center text-blue-600')

                title_input = ui.input(label='Title', validation={'Title is required': bool}).classes('w-full')
                description_input = ui.textarea(label='Description', validation={'Description is required': bool}).classes('w-full')
                price_input = ui.number(
                    label='Price (GH₵)', value=0.0, format='%.2f',
                    validation={'Price must be above 0': lambda v: v > 0}
                ).classes('w-full')
                category_input = ui.select(
                    ['Entertainment & Sound', 'Home & Office', 'Beauty & Health', 'Mobile Devices', 'Other Gadgets'],
                    label='Category',
                    validation={'Category is required': bool}
                ).classes('w-full')

                ui.label('Image Upload:').classes('text-lg font-semibold mt-4')
                ui.upload(on_upload=handle_flyer_upload).props('accept=".jpg,.png"').classes('w-full')

                # def save_advert():
                #     if not all([title_input.value, description_input.value, category_input.value, price_input.value > 0]):
                #         ui.notify('Please fill in all fields correctly.', type='warning')
                #         return
                #     ui.notify('Advert created successfully!', type='positive')

                ui.button('Save Advert', on_click=lambda:save_advert({"title":title_input.value, "description":description_input.value, "price":price_input.value, "category":category_input.value, "flyer": flyer_content })).classes('bg-green-500 text-white w-full mt-4')
