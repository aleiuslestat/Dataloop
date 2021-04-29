from django.shortcuts import render

# Create your views here.
def home(request):
    titulo = 'Home'
    return render(request,'home.html', {'titulo':titulo})