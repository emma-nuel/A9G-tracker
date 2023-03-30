from .models import MyTracker
from rest_framework import serializers

class MyTrackerDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyTracker
        fields = '__all__'
