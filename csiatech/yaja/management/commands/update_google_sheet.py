import requests
import datetime
from ...models import Monday, Tuesday, Wednesday, Thursday  # Update with your app name
from django.core.management.base import BaseCommand

GOOGLE_APPS_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbzgcGleKi_yqXuzFwFXPJTMRf1Dfe0F-hcDUrirmgdQuIYITYTq297KsRmB1PxzBuXj/exec"


def fetch_schedule():
    day_of_week = datetime.datetime.today().weekday()
    if day_of_week in [0, 4, 5, 6]:  # Assuming Monday to be used on weekends as well
        schedules = Monday.objects.all()
    elif day_of_week == 1:
        schedules = Tuesday.objects.all()
    elif day_of_week == 2:
        schedules = Wednesday.objects.all()
    elif day_of_week == 3:
        schedules = Thursday.objects.all()
    else:
        return None
    return schedules


def update_google_sheet():
    schedules = fetch_schedule()
    if not schedules:
        print("No schedules to update for today.")
        return

    # Prepare the payload with type and updates
    updates = []
    for schedule in schedules:
        updates.append(
            {
                "student_id": schedule.student_id,
                "period1": schedule.period1,
                "period2": schedule.period2,
                "period3": schedule.period3,
            }
        )

    payload = {"type": "yaja", "updates": updates}

    print("Payload to send:", payload)

    response = requests.post(
        GOOGLE_APPS_SCRIPT_URL, json=payload  # Send the payload as JSON
    )
    if response.status_code == 200:
        print("Google Sheet updated successfully.")
    else:
        print("Failed to update Google Sheet.", response.text)


class Command(BaseCommand):
    help = "Resets user schedules to default values every Friday"

    def handle(self, *args, **kwargs):
        update_google_sheet()