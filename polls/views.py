from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("Hello, world 123. You're at the polls index.")