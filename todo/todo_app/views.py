from django.shortcuts import render

import datetime


def index(request):
    context = {"current_date": datetime.date.today()}
    return render(request, "index.html", context)
