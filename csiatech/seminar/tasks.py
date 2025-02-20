from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.core.management import call_command


@shared_task
def run_clear_room():
    try:
        # Call the Django management command 'clear_room'
        call_command("clear_room")
        print("clear_room complete")
        print("Successfully ran clear_room management command")
    except Exception as e:
        print(f"Clear room script error: {e}")


@shared_task
def run_update_seminar():
    try:
        # Call the Django management command 'update_seminar'
        call_command("update_seminar")
        print("update_seminar complete")
        print("Successfully ran update_seminar management command")
    except Exception as e:
        print(f"Update seminar script error: {e}")