from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import StaticHTMLRenderer, TemplateHTMLRenderer, JSONRenderer

from django.utils.encoding import smart_text
from rest_framework import renderers

from .models import User
from .serializers import UserSerializer

from rest_framework.settings import api_settings
from rest_framework_csv import renderers as r

@api_view(['GET'])
@renderer_classes([StaticHTMLRenderer])
def simple_html_view(request):
    data = '<html><body><h1>Hello, world</h1></body></html>'
    return Response(data)

@api_view(['GET', 'POST'])
@renderer_classes([JSONRenderer, r.CSVRenderer ])
def list_users(request):
    """
    A view that can return JSON or CSV representations
    of the users in the system.
    """
    queryset = User.objects.all()

    if request.method == 'POST':
        
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'GET':

        serializer = UserSerializer(queryset, many=True)

        if request.accepted_renderer.format == 'csv':
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.data)
