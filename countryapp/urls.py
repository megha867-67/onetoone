from django.urls import path
from .import views
urlpatterns=[
    path('',views.insertcountry,name='insertcountry'),
    path('countries/',views.countrylist,name='countrylist')
]