from django.urls import path
from . import views


urlpatterns = [
    path('', views.IndexView.as_view()),
    path('contact/', views.ContactView.as_view())
]
