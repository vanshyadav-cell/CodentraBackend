from rest_framework import serializers
from .models import Contact

class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = "__all__"


from .models import Career

class CareerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Career
        fields = "__all__"