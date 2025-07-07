import os

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .utils import check_service_status
from django.conf import settings
from dotenv import load_dotenv

load_dotenv()
METABASE_URL = os.getenv("METABASE_URL")
DEFAULT_TABLE = os.getenv("DEFAULT_TABLE_URL")

@login_required
def dashboard_view(request):
    return render(request, "dashboard.html", {"user": request.user})

@login_required
def services_view(request):
    services = [
        {"name": "GitHub", "url":  "https://github.com"},
        {"name": "Metabase", "url": METABASE_URL},
        {"name": "Default-table", "url": DEFAULT_TABLE}
    ]
    return render(request, "services.html", {"services": services})

@login_required
def services_status_view(request):
    services = settings.SERVICES
    statuses = {
        name: check_service_status(config)
        for name, config in services.items()
    }
    return render(request, "services_status.html", {"statuses": statuses})