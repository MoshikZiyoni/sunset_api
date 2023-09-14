from django.forms import ModelForm
from rest_framework.serializers import ModelSerializer
from app.models import SunSet
class SunSetSerializer(ModelSerializer):
    class Meta:
        model = SunSet
        fields='__all__'