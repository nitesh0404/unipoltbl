from rest_framework.serializers import ModelSerializer
from .models import operational_parameter

class Op_Serializer(ModelSerializer):
    class Meta:
        model = operational_parameter
        fields = '__all__'