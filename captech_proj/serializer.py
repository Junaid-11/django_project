from rest_framework.serializers import ModelSerializer
from .models import *


class ProfileSer(ModelSerializer):
    class Meta:
        model=Profile
        fields='__all__'

class ProductSer(ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'