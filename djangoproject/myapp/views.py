from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def image_gallery(request):
  return render(request,'image_gallery.html')

def my_profile(request):
  return HttpResponse("Hi My Name is Ashok") #to show a content in response