from django.apps import AppConfig


class FilesharingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.filesharing'

    def ready(self):
        """Run tasks"""
        from .tasks import Scheduler
        tasks = Scheduler()
        tasks.run_tasks()
