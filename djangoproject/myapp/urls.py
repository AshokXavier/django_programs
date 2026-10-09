from django.urls import path
from . import views
urlpatterns=[
  path('gallery/',views.image_gallery,name='image_gallery'),
  path('profile/',views.my_profile,name="my_profile"),
  path('student_list/',views.student_list,name='student_list'),
  path('student_dict/',views.student_dict,name='student_dict'),
  path('inheritance/',views.inhertitance,name='inheritance'),
  path('',views.class_details,name='class_details')
]

