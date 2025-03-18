from django.apps import AppConfig
import asyncio

class PresenceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'presence'

    def ready(self):
        # Start the database monitor when the app starts
        from .database_monitor import DatabaseMonitor
        monitor = DatabaseMonitor(check_interval=5)
        
        # Run the monitor in a separate thread to avoid blocking
        import threading
        monitor_thread = threading.Thread(
            target=lambda: asyncio.run(monitor.start_monitoring())
        )
        monitor_thread.daemon = True
        monitor_thread.start()
