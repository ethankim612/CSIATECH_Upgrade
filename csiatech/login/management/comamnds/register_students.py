# myapp/management/commands/register_students.py
import os
import json
import requests
from django.core.management.base import BaseCommand
from login.models import CustomUser


class Command(BaseCommand):
    help = "Register users from a Google Spreadsheet"

    def handle(self, *args, **kwargs):
        sheet_url = "https://script.google.com/macros/s/AKfycbxTVvkT4ZIsIjhTIFlqcGiOwKGtF59MIVwlE6Qu2D-ikilXo2ZlxKoxMbLfIfLD-n3Qjw/exec"  # Fetch from environment variable
        response = requests.get(sheet_url)
        if response.status_code != 200:
            self.stdout.write(
                self.style.ERROR("Failed to fetch data from Google Sheets")
            )
            return

        data = response.json()
        for entry in data:
            student_id = entry.get("student_id")
            password = entry.get("password")

            if student_id and password:
                if not CustomUser.objects.filter(student_id=student_id).exists():
                    CustomUser.objects.create_user(student_id=student_id)
                    cur = CustomUser.objects.get(student_id=student_id)
                    cur.password = password
                    cur.save()
                    self.stdout.write(
                        self.style.SUCCESS(
                            f"Successfully created user with student_id: {student_id}, {password}"
                        )
                    )
                else:
                    self.stdout.write(
                        self.style.WARNING(
                            f"User with student_id: {student_id} already exists"
                        )
                    )

        self.stdout.write(self.style.SUCCESS("Finished processing all students"))