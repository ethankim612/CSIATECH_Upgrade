from django.shortcuts import render
from django.http import HttpResponseRedirect


# Create your views here.
def club_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect("https://csiatech.kr/")

    context = {}
    context["student_id"] = request.user.student_id
    return render(request, "club.html")