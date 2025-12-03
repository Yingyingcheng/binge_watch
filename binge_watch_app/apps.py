# binge_watch_app/apps.py

from django.apps import AppConfig


class BingeWatchAppConfig(AppConfig):
    # This ensures your primary keys are defined correctly
    default_auto_field = 'django.db.models.BigAutoField'
    
    # 🌟 This is the crucial line that defines the app's name 🌟
    name = 'binge_watch_app' 
    
    # This line explicitly sets the application label, solving the RuntimeError
    label = 'binge_watch_app'