from django.shortcuts import render

# Create your views here.
def a(request):
    d = {"x":0, "y":5}
    return render(request, "If.html", context=d)

def b(request):
    d = {"name" : "SOUMYA"}
    return render(request, "Loop.html", context=d)

def c(request):
    d = {"a":20, "b":30,"c":50}
    return render(request, "Elif.html",d)