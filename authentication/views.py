from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    print("this page is call from views")
    return render(request,"index.html",{})
    # return HttpResponse("<h1>Hello this is Index page<h1>")

# def home(request):
#     print("this page is call from views")
#     return render(request,"home.html",{})
    # return HttpResponse("<h1>Hello this is Home page <h1>")

def about(request):
    return render(request, "about.html",{})
def features(request):
    return render(request,"features.html",{})
def contact(request):
    return render(request,"contact.html",{})
def webcam_view(request):
    return render(request, 'registration/webcam.html')