from nicegui import ui
import requests
from utils.api import base_url
from components.sidebar import show_sidebar



def save_advert(data: dict):
    """
    Saves a new advertisement by sending a multipart/form-data request.
    The file is separated from other data and sent via the `files` parameter.
    """
    flyer_content = data.pop("flyer", None)
    files = None
    if flyer_content:
        # The backend expects a file named 'flyer'.
        # The tuple format is (filename, file_object, content_type).
        files = {"flyer": ("flyer_image.jpg", flyer_content, "image/jpeg")}
    
    return requests.post(f"{base_url}/advert", data=data, files=files)


@ui.page("/add_event")
def post_ad_page():
    flyer_content = None

    def handle_flyer_upload(e):
        nonlocal flyer_content
        flyer_content = e.content

    # Full screen background image container
    with ui.row().classes("w-full"):
        with ui.column().classes("w-[20%]"):
            show_sidebar()
        with ui.column().classes("w-[80%]"):
  
            with ui.element("div").classes("w-full h-screen relative").style(
                "background-image: url(assests/laptop-1478822_640.jpg); background-size: cover; background-position: center; background-repeat: no-repeat;"
            ):

                # Centered form container
                with ui.element("div").classes(
                    "relative z-10 w-full h-full flex items-center justify-center p-8"
                ):
                    with ui.card().classes(
                        "w-full max-w-md p-6 shadow-2xl rounded-xl bg-white bg-opacity-95 backdrop-blur-sm"
                    ):
                        ui.label("Add New Advert").classes(
                            "text-3xl font-bold mb-6 text-center text-blue-600"
                        )

                        title_input = ui.input(
                            label="Title", validation={"Title is required": bool}
                        ).classes("w-full")
                        description_input = ui.textarea(
                            label="Description", validation={"Description is required": bool}
                        ).classes("w-full")
                        price_input = ui.number(
                            label="Price (GH₵)",
                            value=0.0,
                            format="%.2f",
                            validation={"Price must be above 0": lambda v: v > 0},
                        ).classes("w-full")
                        category_input = ui.select(
                            [
                                'Mobile Devices',
                                'Home & Office',
                                'Entertainment & Sound',
                                'Health & Beauty',
                                'Other Gadgets',
                            ],
                            label="Category",
                            validation={"Category is required": bool},
                        ).classes("w-full")

                        ui.label("Image Upload:").classes("text-lg font-semibold mt-4")
                        ui.upload(on_upload=handle_flyer_upload).props(
                            'accept=".jpg,.png"'
                        ).classes("w-full")

                        def handle_save():
                            if not all([title_input.value, description_input.value, category_input.value, price_input.value > 0, flyer_content]):
                                ui.notify('Please fill in all fields and upload an image.', type='warning')
                                return
                            
                            ad_data = {
                                "title": title_input.value,
                                "description": description_input.value,
                                "price": price_input.value,
                                "category": category_input.value,
                                "flyer": flyer_content,
                            }
                            
                            try:
                                response = save_advert(ad_data)
                                response.raise_for_status()
                                ui.notify('Advert created successfully!', type='positive')
                                ui.navigate.to('/home')
                            except requests.exceptions.RequestException as e:
                                ui.notify(f"Failed to create advert: {e}", type='negative')

                        with ui.row().classes("w-full gap-3 mt-4"):
                            ui.button("Save Advert", on_click=handle_save).classes(
                                "flex-1 bg-gray-500 text-white py-3 rounded-lg hover:bg-gray-600 transition-colors"
                            )
                        ui.button(
                            "Back Home", on_click=lambda: ui.navigate.to("/home")
                        ).classes(
                            "flex-1 bg-green-500 text-white py-3 rounded-lg hover:bg-green-600 transition-colors"
                        )
