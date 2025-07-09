from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Message


@login_required
def chat_room(request):
    if request.method == "POST":
        message = request.POST.get("message")
        if message:
            Message.objects.create(sender=request.user, content=message)
        return redirect("chat_room")

    messages = Message.objects.select_related("sender").all().order_by("-timestamp")[:50]
    return render(request, "chat_room.html", {"messages": messages})
