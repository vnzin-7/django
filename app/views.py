from django.shortcuts import render

def index(request):
    return render(request, "app/index.html")
    return render(request,"tindex.html")
