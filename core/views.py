from django.shortcuts import render
from .models import Client, ImageClie

# Create your views here.

def home(request):

    client = Client.objects.all()

    return render(request, "home.html", {
        "title" : "Galeria",
        "clients": client
    })

def gall_client(request):

    # img_client = ImageClie.objects.get(category=category)
    img_client = ImageClie.objects.all()

    print(img_client)
    return render(request, "client.html",{
        "galleries": img_client
    })