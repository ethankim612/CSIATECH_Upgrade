from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login
from .models import CustomUser
import json


@csrf_exempt
def custom_login(request):
    if request.method == "POST":
        # Get data from the form
        data = json.loads(request.body.decode("utf-8"))
        student_id = data.get("student_id")
        password = data.get("password")

        try:
            user = CustomUser.objects.get(student_id=student_id, password=password)

            # Clear any existing sessions for this user
            request.session.flush()

            # Log in the user
            login(request, user)

            # Configure session settings
            request.session["user_id"] = user.id
            request.session["student_id"] = student_id

            request.session.set_expiry(1800)  # 30 minutes in seconds

            # Set session cookie settings
            request.session.set_test_cookie()

            return JsonResponse(
                {"status": "success", "session_id": request.session.session_key}
            )

        except CustomUser.DoesNotExist:
            return JsonResponse(
                {"error": "Invalid login credentials. Please check your inputs."},
                status=400,
            )

    return render(request, "login.html")