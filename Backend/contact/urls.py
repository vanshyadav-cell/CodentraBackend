from django.urls import path
from .views import ContactCreateView
from .views import CareerCreateView
urlpatterns = [
    path("contact/", ContactCreateView.as_view(), name="contact"),
    path("career/", CareerCreateView.as_view(), name="career"),
]