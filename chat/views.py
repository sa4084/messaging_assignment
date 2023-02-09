from django.shortcuts import render, redirect
from .models import Message
from .forms import MessageForm
from django.contrib import messages
from django.http import JsonResponse
from django.core import serializers
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# import uuid
# from django.db import models


# Create your views here.
def home(request):
    all_members = Message.objects.all()
    print(type(all_members))
    # return JsonResponse({'all': all_members})
    return JsonResponse(list(all_members.values()), safe=False)
    # return render(request, {'all': all_members})

def count(request):
    all_members = Message.objects.all()
    print(len(all_members))
    return JsonResponse(len(all_members), safe=False)


def sent(request, user_id):
    all_members = Message.objects.all().filter(sender=user_id)
    print(type(all_members))
    
    # return JsonResponse({'all': all_members})
    return JsonResponse(list(all_members.values()), safe=False)
    # return render(request, {'all': all_members})

def inbox(request, user_id):
    all_members = Message.objects.all().filter(recipent=user_id)
    print(type(all_members))
    
    # return JsonResponse({'all': all_members})
    return JsonResponse(list(all_members.values()), safe=False)
    # return render(request, {'all': all_members})

@csrf_exempt 
def compose(request):
    print("hitting")
    if request.method == "POST":
        # print(request.body)
        # form = MessageForm(request.POST or None)
        recipent = request.POST.get('recipent')
        title = request.POST.get('title')
        message = request.POST.get('message')
        sender = request.POST.get('sender')
        # id_msg = request.POST.get('id')
        data = {
            # 'id': id,
            'sender': sender,
            'recipent': recipent,
            'title': title,
            'message': message
        }

        Message.objects.create(
            recipent = recipent,
            title = title,
            message = message,
            # id = uuid.uuid4().int & (1<<64)-1,
            sender = sender
        )
        # form(data)
        # form = UserQueueForm(initial=data)
        print(recipent)
        print(title)
        print(message)

        return HttpResponse(True) 

    else:
        return render(request, 'compose.html', {})

def delete_event(request, event_id):
    event = Message.objects.get(pk=event_id)
    event.delete()
    all_members = Message.objects.all
    return HttpResponse(True) 


