from rest_framework import serializers
from app import models


class OpenCelliDSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.OpenCelliD
        
        fields = ('mcc', 'net', 'area', 'cell')
        depth = 1