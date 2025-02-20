# myapp/management/commands/reset_schedules.py
from django.core.management.base import BaseCommand
from django.utils import timezone
from django.contrib.auth import get_user_model
from login.models import CustomUser
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


def reset_schedules(user):
    try:
        default_monday = DefaultMonday.objects.get(student_id=user)
        default_tuesday = DefaultTuesday.objects.get(student_id=user)
        default_wednesday = DefaultWednesday.objects.get(student_id=user)
        default_thursday = DefaultThursday.objects.get(student_id=user)

        Monday.objects.filter(student_id=user).update(
            period1=default_monday.period1,
            period2=default_monday.period2,
            period3=default_monday.period3,
        )
        Tuesday.objects.filter(student_id=user).update(
            period1=default_tuesday.period1,
            period2=default_tuesday.period2,
            period3=default_tuesday.period3,
        )
        Wednesday.objects.filter(student_id=user).update(
            period1=default_wednesday.period1,
            period2=default_wednesday.period2,
            period3=default_wednesday.period3,
        )
        Thursday.objects.filter(student_id=user).update(
            period1=default_thursday.period1,
            period2=default_thursday.period2,
            period3=default_thursday.period3,
        )
        print("Successfully reset user schedules to default values")
    except (
        DefaultMonday.DoesNotExist,
        DefaultTuesday.DoesNotExist,
        DefaultWednesday.DoesNotExist,
        DefaultThursday.DoesNotExist,
    ):
        return None

    return {"status": "success", "endswith": "terminated"}


class Command(BaseCommand):
    print("command called on reset_schedules.py")
    help = "Resets user schedules to default values every Friday"

    def handle(self, *args, **kwargs):
        today = timezone.now().date()
        for user in CustomUser.objects.all():
            if user.student_id == "11111":
                continue
            print(type(user.student_id))
            print(user.student_id)
            result = reset_schedules(user.student_id)
            if result["status"] == "success":
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Successfully reset schedules for user {user.student_id}"
                    )
                )
            else:
                self.stdout.write(
                    self.style.WARNING(
                        f"Failed to reset schedules for user {user.student_id}: {result.get('message', '')}"
                    )
                )