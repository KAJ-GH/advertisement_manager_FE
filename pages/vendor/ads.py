from nicegui import ui
from components.sidebar import show_sidebar

@ui.page("/vendor/ads")
def show_vendor_ads():
    with ui.row().classes("w-full"):
        with ui.column().classes("w-[20%]"):
            show_sidebar()
        with ui.column().classes("w-[80%]"):
            ui.label("Vendor Ads goes here")  