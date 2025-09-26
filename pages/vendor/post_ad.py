from nicegui import ui,run,app
import requests
from utils.api import base_url
from components.sidebar import show_sidebar


_post_ad_btn: ui.button = None

def _run_post_ad(data, files,token):
    return requests.post(f'{base_url}/advert', 
                         data=data, files=files, 
                         headers={'Authorization': f'Bearer {token}'})


async def handle_save(data, files):
    _post_ad_btn.props(add='disable loading')
    response= await run.cpu_bound(_run_post_ad, data, files, app.storage.user.get('access_token'))
    print(response.status_code, response.content)
    _post_ad_btn.props(remove='disable loading')

    #
    token = app.storage.user.get('access_token')
    if not token:
        ui.notify('Authentication error. Please log in again.', color='negative')
        _post_ad_btn.props(remove='disable loading')
        return


def handle_save(data, flyer_content):
    """Handles the ad creation process, including UI feedback and API call."""
    if not all(data.values()) or not flyer_content:
        ui.notify('Please fill in all fields and upload an image.', type='warning')
        return


@ui.page("/vendor/post_ad")
def post_ad_page():
    global _post_ad_btn
    flyer_content = None

    def handle_flyer_upload(e):
        nonlocal flyer_content
        flyer_content = e.content

    # --- Role Protection ---
    #if not app.storage.user.get('authenticated') or app.storage.user.get('role') != 'Vendor':
       # ui.notify('Access denied. Please log in as a vendor.', color='negative')
      #  ui.navigate.to('/login')
      #  return
  
    # Main container for the two-column layout
    with ui.row().classes("w-full h-screen p-0 m-0 flex-nowrap"):
        # --- Sidebar Column ---
        with ui.column().classes("w-[20%] h-full bg-gray-100 p-4"):
            show_sidebar()
        
        # --- Main Content Column ---
        with ui.column().classes("w-[80%] h-full"):
            # Full screen background image container for the content area
            with ui.element('div').classes('w-full h-full relative').style('background-image: url(/assets/laptop-1478822_640.jpg); background-size: cover; background-position: center;'):
                # Centered form container
                with ui.element('div').classes('w-full h-full flex items-center justify-center p-8'):
                    with ui.card().classes("w-full max-w-md p-6 shadow-2xl rounded-xl bg-white bg-opacity-95 backdrop-blur-sm"):
                        ui.label("Add New Advert").classes("text-3xl font-bold mb-6 text-center text-blue-600")

                        title_input = ui.input(
                            label="Title", validation={"Title is required": bool}
                        ).classes("w-full").props('rounded-md outlined dense')

                        description_input = ui.textarea(
                            label="Description", validation={"Description is required": bool}
                        ).classes("w-full").props('rounded-md outlined dense')

                        price_input = ui.number(
                            label="Price (GH₵)", value=0.0, format="%.2f",
                            validation={"Price must be above 0": lambda v: v > 0},
                        ).classes("w-full").props('rounded-md outlined dense')

                        category_input = ui.select(
                            ['Mobile Devices', 'Home & Office', 'Entertainment & Sound', 'Health & Beauty', 'Other Gadgets'],
                            label="Category", validation={"Category is required": bool},
                        ).classes("w-full").props('rounded-md outlined dense')

                        ui.label("Image Upload:").classes("text-lg font-semibold mt-4")
                        ui.upload(on_upload=handle_flyer_upload).props('accept=".jpg,.png"').classes("w-full")

                        with ui.row().classes("w-full gap-3 mt-4"):
                            _post_ad_btn = ui.button("Save Advert", on_click=lambda: handle_save(
                                data={
                                    "title": title_input.value,
                                    "description": description_input.value,
                                    "price": price_input.value,
                                    "category": category_input.value,
                                },
                                flyer_content=flyer_content
                            )).classes("flex-1 bg-green-500 text-white py-3 rounded-lg hover:bg-green-600 transition-colors")
                            
                            ui.button("Cancel", on_click=lambda: ui.navigate.to("/vendor/vendor_ads")).classes( 
                                "flex-1 bg-gray-500 text-white py-3 rounded-lg hover:bg-gray-600 transition-colors"
                            ).props('outline')
