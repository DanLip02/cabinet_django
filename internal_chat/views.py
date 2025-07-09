from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Message
from .forms import MessageForm

@login_required
def chat_room(request):
    messages = Message.objects.select_related('sender').order_by('-timestamp')[:50][::-1]

    if request.method == 'POST':
        form = MessageForm(request.POST, request.FILES)
        if form.is_valid():
            msg = form.save(commit=False)
            msg.sender = request.user
            msg.save()
            return redirect('chat_room')
    else:
        form = MessageForm()

    return render(request, 'chat_room.html', {
        'messages': messages,
        'form': form
    })