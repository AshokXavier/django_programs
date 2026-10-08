from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def image_gallery(request):
  return render(request,'image_gallery.html')

def my_profile(request):
  return HttpResponse("Hi My Name is Ashok") #to show a content in response

def student_list(request):
  student_details=['Ashok','Jithu','Ram','Deepu']
  return render(request,'new_page.html',{'names':student_details})

def student_dict(request):
  student_details={
    "Ashok":40,
    "Jithu":45,
    "Ram":48,
    "Deepu":43
  }

  return render(request,'dictionary.html',{'details':student_details})

def inhertitance(request):
  return render(request,'child.html')