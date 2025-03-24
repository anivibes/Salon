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
        # We'll need to execute the SQL statements one by one since there's no bulk execute function
        statements = [stmt.strip() for stmt in query.split(';') if stmt.strip()]
        results = []
        
        for statement in statements:
            if not statement:
                continue
                
            # Determine if it's a SELECT query
            is_select = statement.lower().startswith('select')
            
            if is_select:
                # For SELECT queries, use the REST API
                # Extract the table name from the query
                # This is a simplified approach and might not work for complex queries
                try:
                    from_parts = statement.lower().split('from')
                    if len(from_parts) > 1:
                        table_parts = from_parts[1].strip().split()
                        if table_parts:
                            table = table_parts[0].strip()
                            
                            # Use select method for querying
                            # This is limited and doesn't support complex queries
                            result = self.select(table)
                            results.append(result)
                    else:
                        results.append({'error': 'Could not parse SELECT statement'})
                except Exception as e:
                    results.append({'error': str(e)})
            else:
                # For other queries (CREATE, INSERT, etc.), use a direct database connection
                # This is not ideal but necessary since we can't use function calls
                # These operations require elevated privileges
                url = f"{self.url}/rest/v1/{statement.lower().split()[1] if len(statement.split()) > 1 else 'unknown'}"
                headers = self.admin_headers.copy()
                headers['Prefer'] = 'return=minimal'  # Don't return the response body
                
                # Try to execute the statement
                try:
                    if statement.lower().startswith('create'):
                        # Handle CREATE TABLE statements differently
                        # In real scenarios, use migrations in Supabase UI
                        results.append({'info': 'CREATE statements should be executed manually in Supabase UI'})
                    elif statement.lower().startswith('insert'):
                        # Simplified INSERT handling
                        # This won't work for complex inserts
                        results.append({'info': 'INSERT statements should use the insert() method'})
                    else:
                        results.append({'info': 'Unsupported operation', 'statement': statement})
                except Exception as e:
                    results.append({'error': str(e), 'statement': statement})
        
        return results

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
