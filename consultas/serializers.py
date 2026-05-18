from rest_framework import serializers
from .models import Consulta
from datetime import date

class ConsultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consulta
        fields = '__all__'

    def validate_data(self, value):
        if value < date.today():
            raise serializers.ValidationError("A data de consulta não pode ser no passado.")
        return value