from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseRedirect
from django.db import transaction
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
from datetime import datetime
from .models import Monday, Tuesday, Wednesday, Thursday
from .serializers import (
    MondaySerializer,
    TuesdaySerializer,
    WednesdaySerializer,
    ThursdaySerializer,
)


def get_schedule_model_for_current_day(student_id):
    current_day = datetime.now().weekday()
    model = {0: Monday, 1: Tuesday, 2: Wednesday, 3: Thursday}.get(current_day, Monday)
    return model.objects.filter(student_id=student_id).first()


@transaction.atomic
def ensure_schedule_exists(student_id):
    for model in [Monday, Tuesday, Wednesday, Thursday]:
        model.objects.get_or_create(
            student_id=student_id,
            defaults={"period1": "야자", "period2": "야자", "period3": "야자"},
        )


@transaction.atomic
def update_schedule(model, student_id, data, serializer_class):
    print(f"Updating {model.__name__} for student {student_id}")
    instance = model.objects.select_for_update().filter(student_id=student_id).first()
    serializer = serializer_class(instance, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print(f"Successfully updated {model.__name__} for student {student_id}")
        return None
    print(
        f"Error updating {model.__name__} for student {student_id}: {serializer.errors}"
    )
    return serializer.errors


@csrf_exempt
@api_view(["GET", "PUT"])
def yaja_view(request):
    if not request.user.is_authenticated or "user_id" not in request.session:
        request.session.flush()
        return HttpResponseRedirect("https://csiatech.kr/")

    session_student_id = request.session.get("student_id")
    current_student_id = request.user.student_id
    if session_student_id != current_student_id:
        request.session.flush()
        return HttpResponseRedirect("https://csiatech.kr/")

    schedule = get_schedule_model_for_current_day(current_student_id)

    ensure_schedule_exists(current_student_id)

    if request.method == "PUT":
        data = json.loads(request.body)
        print(data)
        try:
            with transaction.atomic():
                errors = {}
                for day, model, serializer_class in [
                    ("Monday", Monday, MondaySerializer),
                    ("Tuesday", Tuesday, TuesdaySerializer),
                    ("Wednesday", Wednesday, WednesdaySerializer),
                    ("Thursday", Thursday, ThursdaySerializer),
                ]:
                    if day_data := data.get(day):
                        if error := update_schedule(
                            model, current_student_id, day_data, serializer_class
                        ):
                            errors[day] = error

                if errors:
                    return Response(
                        {"status": "error", "errors": errors},
                        status=status.HTTP_400_BAD_REQUEST,
                    )

            return Response(
                {"status": "success", "student_id": current_student_id},
                status=status.HTTP_200_OK,
            )
        except Exception as e:
            print(f"Transaction failed: {str(e)}")
            return Response(
                {"status": "error", "message": "Transaction failed. Please try again."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    if request.method == "GET":
        if request.headers.get("X-Schedule-Type") == "current":
            model_serializer_pairs = [
                (Monday, MondaySerializer),
                (Tuesday, TuesdaySerializer),
                (Wednesday, WednesdaySerializer),
                (Thursday, ThursdaySerializer),
            ]

            response_data = {}
            for model, serializer_class in model_serializer_pairs:
                instance = model.objects.filter(student_id=current_student_id).first()
                serializer = serializer_class(instance)
                response_data[model.__name__.lower()] = serializer.data

            response_data["action"] = "retrieve"
            response_data["type"] = "current"
            print(response_data)

            return Response(response_data)

    return render(request, "yaja.html", {"Yaja": schedule})
