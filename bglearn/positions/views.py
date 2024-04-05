from django.shortcuts import render

from bglearn.positions.models import Position


def index(request):
    positions = Position.objects.all()
    return render(
        request, template_name="position.html", context={"positions": positions}
    )
