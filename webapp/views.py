from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
'''
def home(request):
    message = "Example Django project on vercel"
    return HttpResponse(message)
'''    
def index_view(request):
    return render(request, "yourApp/index.html", {})

def accessibility_view(request):
    return render(request, "yourApp/accessibility.html", {})
