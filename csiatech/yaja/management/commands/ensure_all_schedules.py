from django.core.management.base import BaseCommand
from django.core.exceptions import ObjectDoesNotExist
from yaja.models import (
    Monday,
    Tuesday,
    Wednesday,
    Thursday,
    DefaultMonday,
    DefaultTuesday,
    DefaultWednesday,
    DefaultThursday,
)
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = "Ensure that all schedule records exist for every custom user and create them if they do not."

    def handle(self, *args, **kwargs):
        User = get_user_model()
        users = User.objects.all()

        for user in users:
            student_id = user.student_id
            self.ensure_schedule_exists(student_id)

        self.stdout.write(self.style.SUCCESS("All schedules ensured for all users."))

    def ensure_schedule_exists(self, student_id):
        models = [
            (Monday, DefaultMonday),
            (Tuesday, DefaultTuesday),
            (Wednesday, DefaultWednesday),
            (Thursday, DefaultThursday),
        ]

        for model, default_model in models:
            try:
                model.objects.get(student_id=student_id)
                default_model.objects.get(student_id=student_id)
            except ObjectDoesNotExist:
                default_model.objects.get_or_create(
                    student_id=student_id,
                    period1="야자",
                    period2="야자",
                    period3="야자",
                )
                model.objects.get_or_create(
                    student_id=student_id,
                    period1="야자",
                    period2="야자",
                    period3="야자",
                )