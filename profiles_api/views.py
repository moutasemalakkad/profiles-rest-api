from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializer

#from rest_framework import authentication, permissions
#from django.contrib.auth.models import User


class HelloApiView(APIView):
    """Test APIVIEW"""
    serializer_class = serializer.HelloSerializer

    def get(self, request, format=None):
        """Return a list of API features """
        an_apiview = [
            'User an HTTP(get, post, patch, put, delete)',
            'is similar to a tradational Django view'    ,
            'gives you the most control over your app logic' ,
            'mapped manually'
        ]

        return Response({
                        'message' : 'hello world',
                        'an_apiview' : an_apiview
                        })

    def post(self, request):
        """post hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            print(serializer.validated_data)
            name =  serializer.validated_data.get('name')
            message = f'Hi {name}'
            return Response({'message' : message})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """modify name"""
        return Response({'method' : 'PUT'})

    def patch(self, request, pk=None):
        """partial update"""
        return Response({'method' : 'PATCH'})

    def delete(self, request, pk=None):
        """delete"""
        return Response({'method' : 'DELETE'})
