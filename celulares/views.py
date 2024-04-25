from django.shortcuts import render
from .models import CelularesBase, Avaliacao
from .serializer import CelularesSerializer
from rest_framework import generics
from rest_framework import viewsets



"""
    API V1
"""

class CelularesViewSet(viewsets.ModelViewSet):
    queryset = CelularesBase.objects.all()
    serializer_class = CelularesSerializer

class AvaliacoesViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = CelularesSerializer



class CelularAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = CelularesBase.objects.all()
    serializer_class = CelularesSerializer


