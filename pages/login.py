from nicegui import ui, app, run
import requests
from utils.api import base_url

_login_btn: ui.button = None

def _run_login(data):
     return requests.post(f'{base_url}/users/login', data=data)


async def _login(data):
    _login_btn.props(add='disable loading')
    response= await run.cpu_bound(_run_login, data)
    print(response.status_code, response.content)
    _login_btn.props(remove='disable loading')
    if response.status_code == 200:
         json_data = response.json()
         app.storage.user['access_token'] = json_data['access_token']
         app.storage.user['id'] = json_data.get('id')  # Store the user ID
         app.storage.user['role'] = 'Vendor' # Assuming all logged-in users are vendors
         return ui.navigate.to('/home')
    


# Placeholder URL for the background image
BG_IMAGE_URL = "https://i.pinimg.com/1200x/0d/a8/73/0da873d8a524030fa1614db0fef840e4.jpg"


@ui.page('/login')
def login_page():
    global _login_btn

    # The main container, centered on the page.
    with ui.row().classes('w-full h-screen justify-center items-center').classes(
        'bg-[url("https://i.pinimg.com/1200x/0d/a8/73/0da873d8a524030fa1614db0fef840e4.jpg")] bg-cover bg-center bg-attachment-fixed'
    ):
        # The white card-like login form.
        with ui.card().classes('w-full max-w-sm p-6 bg-white rounded-xl shadow-2xl'):
            ui.label('Hi, Welcome Back!').classes('text-2xl font-bold text-center mb-6')

            # Username/Email input field with an icon.
            email_input = ui.input(placeholder='username/email').props('dense rounded outlined')
            with email_input.add_slot('before'):
                    ui.icon('person_outline').classes('text-lg text-gray-400')
            
            # Password input field with an icon.
            password_input = ui.input(placeholder='password', password=True, password_toggle_button=True).props('dense rounded outlined')
            with password_input.add_slot('before'):
                    ui.icon('lock_outline').classes('text-lg text-gray-400')

            # Role selection dropdown
            #role_select = ui.select(['User', 'Vendor'], value='User', label='Login as').props('rounded outlined dense').classes('w-full mt-4')

            # Sign In button.
            _login_btn = ui.button('SIGN IN', on_click=lambda: _login({'email': email_input.value, 'password': password_input.value})).props('rounded').classes('w-full mt-4 bg-blue-500 text-white font-semibold rounded-lg shadow-md hover:bg-blue-600 transition duration-300')

            # "Forgot my password" link.
            ui.label('Forgot my password?').classes('text-center text-sm text-blue-500 mt-2 cursor-pointer hover:underline')

            # Back Home button
            ui.button('Back Home', on_click=lambda: ui.navigate.to('/home')).props('outline').classes('w-full mt-4')

            