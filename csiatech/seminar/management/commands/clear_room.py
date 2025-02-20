# seminar/management/commands/clear_room.py

from django.core.management.base import BaseCommand
from seminar.models import Reservation, Room


class Command(BaseCommand):
    help = "Clears all reservations and resets room availability"

    def handle(self, *args, **kwargs):

        self.stdout.write("Starting to clear reservations...")
        # Clear all reservations
        Reservation.objects.all().delete()
        self.stdout.write("Cleared all reservations.")

        # Reset all room periods to False
        Room.objects.update(period1=False, period2=False, period3=False)
        self.stdout.write("Reset all room periods to False.")

        self.stdout.write(
            self.style.SUCCESS(
                "Successfully cleared all reservations and reset room availability"
            )
        )