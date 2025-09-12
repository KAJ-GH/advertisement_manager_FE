from nicegui import ui

# Dummy data
advert = {
    'title': 'Smartphone',
    'description': 'Latest model with great features',
    'price': 999.99,
    'category': 'Mobile Devices',
}

@ui.page('/edit_event')
def edit_ad_page():
    # Full screen background image container
    with ui.element('div').classes('w-full h-screen relative').style('background-image: url(assests/ecommerce-3640321_1280.jpg); background-size: cover; background-position: center; background-repeat: no-repeat;'):
        
        # Dark overlay for better text readability
        #ui.element('div').classes('absolute inset-0 bg-black bg-opacity-50')
        
        # Centered form container
        with ui.element('div').classes('relative z-10 w-full h-full flex items-center justify-center p-8'):
            with ui.card().classes('w-full max-w-md p-6 shadow-2xl rounded-xl bg-white bg-opacity-95 backdrop-blur-sm'):
                ui.label('Edit Advert').classes('text-3xl font-bold mb-6 text-center text-blue-600')

                # Pre-filled form fields
                title_input = ui.input(label='Title', value=advert['title'], validation={'Title is required': bool}).classes('w-full')
                description_input = ui.textarea(label='Description', value=advert['description'], validation={'Description is required': bool}).classes('w-full')
                price_input = ui.number(
                    label='Price (₵)', value=advert['price'], format='%.2f',
                    validation={'Price must be above 0': lambda v: v > 0}
                ).classes('w-full')
                category_input = ui.select(
                    ['Entertainment & Sound', 'Home & Office', 'Beauty & Health', 'Mobile Devices', 'Other Gadgets'],
                    label='Category',
                    value=advert['category'],
                    validation={'Category is required': bool}
                ).classes('w-full')

                ui.label('Image Upload:').classes('text-lg font-semibold mt-4')
                ui.upload().props('accept=".jpg,.png"').classes('w-full')

                # Save (update) button
                def update_advert():
                    if not all([title_input.value, description_input.value, category_input.value, price_input.value > 0]):
                        ui.notify('Please fill in all fields correctly.', type='warning')
                        return
                    
                    advert['title'] = title_input.value
                    advert['description'] = description_input.value
                    advert['price'] = price_input.value
                    advert['category'] = category_input.value

                    print("Updated advert:", advert) 
                    ui.notify('Advert updated successfully!', type='positive')

                with ui.row().classes('w-full gap-3 mt-4'):
                    ui.button('Cancel', icon='close', on_click=lambda: ui.navigate.to('/home')).classes(
                        'flex-1 bg-gray-500 text-white py-3 rounded-lg hover:bg-gray-600 transition-colors'
                    )
                    ui.button('Update Advert', on_click=update_advert).classes(
                        'flex-1 bg-green-500 text-white py-3 rounded-lg hover:bg-green-600 transition-colors'
                    )
