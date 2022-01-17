from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, my name is Yagnesh. You're at the polls index.")
    
