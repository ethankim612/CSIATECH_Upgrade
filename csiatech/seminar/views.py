from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseRedirect
from .models import Reservation, Room
import json
from django.db.models import Q


def update_room_status():
    # Fetch all Room objects and reset all periods to False
    rooms = Room.objects.all()
    for room in rooms:
        room.period1 = False
        room.period2 = False
        room.period3 = False
        room.save()

    # Retrieve all reservations and update room status based on each reservation
    reservations = Reservation.objects.all()
    for reservation in reservations:
        room = Room.objects.get(room_number=reservation.room_number)

        # Update room periods based on the reservation's periods
        if reservation.period1:
            room.period1 = True
        if reservation.period2:
            room.period2 = True
        if reservation.period3:
            room.period3 = True

        room.save()  # Save changes for each room after updating periods

    return JsonResponse({"status": "Rooms updated based on reservations"})


@csrf_exempt
def seminar_room_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect("https://csiatech.kr/")

    current_student_id = request.user.student_id

    if request.method == "DELETE":
        reservation_data = json.loads(request.body)  # Load JSON data

        room_number = reservation_data.get("room_number")
        student_ids = [
            reservation_data.get("student1"),
            reservation_data.get("student2"),
            reservation_data.get("student3"),
            reservation_data.get("student4"),
            reservation_data.get("student5"),
            reservation_data.get("student6"),
        ]
        print(student_ids)

        # Delete the reservation
        Reservation.objects.filter(
            Q(room_number=room_number)
            & Q(student1__contains=str(student_ids[0]))
            & Q(period1=reservation_data.get("period1"))
            & Q(period2=reservation_data.get("period2"))
            & Q(period3=reservation_data.get("period3"))
        ).delete()

        # Update room status
        update_room_status()

        return JsonResponse({"status": "canceled"})

    if request.method == "GET" and request.headers.get("type") == "retrieve":
        print("GET recieved")
        current_student_id = request.user.student_id
        print(current_student_id)

        # Retrieve the reservation details for the logged-in student
        student_reservation = Reservation.objects.filter(
            Q(student1__contains=str(current_student_id))
            | Q(student2__contains=str(current_student_id))
            | Q(student3__contains=str(current_student_id))
            | Q(student4__contains=str(current_student_id))
            | Q(student5__contains=str(current_student_id))
            | Q(student6__contains=str(current_student_id))
        ).first()

        # Fetch all room statuses
        rooms = Room.objects.all()
        room_status = {
            room.room_number: {
                "period1": room.period1,
                "period2": room.period2,
                "period3": room.period3,
            }
            for room in rooms
        }

        if student_reservation:
            student1 = student_reservation.student1
            student2 = student_reservation.student2
            student3 = student_reservation.student3
            student4 = student_reservation.student4
            student5 = student_reservation.student5
            student6 = student_reservation.student6
            data = {
                "status": "reserved",
                "room_number": student_reservation.room_number,
                "student1": student1,
                "student2": student2,
                "student3": student3,
                "student4": student4,
                "student5": student5,
                "student6": student6,
                "period1": student_reservation.period1,
                "period2": student_reservation.period2,
                "period3": student_reservation.period3,
                "room_status": room_status,  # Include room status in the response
            }
        else:
            data = {
                "status": "notreserved",
                "room_status": room_status,
            }  # No reservation found, but include room status

        return JsonResponse(data)

    if request.method == "POST":

        reservation_data = json.loads(request.body)

        room_number = int(reservation_data.get("room_number"))
        period1 = bool(reservation_data.get("period1"))
        period2 = bool(reservation_data.get("period2"))
        period3 = bool(reservation_data.get("period3"))
        student_ids = [
            reservation_data.get("student1"),
            reservation_data.get("student2"),
            reservation_data.get("student3"),
            reservation_data.get("student4"),
            reservation_data.get("student5"),
            reservation_data.get("student6"),
        ]

        # If the student already has a reservation, cancel it
        # Create new reservation
        Reservation.objects.create(
            student1=student_ids[0],
            student2=student_ids[1],
            student3=student_ids[2],
            student4=student_ids[3],
            student5=student_ids[4],
            student6=student_ids[5],
            period1=period1,
            period2=period2,
            period3=period3,
            room_number=room_number,
        )

        # Update room status
        update_room_status()

        return JsonResponse({"status": "reserved"})

    # Retrieve the reservation details for the logged-in student


    context = {}
    context["student_id"] = request.user.student_id  # student_id 추가

    return render(request, "seminar.html", context)