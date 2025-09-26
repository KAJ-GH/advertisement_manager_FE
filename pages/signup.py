from nicegui import ui, app, run
import requests
from utils.api import base_url

def _run_signup(data):
     return requests.post(f'{base_url}/users/register', data=data)


async def _signup(data):
    response= await run.cpu_bound(_run_signup, data)
    print(response.status_code, response.content)
    if response.status_code == 200:
         ui.notify('Signup successful! Please log in.', color='positive')
         return ui.navigate.to('/login')
    elif response.status_code == 409:
         return ui.notify(message='user already exixts', type='warning')


@ui.page('/signup')
def signup_page():
    ui.add_head_html('<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css" rel="stylesheet" />')
    with ui.row().classes('w-full h-screen no-wrap'):
        # Left Panel: Welcome Back!
        with ui.column().classes('w-2/5 h-full bg-blue-700 text-white flex flex-col justify-center items-center p-8'):
            ui.label('WELCOME BACK!').classes('text-4xl font-bold mb-4')
            ui.label('Already have an account? Click below to continue using the service.').classes('text-center text-lg mb-8')
            ui.button('Login', on_click=lambda: ui.navigate.to('/login')).props('outline rounded size=lg').classes('border-white text-white hover:bg-white hover:text-blue-700 transition duration-300')

        # Right Panel: Create Account
        with ui.column().classes('w-3/5 h-full bg-white flex flex-col justify-center items-center p-8'):
            ui.label('Create Account').classes('text-4xl font-bold text-gray-800 mb-6')

            with ui.row().classes('space-x-4 mb-4'):
                ui.icon('fab fa-facebook').classes('text-blue-600 text-3xl cursor-pointer hover:text-blue-800')
                ui.icon('fab fa-google').classes('text-blue-400 text-3xl cursor-pointer hover:text-blue-600')
                ui.icon('fab fa-instagram').classes('text-blue-700 text-3xl cursor-pointer hover:text-blue-900')

            ui.label('or use your email account').classes('text-gray-500 mb-6')

            # Username Input
            username_input = ui.input(placeholder='Username').props('rounded outlined dense')
            with username_input.add_slot("before"):
                    ui.icon('person_outline').classes('text-lg text-gray-400')
            username_input.classes('w-3/5 mb-4')

            #Email Input
            email_input = ui.input(placeholder='Email').props('rounded outlined dense')
            with email_input.add_slot('before'):
                    ui.icon('email').classes('text-lg text-gray-400')
            email_input.classes('w-3/5 mb-4')


            # Password Input
            password_input = ui.input(placeholder='Password', password=True, password_toggle_button=True).props('rounded outlined dense')
            with password_input.add_slot('before'):
                    ui.icon('lock_outline').classes('text-lg text-gray-400')
            password_input.classes('w-3/5 mb-4')
            
            # Select between user and a vendor
            # Role selection dropdown
            role = ui.select(['User', 'Vendor'], label='I am a').props('rounded outlined dense').classes('w-3/5 mb-8')

            # Sign Up Button
            ui.button('SIGN UP', on_click=lambda:_signup({
                'username': username_input.value,
                'email': email_input.value,
                'password': password_input.value,
                #'role': role.value
                }
            )).classes('bg-blue-700 text-white px-8 py-3 rounded-full shadow-lg hover:bg-blue-800 transition duration-300')

            #Already have an account
            #with ui.row
