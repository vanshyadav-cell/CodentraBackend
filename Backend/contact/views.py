from rest_framework import generics
from .models import Contact
from .serializers import ContactSerializer
# create views here
class ContactCreateView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

from .models import Career
from .serializers import CareerSerializer
class CareerCreateView(generics.CreateAPIView):
    queryset = Career.objects.all()
    serializer_class = CareerSerializer