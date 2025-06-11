from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Incident, Treballador

def llista_incidencies(request):
    query = request.GET.get("q", "")
    assigned_to = request.GET.get("assigned_to", "")

    incidencies = Incident.objects.all()

    if query:
        incidencies = incidencies.filter(title__icontains=query)

    if assigned_to:
        incidencies = incidencies.filter(assigned_to_id=assigned_to)

    paginator = Paginator(incidencies.order_by("-created_at"), 10)
    page_number = request.GET.get("page")
    paginated_incidencies = paginator.get_page(page_number)

    treballadors = Treballador.objects.all()

    return render(
        request,
        "incidencies/llista_incidencies.html",
        {
            "incidencies": paginated_incidencies,
            "query": query,
            "assigned_to": assigned_to,
            "treballadors": treballadors,
        },
    )
