from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from app import models
from api import serializers


class OpenCelliDViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple viewset to retrieve all the OpenCelliD with filter.
    """
    queryset = models.OpenCelliD.objects.all()
    serializer_class = serializers.OpenCelliDSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['mcc', 'net', 'area', 'cell']