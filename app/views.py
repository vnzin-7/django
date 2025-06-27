from django.shortcuts import render

def index(request):
    return render(request, "app/index.html")
    return render(request,"tindex.html")

def pagina1(request):
    return render(request, 'pagina1.html')

def pagina2(request):
    return render(request, 'pagina2.html')
