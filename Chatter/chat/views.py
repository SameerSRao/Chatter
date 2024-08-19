from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from .models import Message, ChatRoom

def index(request):
    chat_rooms = []
    if request.user.is_authenticated:
        chat_rooms = request.user.chat_rooms.all()
    return render(request, "chat/index.html", {'chat_rooms': chat_rooms})

@login_required
def room(request, room_name):
    chat_room, created = ChatRoom.objects.get_or_create(name=room_name, owner=request.user)
    chat_room.members.add(request.user)
    return render(request, 'chat/room.html', {"room_name":room_name})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form':form})

def logout_view(request):
    logout(request)
    return redirect('login')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form':form})

def chat_history(request, room_name):
    messages = Message.objects.filter(room_name=room_name).order_by('timestamp')
    message_list = [{"user": msg.user.username, "content": msg.content} for msg in messages]
    return JsonResponse({"messages": message_list})

def leave_room(request, room_name):
    chat_room = get_object_or_404(ChatRoom, name=room_name)

    if not chat_room.id:
        raise ValueError(f"ChatRoom with name '{room_name}' does not exist.")

    chat_room.members.remove(request.user) 

    if request.user == chat_room.owner or chat_room.members.count() == 0:
        chat_room.delete()
        Message.objects.filter(room_name=room_name).delete()

    return redirect('index')

def owned_rooms_view(request):
    if request.user.is_authenticated:
        owned_rooms = request.user.owned_rooms.all()
    else:
        owned_rooms = []

    return render(request, 'chat/owned_rooms.html', {'owned_rooms': owned_rooms})