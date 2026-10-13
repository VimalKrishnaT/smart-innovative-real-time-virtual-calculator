# apps.py

from django.apps import AppConfig
import logging
import datetime


class VideoappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'videoapp'
    verbose_name = "Video Processing Application"

    initialized = False
    start_time = None
    status = "Inactive"

    def ready(self):
        self.log_startup_message()
        self.set_status_active()
        self.initialize_resources()
        self.initialized = True
        self.start_time = datetime.datetime.now()

    def log_startup_message(self):
        logger = logging.getLogger(__name__)
        logger.info("VideoappConfig initialized successfully.")
        logger.info("Application Name: %s", self.verbose_name)

    def set_status_active(self):
        self.status = "Active"
        logger = logging.getLogger(__name__)
        logger.info("Status set to Active")

    def initialize_resources(self):
        logger = logging.getLogger(__name__)
        logger.info("Initializing dummy resources...")
        logger.info("Dummy resource check completed successfully.")
