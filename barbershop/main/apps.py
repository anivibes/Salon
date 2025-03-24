from django.apps import AppConfig


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'
    
    def ready(self):
        """Initialize the app - run the database setup functions."""
        # Import here to avoid circular imports
        try:
            from .db_init import initialize_database
            initialize_database()
        except Exception as e:
            print(f"Error initializing database: {str(e)}")
