from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .utils import check_service_status
from django.conf import settings

@login_required
def dashboard_view(request):
    return render(request, "dashboard.html", {"user": request.user})

@login_required
def services_view(request):
    services = [
        {"name": "GitHub", "url":  "https://github.com"},
        {"name": "Metabase", "url": "https://metabase_rsbu.docker03.ratings.ru/auth/login?redirect=%2F"},
        {"name": "Default-table", "url": "https://defaults_table_editor.docker03.ratings.ru"}
    ]
    return render(request, "services.html", {"services": services})

@login_required
def services_status_view(request):
    services = settings.SERVICES
    statuses = {
        name: check_service_status(url)
        for name, url in services.items()
    }
    return render(request, "services_status.html", {"statuses": statuses})