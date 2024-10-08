from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from .models import Message, ChatRoom, ChatRoomMembership
from django.contrib.auth.models import User
from django.utils import timezone
from openai import OpenAI
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

def index(request):
    chat_rooms = []
    if request.user.is_authenticated:
        chat_rooms = request.user.chat_rooms.all()
    return render(request, "chat/index.html", {'chat_rooms': chat_rooms})


@login_required
def room(request, room_name):
    # get or create chat room
    chat_room, created = ChatRoom.objects.get_or_create(name=room_name, defaults={'owner':request.user})

    bot_user = User.objects.get(username="ChatterBox")

    # If the room is created, send a welcome message from the bot
    if created:
        Message.objects.create(
            user=bot_user,
            room_name=room_name,
            content="Welcome to the chat room! Prefix messages with '!' to interact with me."
        )

    membership, _ = ChatRoomMembership.objects.get_or_create(user=request.user, chat_room=chat_room)
    missed_messages = Message.objects.filter(room_name=room_name, timestamp__gt=membership.last_accessed)[:30]
    count = missed_messages.count()
    recap_summary = None
    if count >= 5:
        recap_summary = f"You missed {count}{'+' if count == 30 else ''} messages since your last visit:"

    if not chat_room.members.filter(id=request.user.id).exists():
        chat_room.members.add(request.user)

        Message.objects.create(
            user=bot_user,
            room_name=room_name,
            content=f"{request.user} just joined!"
        )

    return render(request, 'chat/room.html', {
        "room_name":room_name, 
        "recap_summary":recap_summary,
        'count': count
    })


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
    chat_rooms = ChatRoom.objects.filter(name=room_name, members=request.user)

    if not chat_rooms.exists():
        raise ValueError(f"ChatRoom with name '{room_name}' does not exist.")
    
    for chat_room in chat_rooms:
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


@csrf_exempt
def get_recap_summary(request, room_name, count):
    if request.method == 'GET' and request.user.is_authenticated:
        print(room_name, count)
        missed_messages = Message.objects.filter(room_name=room_name).order_by('-timestamp')[:count]
        missed_messages = reversed(missed_messages)

        recap_text = "\n".join(f"{msg.user.username}: {msg.content}" for msg in missed_messages)
        client = OpenAI(api_key=settings.OPENAI_API_KEY)
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": f"summarize these missed messages in less than 100 words: {recap_text}",
                }
            ],
            model="gpt-4o-mini",
            max_tokens=150,
        )

        recap_summary = response.choices[0].message.content
        return JsonResponse({"recap_summary": recap_summary})
    return JsonResponse({"error": "Invalid request"}, status=400)