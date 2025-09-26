import requests
from nicegui import app, ui, run

BASE_URL = "http://127.0.0.1:8000"  # Your backend URL

class ApiClient:
    """A client for making authenticated requests to the backend API."""

    def _get_token(self):
        """Safely retrieves the auth token from user storage."""
        return app.storage.user.get('access_token')

    def _get_auth_headers(self):
        """Constructs authorization headers if a token exists."""
        token = self._get_token()
        if token:
            return {'Authorization': f'Bearer {token}'}
        return {}

    async def _handle_request(self, method, endpoint, **kwargs):
        """A generic, async-friendly method to handle all API requests."""
        url = f"{BASE_URL}{endpoint}"
        try:
            # Use run.cpu_bound for synchronous requests library
            response = await run.cpu_bound(requests.request, method, url, **kwargs)
            response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
            return response.json()
        except requests.exceptions.HTTPError as e:
            # Handle specific HTTP errors, e.g., 401 Unauthorized
            if e.response.status_code == 401:
                ui.notify('Authentication failed. Please log in again.', color='negative')
                app.storage.user.clear()
                ui.navigate.to('/login')
            else:
                ui.notify(f"Error: {e.response.status_code} - {e.response.text}", color='negative')
        except requests.exceptions.RequestException as e:
            # Handle network errors (like the ConnectionError)
            ui.notify(f"Could not connect to the server: {e}", color='negative')
        return None # Return None on failure

    # --- User Endpoints ---
    async def login(self, data: dict):
        return await self._handle_request('post', '/users/login', data=data)

    async def register(self, data: dict):
        return await self._handle_request('post', '/users/register', data=data)

# Create a single instance to be used throughout the app
api = ApiClient()
