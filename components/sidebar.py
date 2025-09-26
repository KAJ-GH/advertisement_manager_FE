from nicegui import ui

ui.add_head_html('<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css" rel="stylesheet" />')

def show_sidebar(categories_data: dict = {}):
    #ui.label("Vendor's Sidebar goes here")
            with ui.column().classes("items-center mt-8"):
                ui.image("assets/logo.png").classes("w-24 h-24 rounded-full mb-4")
                ui.label("KAJ-GH").classes("text-xl font-bold")
                ui.label("+233 576688347").classes("text-sm text-gray-600")
            
            ui.separator().classes("my-4")

            # Navigation links for sidebar
            ui.label("My Account").classes("font-bold text-lg mb-2")
            ui.button("Make Money", on_click=lambda: ui.navigate.to('/vendor/post_ad'), icon="attach_money").classes("w-full text-gray-700 shadow-none hover:bg-gray-200 justify-start")
            ui.button("Analytics", on_click=lambda: ui.navigate.to('/vendor/dashboard',), icon="bar_chart").classes("w-full text-gray-700 shadow-none hover:bg-gray-200 justify-start")
            ui.button("My Adverts", on_click=lambda: ui.navigate.to('/vendor/vendor_ads'), icon="list_alt").classes("w-full text-blue-500 font-bold shadow-none hover:bg-gray-200 justify-start")
            
            ui.separator().classes("my-4")

            # AI Advice section
            with ui.row().classes("w-full bg-yellow-100 p-2 rounded-lg items-center"):
                ui.icon("lightbulb", size="sm").classes("text-yellow-500")
                with ui.column():
                    ui.label("Advice from BG Bot").classes("font-semibold")
                    ui.label("Learn, how to create an effective ad").classes("text-sm text-gray-700")

            ui.separator().classes("my-4")

            # Adverts summary based on categories
            with ui.column().classes("w-full"):
                if categories_data:
                    ui.label("Adverts Summary").classes("font-semibold text-sm")
                    for category, count in categories_data.items():
                        with ui.row().classes("items-center justify-between w-full"):
                            ui.label(category).classes("text-sm text-gray-700")
                            ui.label(f"({count})").classes("text-sm text-gray-500")

    