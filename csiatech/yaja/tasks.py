
from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.core.management import call_command


@shared_task
def run_reset_script():
    try:
        from .management.commands.reset_schedules import reset_schedules

        # Call the Django management command 'reset_schedules'
        call_command("reset_schedules")
        print("reset complete")
        print("Successfully ran reset_schedules management command")
    except Exception as e:
        print(f"Reset script error: {e}")


@shared_task
def run_update_script():
    try:
        from .management.commands.update_google_sheet import update_google_sheet

        # Call the Django management command 'reset_schedules'
        call_command("update_google_sheet")
        print("update complete")
        print("Successfully ran update_google_sheet management command")
    except Exception as e:
        print(f"Update script error: {e}")
