from django.urls import path
from challenges import views

urlpatterns = [
    path('', views.home, name="home"),
    path("<int:month>", views.monthly_challenges_by_number),
    path("<str:month>", views.monthly_challenge, name="monthly-challenge"),
]

