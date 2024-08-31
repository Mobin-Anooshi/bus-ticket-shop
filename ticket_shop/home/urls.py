from django.urls import path
from home import views


urlpatterns = [
    path('',views.HomeView.as_view()),
    path('create/',views.CreateTravel.as_view()),
]
