from rest_framework import serializers
from .models import Vehicle

class vehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ('id','owner', 'plaque', 'vin', 'brand','sub_brand','verify_reason','service','line','no_tech','folio')
        read_only_fields = ('date', )
