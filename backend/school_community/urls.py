from django.contrib import admin
from django.urls import 
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, this is the School Community homepage!")

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
]