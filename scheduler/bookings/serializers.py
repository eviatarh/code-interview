from rest_framework import serializers

from .models import Availabilities, Speciality, Provider

class AvailabilitieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Availabilities
        fields = '__all__'  #or a tupple


class SpecialitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Speciality
        fields = '__all__'


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = ('name', )

