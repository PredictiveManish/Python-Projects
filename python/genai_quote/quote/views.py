from django.shortcuts import render
def home(request):
    return render(request, 'quote/home.html')