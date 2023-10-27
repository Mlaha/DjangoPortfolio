from django.urls import path
from . import views


urlpatterns=[
 path('', views.Home, name="Home"),
    path('About/', views.About, name="About"),
    path('Contact/', views.Contact, name="Contact"),
    path('Services/', views.Services, name="Services"),
     path('Portfolio/', views.Portfolio, name="Portfolio"),

]

