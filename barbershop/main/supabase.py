import os
import json
import requests
from django.conf import settings

class SupabaseClient:
    """A client for interacting with Supabase API."""
    
    def __init__(self, url=None, key=None, secret_key=None):
        """Initialize the Supabase client with API credentials."""
        self.url = url or settings.SUPABASE_URL
        self.key = key or settings.SUPABASE_KEY
        self.secret_key = secret_key or settings.SUPABASE_SECRET_KEY
        self.headers = {
            'apikey': self.key,
            'Authorization': f'Bearer {self.key}',
            'Content-Type': 'application/json'
        }
        self.admin_headers = {
            'apikey': self.key,
            'Authorization': f'Bearer {self.secret_key}',
            'Content-Type': 'application/json'
        }

    def _build_url(self, table, id=None):
        """Build the URL for the REST API request."""
        url = f"{self.url}/rest/v1/{table}"
        if id:
            url += f"/{id}"
        return url

    def select(self, table, columns="*", filter_column=None, filter_value=None, order=None, range_from=None, range_to=None):
        """Query data from a table."""
        url = self._build_url(table)
        params = {'select': columns}
        
        if filter_column and filter_value:
            params[filter_column] = f'eq.{filter_value}'
        
        if order:
            params['order'] = order
            
        headers = self.headers.copy()
        if range_from is not None and range_to is not None:
            headers['Range'] = f'{range_from}-{range_to}'
            
        response = requests.get(url, headers=headers, params=params)
        
        if response.status_code >= 400:
            return {'error': response.text}
        
        return response.json()

    def insert(self, table, data):
        """Insert data into a table."""
        url = self._build_url(table)
        response = requests.post(url, headers=self.headers, data=json.dumps(data))
        
        if response.status_code >= 400:
            return {'error': response.text}
        
        return response.json()

    def update(self, table, id, data):
        """Update data in a table."""
        url = self._build_url(table)
        params = {'id': f'eq.{id}'}
        response = requests.patch(url, headers=self.headers, params=params, data=json.dumps(data))
        
        if response.status_code >= 400:
            return {'error': response.text}
        
        return response.json()

    def delete(self, table, id):
        """Delete data from a table."""
        url = self._build_url(table)
        params = {'id': f'eq.{id}'}
        response = requests.delete(url, headers=self.headers, params=params)
        
        if response.status_code >= 400:
            return {'error': response.text}
        
        return {'success': True}

    def custom_query(self, query):
        """Execute a custom SQL query using the admin key."""
        url = f"{self.url}/rest/v1/rpc/execute_sql"
        data = {'sql': query}
        response = requests.post(url, headers=self.admin_headers, data=json.dumps(data))
        
        if response.status_code >= 400:
            return {'error': response.text}
        
        return response.json()

    def auth_signup(self, email, password, user_data=None):
        """Register a new user using Supabase Auth."""
        url = f"{self.url}/auth/v1/signup"
        data = {
            'email': email,
            'password': password
        }
        if user_data:
            data['data'] = user_data
            
        response = requests.post(url, headers=self.headers, data=json.dumps(data))
        
        if response.status_code >= 400:
            return {'error': response.text}
        
        return response.json()

    def auth_login(self, email, password):
        """Log in a user using Supabase Auth."""
        url = f"{self.url}/auth/v1/token?grant_type=password"
        data = {
            'email': email,
            'password': password
        }
        
        response = requests.post(url, headers=self.headers, data=json.dumps(data))
        
        if response.status_code >= 400:
            return {'error': response.text}
        
        return response.json()

    def auth_user(self, jwt):
        """Get user data using the JWT token."""
        headers = self.headers.copy()
        headers['Authorization'] = f'Bearer {jwt}'
        
        url = f"{self.url}/auth/v1/user"
        response = requests.get(url, headers=headers)
        
        if response.status_code >= 400:
            return {'error': response.text}
        
        return response.json()


# Create a global instance for use throughout the app
supabase = SupabaseClient()
