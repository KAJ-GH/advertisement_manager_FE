from nicegui import ui

# Mock existing advert data
advert = {
    "title": "Samsung Galaxy S21",
    "description": "Gently used smartphone, excellent condition.",
    "price": 450,
    "category": "Communication Devices"
}

categories = ["Home", "Office", "Health & Beauty", "Communication Devices", "Entertainment"]


def show_edit_event_page():
    def save_changes():
        try:
            price_val = None
            if price_input.value not in (None, ''):
                price_val = float(price_input.value)
        except ValueError:
            ui.notify('Price must be a number', type='negative')
            return

        advert["title"] = title_input.value
        advert["description"] = description_input.value
        advert["price"] = price_val
        advert["category"] = category_dropdown.value

        ui.notify(f"Advert updated: {advert}", type='positive')

    def cancel_edit():
        ui.notify("Edit cancelled. Returning to homepage...", type='warning')

    with ui.card().classes('w-full max-w-md mx-auto mt-10 p-6'):
        ui.label("Edit Advert").classes('text-2xl font-bold mb-4 text-green-700')

        title_input = ui.input("Title", value=advert["title"]).classes("w-full mb-3")
        description_input = ui.textarea("Description", value=advert["description"]).classes("w-full mb-3")

        category_dropdown = ui.select(categories, value=advert["category"], label="Category").classes("w-full mb-3")

        with ui.row().classes("w-full justify-between mt-4"):
            ui.button("Save Changes", on_click=save_changes).props("color=green")
            ui.button("Cancel", on_click=cancel_edit).props("color=grey")


ui.run()
